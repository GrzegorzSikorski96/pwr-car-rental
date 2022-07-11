from django.test import TestCase

from car.forms.CarForm import CarForm


class CarFormTestCase(TestCase):
    def test_should_pass_when_all_data_is_correct(self):
        data = {
            'manufacturer': 'Manufacturer',
            'model': 'Model',
            'mileage': 1233,
            'production_date': '2022-01-01',
            'air_conditioning': 'true',
            'transmission_type': 'automatic',
            'body_type': 'coupe',
            'drivetrain_type': 'all wheel drive',
            'seats': 3,
            'trunk_volume': 2,
            'volume': 1292,
            'horsepower': 123,
            'fuel_type': 'diesel',
            'service_mileage_interval': 15000,
            'insured_date': '2022-02-1',
            'technical_overview_date': '2022-02-1',
            'registration_number': 'DW 123',
            'daily': 30,
            'weekly': 900,
            'monthly': 2800,
        }

        form = CarForm(data=data)

        self.assertTrue(form.is_valid())

    def test_air_conditioning_should_return_boolean_true_when_is_true(self):
        data = {
            'manufacturer': 'Manufacturer',
            'model': 'Model',
            'mileage': 1233,
            'production_date': '2022-01-01',
            'air_conditioning': 'true',
            'transmission_type': 'manual',
            'body_type': 'coupe',
            'drivetrain_type': 'all wheel drive',
            'seats': 3,
            'trunk_volume': 2,
            'volume': 1292,
            'horsepower': 123,
            'fuel_type': 'diesel',
            'service_mileage_interval': 15000,
            'insured_date': '2022-02-1',
            'technical_overview_date': '2022-02-1',
            'registration_number': 'DW 123',
            'daily': 30,
            'weekly': 900,
            'monthly': 2800,
        }

        form = CarForm(data=data)

        self.assertTrue(form.is_valid())
        self.assertTrue(form.cleaned_data['air_conditioning'])

    def test_air_conditioning_should_return_boolean_false_when_is_true(self):
        data = {
            'manufacturer': 'Manufacturer',
            'model': 'Model',
            'mileage': 1233,
            'production_date': '2022-01-01',
            'air_conditioning': 'false',
            'transmission_type': 'automatic',
            'body_type': 'coupe',
            'drivetrain_type': 'all wheel drive',
            'seats': 3,
            'trunk_volume': 2,
            'volume': 1292,
            'horsepower': 123,
            'fuel_type': 'diesel',
            'service_mileage_interval': 15000,
            'insured_date': '2022-02-1',
            'technical_overview_date': '2022-02-1',
            'registration_number': 'DW 123',
            'daily': 30,
            'weekly': 900,
            'monthly': 2800,
        }

        form = CarForm(data=data)

        self.assertTrue(form.is_valid())
        self.assertFalse(form.cleaned_data['air_conditioning'])

    def test_registration_number_should_be_stripped_and_uppercase(self):
        data = {
            'manufacturer': 'Manufacturer',
            'model': 'Model',
            'mileage': 1233,
            'production_date': '2022-01-01',
            'air_conditioning': 'false',
            'transmission_type': 'automatic',
            'body_type': 'coupe',
            'drivetrain_type': 'all wheel drive',
            'seats': 3,
            'trunk_volume': 2,
            'volume': 1292,
            'horsepower': 123,
            'fuel_type': 'diesel',
            'service_mileage_interval': 15000,
            'insured_date': '2022-02-1',
            'technical_overview_date': '2022-02-1',
            'registration_number': 'dw 123',
            'daily': 30,
            'weekly': 900,
            'monthly': 2800,
        }

        form = CarForm(data=data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['registration_number'], 'DW 123')

    def test_should_return_errors_when_data_is_not_correct(self):
        data = {
            'manufacturer': 'Manufacturer',
            'model': 'Model',
            'mileage': 1233,
            'production_date': '2022-01-01',
            'air_conditioning': 'asd',
            'transmission_type': 'automatic',
            'body_type': 'coupe',
            'drivetrain_type': 'all wheel drive',
            'seats': 3,
            'trunk_volume': 2,
            'volume': 1292,
            'horsepower': 123,
            'fuel_type': 'diesel',
            'service_mileage_interval': 15000,
            'insured_date': 'date',
            'technical_overview_date': 'date',
            'registration_number': '',
            'daily': 30,
            'weekly': 900,
            'monthly': 2800,
        }

        form = CarForm(data=data)

        expected_errors = {
            'registration_number': ['This field is required.'],
            'air_conditioning': ['Select a valid choice. asd is not one of the available choices.'],
            'insured_date': ['Enter a valid date.'],
            'technical_overview_date': ['Enter a valid date.'],
        }

        self.assertFalse(form.is_valid())
        self.assertEqual(expected_errors, form.errors)
