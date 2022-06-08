from django.test import TestCase

from car.forms.ServicingForm import ServicingForm


class ServicingFormTestCase(TestCase):
    def test_should_pass_when_all_data_is_correct(self):
        data = {
            'service_mileage_interval': 15000,
            'insured_date': "2022-02-2",
            'technical_overview_date': "2022-02-2"
        }

        form = ServicingForm(data=data)

        self.assertTrue(form.is_valid())

    def test_should_return_error_when_dates_provided_in_wrong_format(self):
        data = {
            'service_mileage_interval': 15000,
            'insured_date': "date",
            'technical_overview_date': "date"
        }

        form = ServicingForm(data=data)

        expected_error = {
            'insured_date': ['Enter a valid date.'],
            'technical_overview_date': ['Enter a valid date.'],
        }

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, expected_error)

    def test_should_pass_when_mileage_is_string(self):
        data = {
            'service_mileage_interval': '15000',
            'insured_date': "2022-02-2",
            'technical_overview_date': "2022-02-2"
        }

        form = ServicingForm(data=data)

        self.assertTrue(form.is_valid())
