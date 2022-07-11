import datetime

from django.db.models import QuerySet

from car.models import ScheduleService
from core.integrations.google_api.distance_matrix import DistanceMatrix
from core.models import User
from schedule.extractors.addresses_from_scheduled_services_extractor import AddressesFromScheduledServicesExtractor
from schedule.generators.schedule_generator import ScheduleGenerator
from schedule.helpers.time import add_minutes_to_date_time
from schedule.mappers.services_to_algorithm_data_string_mapper import ServicesToAlgorithmDataStringMapper
from schedule.models import Schedule, Event


class GenerateScheduleService:
    def __init__(self):
        self.addresses_from_scheduled_services_extractor = AddressesFromScheduledServicesExtractor()
        self.distances_matrix_service = DistanceMatrix()
        self.services_to_algorithm_data_string_mapper = ServicesToAlgorithmDataStringMapper()

    def generate(self):
        services: 'QuerySet[ScheduleService]' = ScheduleService.objects.filter(ended_at=None)
        addresses = self.addresses_from_scheduled_services_extractor.extract(services)

        self.distances_matrix_service.set_addresses(addresses)
        distances = self.distances_matrix_service.distance_matrix
        address_to_index_map = self.distances_matrix_service.address_to_index_map

        algorithm_string_data = self.services_to_algorithm_data_string_mapper.map(services, list(address_to_index_map))

        generated_routes = ScheduleGenerator().generate(algorithm_string_data, distances)

        self.__archive_schedules()

        for index, route in enumerate(generated_routes):
            schedule: 'Schedule' = Schedule()
            schedule.date = datetime.date.today()
            schedule.employee = User.objects.filter(groups__name='employee')[index]
            schedule.time = route.work_time
            schedule.save()

            for key in range(0, len(route.addresses)):
                if key == 0:
                    event = Event(
                        title='Start work',
                        start=add_minutes_to_date_time(
                            datetime.datetime(day=1, month=1, year=datetime.date.today().year), route.S[key]),
                        end=add_minutes_to_date_time(
                            datetime.datetime(day=1, month=1, year=datetime.date.today().year), (route.S[key] + 1)),
                        address=address_to_index_map[route.trace[key]]
                    )
                    schedule.events.add(event, bulk=False)
                    continue

                if key == (len(route.addresses)-1):
                    event = Event(
                        title='End work',
                        start=add_minutes_to_date_time(
                            datetime.datetime(day=1, month=1, year=datetime.date.today().year), route.C[0]),
                        end=add_minutes_to_date_time(
                            datetime.datetime(day=1, month=1, year=datetime.date.today().year), (route.C[0] + 1)),
                        address=address_to_index_map[route.trace[key]],
                    )
                    schedule.events.add(event, bulk=False)
                    continue

                if key < len(route.S):
                    event = Event(
                        title='Place %d' % key,
                        start=add_minutes_to_date_time(
                            datetime.datetime(day=1, month=1, year=datetime.date.today().year), route.S[key]),
                        end=add_minutes_to_date_time(
                            datetime.datetime(day=1, month=1, year=datetime.date.today().year), route.C[key]),
                        address=address_to_index_map[route.addresses[key]],
                    )
                    schedule.events.add(event, bulk=False)

    def __archive_schedules(self):
        schedules = Schedule.objects.filter(is_archive=False)

        for schedule in schedules:
            schedule.is_archive = True
            schedule.save()
