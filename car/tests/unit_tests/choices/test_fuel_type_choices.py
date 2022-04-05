from typing import List

from django.test import TestCase

from car.choices.fuel_type_choices import FuelType


class FuelTypeChoicesTestCase(TestCase):
    def test_should_return_choices_as_list(self):
        fuel_type_choices = FuelType.FUEL_TYPES_CHOICES

        self.assertEqual(3, len(fuel_type_choices))
        self.assertIsInstance(fuel_type_choices, List)

        for fuel_type in fuel_type_choices:
            self.assertIsInstance(fuel_type, tuple)
            self.assertIsInstance(fuel_type[0], str)
            self.assertIsInstance(fuel_type[1], str)
            self.assertEqual(fuel_type[0], fuel_type[1].lower())
