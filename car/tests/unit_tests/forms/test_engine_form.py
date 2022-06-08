from django.test import TestCase

from car.forms.EngineForm import EngineForm


class EngineFormTestCase(TestCase):
    def test_should_pass_when_all_data_is_correct(self):
        data = {
            'volume': 1292,
            'horsepower': 123,
            'fuel_type': 'diesel',
        }

        form = EngineForm(data=data)

        self.assertTrue(form.is_valid())
