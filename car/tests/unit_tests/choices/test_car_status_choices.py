from typing import List

from django.test import TestCase

from car.choices.car_status_choices import CarStatus


class CarStatusChoicesTestCase(TestCase):
    def test_should_return_choices_as_list(self):
        car_status_choices = CarStatus.CAR_STATUS_CHOICES

        self.assertEqual(4, len(car_status_choices))
        self.assertIsInstance(car_status_choices, List)

        for status in car_status_choices:
            self.assertIsInstance(status, tuple)
            self.assertIsInstance(status[0], str)
            self.assertIsInstance(status[1], str)
            self.assertEqual(status[0], status[1].lower())
