from typing import List

from schedule.data_transfer_objects.availability_dto import AvailabilityDTO
from schedule.data_transfer_objects.service_dto import ServiceDTO
from schedule.data_transfer_objects.vehicle_dto import VehicleDTO


def row_to_array(line: str) -> List[int]:
    array_line = line.replace(' \n', '').replace('\n', '').split(' ')

    return [int(x) for x in array_line]


def load_distances(file_name: str) -> List[List[int]]:
    distances_file = open(file_name, 'r')
    return [row_to_array(row) for row in distances_file]


def load_data(raw_data: List[str]) -> tuple[List['VehicleDTO'], List['ServiceDTO'], int]:
    vehicles_count = int(raw_data.pop(0))

    vehicles: List[VehicleDTO] = [VehicleDTO(0)]
    services: List[ServiceDTO] = [ServiceDTO(identifier=0, vehicle_identifier=0)]

    availability_counter = 1
    service_counter = 1

    for i in range(0, vehicles_count):
        row: list[int] = row_to_array(raw_data.pop(0))

        vehicle = VehicleDTO(identifier=row.pop(0))

        services_count = row.pop(0)
        for j in range(0, services_count):
            service = ServiceDTO(
                identifier=service_counter,
                vehicle_identifier=i + 1,
                start=row.pop(0),
                end=row.pop(0),
                duration=row.pop(0),
                address=row.pop(0),
            )

            vehicle.add_service(service)
            services.append(service)
            service_counter += 1

        availabilities_count = row.pop(0)
        for j in range(0, availabilities_count):
            vehicle.add_availability(AvailabilityDTO(
                identifier=availability_counter,
                vehicle_identifier=i,
                start=row.pop(0),
                end=row.pop(0),
                address=row.pop(0),
            ))
            availability_counter += 1

        vehicles.append(vehicle)

    for i in range(1, len(services)):
        services.append(ServiceDTO(
            identifier=len(services),
            vehicle_identifier=services[i].vehicle_identifier
        ))

    return vehicles, services, service_counter - 1
