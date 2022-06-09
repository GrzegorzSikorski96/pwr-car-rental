import datetime

from schedule.data_transfer_objects.service_dto import ServiceDTO
from schedule.data_transfer_objects.vehicle_dto import VehicleDTO
from schedule.helpers.consts import LOAD_UNLOAD_TIME, FUZE_VALUE


def day_of_year_from_datetime(date_string: str) -> int:
    return datetime.datetime.strptime(date_string, "%Y-%m-%d").timetuple().tm_yday


def minutes_between_date_times(start: str, end: str) -> int:
    start_datetime = datetime.datetime.strptime(start, "%Y-%m-%d")
    end_datetime = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")

    diff = end_datetime - start_datetime

    return int(diff.total_seconds() / 60)


def add_minutes_to_date_time(start: 'datetime.datetime', minutes: int):
    return start + datetime.timedelta(minutes=minutes)


def work_time(trace: list[int], distances: list[list[int]], vehicles: list['VehicleDTO'], services: list['ServiceDTO'],
              services_count: int) -> tuple[int, list[int], list[int], list[int]]:
    time: int = 0
    old_address: int = 0
    S: list[int] = [0]
    C: list[int] = [0]
    addresses: list[int] = []

    for current_action, next_action in zip(trace, trace[1:]):
        from_address: int = 0

        if current_action == 0:
            from_address = 0
            addresses.append(0)

        if 1 <= current_action <= services_count:
            from_address = services[current_action].address  # type: ignore
            addresses.append(from_address)

        if current_action >= services_count + 1:
            from_address = old_address
            addresses.append(from_address)

        if next_action == 0:
            to_address = 0
            time += distances[from_address][to_address]
            C[0] = time
            addresses.append(0)

        if 1 <= next_action <= services_count:
            to_address = services[next_action].address  # type: ignore
            time += distances[from_address][to_address]
            S.append(time)
            time += LOAD_UNLOAD_TIME
            C.append(time)

        if next_action >= services_count + 1:
            found, time, old_address = vehicles[services[next_action].vehicle_identifier]. \
                find_available_time_range_forward(time, from_address, distances)
            S.append(time)
            time += LOAD_UNLOAD_TIME
            C.append(time)

            if not found:
                return FUZE_VALUE, S, C, addresses

    time, S, C, addresses = work_time_phase2(trace, S, C, distances, vehicles, services, services_count, addresses)

    return C[0] - S[0], S, C, addresses


def work_time_phase2(trace: list[int], S: list[int], C: list[int], distances: list[list[int]],
                     vehicles: list['VehicleDTO'], services: list['ServiceDTO'], services_count: int,
                     addresses: list[int]) -> tuple[int, list[int], list[int], list[int]]:
    time: int = C[0]
    old_address: int = 0
    for i in range(len(trace) - 2, -1, -1):
        from_address: int = 0
        current_action: int = trace[i]
        next_action: int = trace[i + 1]

        if next_action == 0:
            from_address = 0

        if 1 <= next_action <= services_count:
            from_address = services[next_action].address  # type: ignore

        if next_action >= services_count + 1:
            from_address = old_address

        if current_action == 0:
            to_address = 0
            time -= (distances[to_address][from_address])
            S[0] = time

        if 1 <= current_action <= services_count:
            to_address = services[current_action].address  # type: ignore
            time -= distances[to_address][from_address]
            C[i] = time
            time -= LOAD_UNLOAD_TIME
            S[i] = time

        if current_action >= services_count + 1:
            found, time, old_address = vehicles[
                services[current_action].vehicle_identifier]. \
                find_available_time_range_backward(time, from_address, distances)
            C[i] = time
            time -= LOAD_UNLOAD_TIME
            S[i] = time

    return C[0] - S[0], S, C, addresses
