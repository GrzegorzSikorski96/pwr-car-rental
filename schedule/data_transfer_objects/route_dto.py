class RouteDTO:
    def __init__(self):
        self.services: list[int] = []
        self.work_time: int = 0
        self.trace: list[int] = []
        self.S: list[int] = [0]
        self.C: list[int] = [0]
        self.addresses: list[int] = []

    def __str__(self):
        return '%s %s %s' % (
            str(self.work_time),
            ' '.join([str(operation) for operation in self.trace]),
            ' '.join([str(time) for time in self.__S_C_to_times()]),
        )

    def operations(self):
        return self.services_to_operations_list(self.services)

    @classmethod
    def services_to_operations_list(cls, services: list[int]):
        return [0] + services + [0]

    def __S_C_to_times(self):
        times = [self.S[0]]

        for i in range(1, len(self.S)):
            times.append(self.S[i])
            times.append(self.C[i])

        times.append(self.C[0])

        return times
