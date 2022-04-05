from django.contrib.auth import get_user_model

from car.choices.body_type_choices import BodyType
from car.choices.drivetrain_type_choices import DrivetrainType
from car.choices.fuel_type_choices import FuelType
from car.choices.transmission_type_choices import TransmissionType
from car.models import Engine, Servicing, Car
from rent.tests.helpers.sample_objects import sample_pricing


def sample_engine(**kwargs) -> Engine:
    defaults = {
        'volume': 1292,
        'horsepower': 123,
        'fuel_type': FuelType.DIESEL,
    }

    defaults.update(kwargs)

    return Engine.objects.create(**defaults)


def sample_servicing(**kwargs) -> Servicing:
    defaults = {
        'service_mileage_interval': 15000,
        'insured_date': '2022-02-1',
        'technical_overview_date': '2022-02-1',
    }

    defaults.update(kwargs)

    return Servicing.objects.create(**defaults)


def sample_car(**kwargs) -> Car:
    defaults = {
        'manufacturer': 'Manufacturer',
        'model': 'Model',
        'mileage': 1500,
        'production_date': '2022-01-01',
        'air_conditioning': True,
        'transmission_type': TransmissionType.AUTOMATIC_TRANSMISSION,
        'body_type': BodyType.PICKUP_BODY_TYPE,
        'drivetrain_type': DrivetrainType.FOUR_WHEEL_DRIVETRAIN_TYPE,
        'seats': 3,
        'trunk_volume': 2,
        'registration_number': 'DW 123',
        'created_by': 'username@example.com'
    }

    defaults.update(kwargs)

    defaults['created_by'] = get_user_model().objects.get(email=defaults['created_by'])

    if not kwargs.get('engine', None):
        defaults.update({'engine': sample_engine()})

    if not kwargs.get('pricing', None):
        defaults.update({'pricing': sample_pricing()})

    if not kwargs.get('servicing', None):
        defaults.update({'servicing': sample_servicing()})

    return Car.objects.create(**defaults)
