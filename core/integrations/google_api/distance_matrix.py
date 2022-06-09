from __future__ import division
from __future__ import print_function

import json
import requests

from typing import List

from django.conf import settings
from django.db.models import QuerySet

from core.models import Address


class DistanceMatrix:
    def __init__(self):
        self.addresses: List[Address] = list(Address.objects.none())

        self.distance_matrix: List[List[int]] = []
        self.address_to_index_map: List[Address] = []

    def set_addresses(self, addresses: QuerySet[Address]):
        self.addresses = list(addresses)
        self.distance_matrix = self.get_distance_matrix()
        self.__map_addresses_to_index()

    def __map_addresses_to_index(self):
        for address in self.addresses:
            self.address_to_index_map.append(address)

    def __create_distance_matrix(self):
        api_key = settings.GOOGLE_API_KEY
        max_elements = 100
        num_addresses = len(self.addresses)
        max_rows = max_elements // num_addresses
        q, r = divmod(num_addresses, max_rows)
        dest_addresses = self.addresses
        distance_matrix = []

        for i in range(q):
            origin_addresses = self.addresses[i * max_rows: (i + 1) * max_rows]
            response = self.__send_request(origin_addresses, dest_addresses, api_key)
            distance_matrix += self.__build_distance_matrix(response)

        if r > 0:
            origin_addresses = self.addresses[q * max_rows: q * max_rows + r]
            response = self.__send_request(origin_addresses, dest_addresses, api_key)
            distance_matrix += self.__build_distance_matrix(response)
        return distance_matrix

    def __send_request(self, origin_addresses, dest_addresses, api_key):
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'
        origin_address_str = self.__build_address_str(origin_addresses)
        dest_address_str = self.__build_address_str(dest_addresses)
        url += '&origins=' + origin_address_str + '&destinations=' + dest_address_str + '&key=' + api_key

        response = requests.get(url)

        return json.loads(response.content)

    def __build_address_str(self, addresses):
        address_str = ''

        for i in range(len(addresses) - 1):
            address_str += addresses[i].__str__() + '|'

        address_str += addresses[-1].__str__()

        return address_str

    def __build_distance_matrix(self, response):
        distance_matrix = []
        for row in response['rows']:
            row_list = [row['elements'][j]['distance']['value'] for j in range(len(row['elements']))]
            distance_matrix.append(row_list)
        return distance_matrix

    def get_distance_matrix(self):
        matrix = self.__create_distance_matrix()

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                matrix[i][j] = int(matrix[i][j]/1000)

        return matrix
