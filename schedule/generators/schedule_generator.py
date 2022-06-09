import random
from typing import List

from schedule.data_transfer_objects.route_dto import RouteDTO
from schedule.data_transfer_objects.service_dto import ServiceDTO
from schedule.data_transfer_objects.vehicle_dto import VehicleDTO
from schedule.generators.data import load_data
from schedule.helpers.consts import FUZE_VALUE, MAX_LOAD_CAPACITY
from schedule.helpers.time import work_time


class ScheduleGenerator:
    def __int__(self, vehicles: List['VehicleDTO'], services: List['ServiceDTO'], services_count: int,
                distances: List[List[int]]):
        self.vehicles = vehicles
        self.services = services
        self.services_count = services_count
        self.distances = distances

    def permute_trace(self, trace: list[int], operations_count: int, position: int, services_count: int,
                      permutations: list) -> list[list[int]]:
        if position == 1:
            ps: list[int] = [0] * (2 * services_count + 1)

            for i in range(1, operations_count + 1):
                ps[trace[i]] = i

            for i in range(1, operations_count + 1):
                if trace[i] <= services_count and ps[trace[i]] < ps[trace[i] + services_count]:
                    return permutations

            permutations.append(list(trace))

            return permutations

        for i in range(position, 0, -1):
            trace[i], trace[position] = trace[position], trace[i]

            permutations = self.permute_trace(trace, operations_count, position - 1, services_count, permutations)

            trace[i], trace[position] = trace[position], trace[i]

        return permutations

    def services_list_to_trace(self, services: list[int], services_count: int) -> list[int]:
        return [0] + [service + services_count for service in services] + services + [0]

    def optimize(self, route_services: list[int], distances: list[list[int]], vehicles: list['VehicleDTO'],
                 services: list['ServiceDTO'], services_count: int) -> list[int]:
        trace: list[int] = self.services_list_to_trace(route_services, services_count)

        trace_permutations: list[list[int]] = self.permute_trace(trace, 2 * len(route_services),
                                                                 2 * len(route_services), services_count, [])

        lowest_time: int = FUZE_VALUE
        for permutation in trace_permutations:
            permutation_time, _, _, _ = work_time(permutation, distances, vehicles, services, services_count)

            if permutation_time < lowest_time:
                lowest_time = permutation_time
                trace = permutation

        return trace

    def generate(self, data_string: str, distances: List[List[int]]):
        vehicles, services, services_count = load_data(data_string.splitlines())

        routes = self.generate_single_operation_routes(distances, vehicles, services, services_count)

        return self.optimize_orders_by_linking(routes, distances, vehicles, services, services_count)

    def generate_single_operation_routes(self, distances: list[list[int]], vehicles: list['VehicleDTO'],
                                         services: list['ServiceDTO'], services_count: int) -> list['RouteDTO']:
        operations: list[int] = RouteDTO.services_to_operations_list([1])
        routes: list['RouteDTO'] = []

        for i in range(1, services_count + 1):
            operations[1] = i

            route: 'RouteDTO' = RouteDTO()
            route.services.append(i)
            route.trace = self.optimize(route.services, distances, vehicles, services, services_count)
            route.work_time, route.S, route.C, route.addresses = work_time(route.trace, distances, vehicles, services,
                                                                           services_count)

            routes.append(route)

        return routes

    def optimize_orders_by_linking(self, orders: list['RouteDTO'], distances: list[list[int]],
                                   vehicles: list['VehicleDTO'], services: list['ServiceDTO'],
                                   services_count: int) -> list['RouteDTO']:
        optional_orders: list['RouteDTO'] = []

        while len(orders) > 0:
            for _ in range(1, MAX_LOAD_CAPACITY):
                linked_orders_costs: list[int] = [0]

                order: 'RouteDTO' = orders[0]
                for next_order in orders[1:]:
                    tmp_order: 'RouteDTO' = RouteDTO()
                    tmp_order.services = order.services + next_order.services
                    tmp_order.trace = self.optimize(tmp_order.services, distances, vehicles, services, services_count)
                    tmp_order.work_time, tmp_order.S, tmp_order.C, tmp_order.addresses = work_time(tmp_order.trace,
                                                                                                   distances, vehicles,
                                                                                                   services,
                                                                                                   services_count)

                    linked_orders_costs.append(tmp_order.work_time - (order.work_time + next_order.work_time))

                lowest_cost: int = min(linked_orders_costs)
                lowest_cost_route_index: int = linked_orders_costs.index(lowest_cost)

                if lowest_cost < 0:
                    order.services = order.services + orders[lowest_cost_route_index].services
                    order.trace = self.optimize(order.services, distances, vehicles, services, services_count)
                    order.work_time, order.S, order.C, order.addresses = work_time(order.trace, distances, vehicles,
                                                                                   services, services_count)
                    orders.pop(lowest_cost_route_index)

            optional_orders.append(orders.pop(0))

        return optional_orders

    def get_trace_random_operation(self, trace: List[int], services_count: int):
        index = random.randint(1, len(trace) - 2)

        if trace[index] <= services_count:
            trace_service_index = index
            trace_pickup_index = trace.index(trace[index] + services_count)
        else:
            trace_pickup_index = index
            trace_service_index = trace.index(trace[index] - services_count)

        return trace_service_index, trace[trace_service_index], trace_pickup_index, trace[trace_pickup_index]

    def get_random_route_indexes_pair(self, routes: list['RouteDTO']):
        first_route_index = random.randint(0, len(routes) - 1)
        second_route_index = first_route_index

        while second_route_index == first_route_index:
            second_route_index = random.randint(0, len(routes) - 1)

        return first_route_index, second_route_index
