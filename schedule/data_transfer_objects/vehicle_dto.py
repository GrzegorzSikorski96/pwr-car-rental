from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from schedule.data_transfer_objects.availability_dto import AvailabilityDTO
    from schedule.data_transfer_objects.service_dto import ServiceDTO


class VehicleDTO:
    def __init__(
            self,
            identifier: int,
    ):
        self.identifier = identifier
        self.services: List['ServiceDTO'] = []
        self.availabilities: List['AvailabilityDTO'] = []

    def add_availability(self, availability: 'AvailabilityDTO') -> None:
        self.availabilities.append(availability)

    def add_service(self, service: 'ServiceDTO') -> None:
        self.services.append(service)

    def find_available_time_range_forward(self, total_time: int, from_address: int, distances: list[list[int]]):
        found: bool = False
        old_address: int = 0

        for availability in self.availabilities:
            temporary_time: int = total_time + distances[from_address][availability.address]

            if temporary_time < availability.start:
                temporary_time = availability.start

            if temporary_time <= availability.end:
                total_time = temporary_time
                old_address = availability.address
                found = True
                break

        return found, total_time, old_address

    def find_available_time_range_backward(self, total_time: int, from_address: int, distances: list[list[int]]):
        found: bool = False
        old_address: int = 0

        for availability in reversed(self.availabilities):
            temporary_time: int = total_time - distances[availability.address][from_address]

            if temporary_time > availability.end:
                temporary_time = availability.end

            if temporary_time >= availability.start:
                total_time = temporary_time
                old_address = availability.address
                found = True
                break

        return found, total_time, old_address
