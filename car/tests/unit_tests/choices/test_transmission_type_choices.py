from typing import List

from django.test import TestCase

from car.choices.transmission_type_choices import TransmissionType


class FuelTypeChoicesTestCase(TestCase):
    def test_should_return_choices_as_list(self):
        transmission_type = TransmissionType.TRANSMISSION_TYPE_CHOICES

        self.assertEqual(2, len(transmission_type))
        self.assertIsInstance(transmission_type, List)

        for transmission_type in transmission_type:
            self.assertIsInstance(transmission_type, tuple)
            self.assertIsInstance(transmission_type[0], str)
            self.assertIsInstance(transmission_type[1], str)
            self.assertEqual(transmission_type[0], transmission_type[1].lower())
