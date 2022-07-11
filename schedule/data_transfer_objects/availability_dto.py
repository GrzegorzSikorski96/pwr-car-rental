class AvailabilityDTO:
    def __init__(
            self,
            identifier: int,
            vehicle_identifier: int,
            start: int,
            end: int,
            address: int,
    ):
        self.identifier = identifier
        self.vehicle_identifier = vehicle_identifier
        self.start = start
        self.end = end
        self.address = address
