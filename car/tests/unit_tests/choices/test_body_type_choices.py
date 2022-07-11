from typing import List

from django.test import TestCase

from car.choices.body_type_choices import BodyType


class BodyTypeChoicesTestCase(TestCase):
    def test_should_return_choices_as_list(self):
        body_type_choices = BodyType.BODY_TYPE_CHOICES

        self.assertEqual(12, len(body_type_choices))
        self.assertIsInstance(body_type_choices, List)

        for choice in body_type_choices:
            self.assertIsInstance(choice, tuple)
            self.assertIsInstance(choice[0], str)
            self.assertIsInstance(choice[1], str)
            self.assertEqual(choice[0], choice[1].lower())
