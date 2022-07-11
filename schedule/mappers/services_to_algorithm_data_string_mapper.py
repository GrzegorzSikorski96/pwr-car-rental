import datetime
from typing import List

from django.db.models import QuerySet

from car.models import ScheduleService
from core.models import Address
from schedule.helpers.time import day_of_year_from_datetime, minutes_between_date_times


class ServicesToAlgorithmDataStringMapper:
    def __init__(self):
        self.lines = []
        self.data_string = ''

    def map(self, services: 'QuerySet[ScheduleService]', distances_map: List['Address']):
        self.lines.append('%d' % (len(services)))

        for index, service in enumerate(services):
            tmp_str = ''

            tmp_str += '%d 1 %d %d 360 %d %d' % (
                index + 1,
                day_of_year_from_datetime(datetime.date.today().__str__()),
                day_of_year_from_datetime(datetime.date.today().__str__()),
                distances_map.index(service.address),
                len(service.availabilities.all())
            )

            for availability in service.availabilities.all():
                tmp_str += ' %d %d %d' % (
                    minutes_between_date_times(
                        datetime.date(day=1, month=1, year=datetime.date.today().year).__str__(),
                        str(availability.start.replace(tzinfo=None))
                    ),
                    minutes_between_date_times(
                        datetime.date(day=1, month=1, year=datetime.date.today().year).__str__(),
                        str(availability.end.replace(tzinfo=None))
                    ),
                    distances_map.index(availability.address),
                )

            self.lines.append(tmp_str)

        self.data_string = '\n'.join(self.lines)

        return self.data_string
