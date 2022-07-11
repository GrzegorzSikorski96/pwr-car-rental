from typing import List

from django.test import TestCase

from car.choices.drivetrain_type_choices import DrivetrainType


class DrivetrainTypeChoicesTestCase(TestCase):
    def test_should_return_choices_as_list(self):
        drivetrain_type_choices = DrivetrainType.DRIVETRAIN_TYPE_CHOICES

        self.assertEqual(4, len(drivetrain_type_choices))
        self.assertIsInstance(drivetrain_type_choices, List)

        for drivetrain in drivetrain_type_choices:
            self.assertIsInstance(drivetrain, tuple)
            self.assertIsInstance(drivetrain[0], str)
            self.assertIsInstance(drivetrain[1], str)
            self.assertEqual(drivetrain[0], drivetrain[1].lower())
