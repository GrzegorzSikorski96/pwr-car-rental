from __future__ import division
from __future__ import print_function

import json
import urllib.request as url
from typing import List, TYPE_CHECKING

from django.conf import settings

if TYPE_CHECKING:
    from core.models import Address


class DistanceMatrix:
    def __init__(self, addresses: List['Address']):
        self.addresses: List[str] = [address.get_slugged_address() for address in addresses]

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

    def __send_request(self, origin_addresses, dest_addresses, API_key):
        request = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'
        origin_address_str = self.__build_address_str(origin_addresses)
        dest_address_str = self.__build_address_str(dest_addresses)
        request = request + '&origins=' + origin_address_str + '&destinations=' + dest_address_str + '&key=' + API_key
        json_result = url.urlopen(request).read()
        response = json.loads(json_result)

        return response

    def __build_address_str(self, addresses):
        address_str = ''

        for i in range(len(addresses) - 1):
            address_str += addresses[i] + '|'

        address_str += addresses[-1]

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
