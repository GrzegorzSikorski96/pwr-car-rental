from typing import Optional


class ServiceDTO:
    def __init__(
            self,
            identifier: int = 0,
            vehicle_identifier: int = 0,
            start: Optional[int] = None,
            end: Optional[int] = None,
            duration: Optional[int] = None,
            address: Optional[int] = None,
    ):
        self.identifier = identifier
        self.vehicle_identifier = vehicle_identifier
        self.start = start
        self.end = end
        self.duration = duration
        self.address = address
