from django.contrib.auth import get_user_model

from car.tests.helpers.sample_objects import sample_car
from log.models import CarLog, ServiceLog, MessageLog


def sample_car_log(**kwargs) -> CarLog:
    defaults = {
        'mileage': 156000,
        'created_at': '2022-12-2',
    }

    if not kwargs.get('car', None):
        defaults.update({'car': sample_car()})

    defaults.update(kwargs)

    return CarLog.objects.create(**defaults)


def sample_service_log(**kwargs) -> ServiceLog:
    defaults = {
        'action': 'sample_action',
        'description': 'sample_description',
        'mileage': 150000,
        'next_service_mileage': 160000,
        'next_service_date': '2023-01-03',
        'created_by': 'username@example.com',
        'created_at': '2022-01-02',
    }

    if not kwargs.get('car', None):
        defaults.update({'car': sample_car()})

    defaults['created_by'] = get_user_model().objects.get(email=defaults['created_by'])

    defaults.update(kwargs)

    return ServiceLog.objects.create(**defaults)


def sample_message_log(**kwargs) -> MessageLog:
    defaults = {
        'action': 'sample_action',
        'message': 'sample_message',
        'created_by': 'username@example.com',
    }

    if not kwargs.get('car', None):
        defaults.update({'car': sample_car()})

    defaults['created_by'] = get_user_model().objects.get(email=defaults['created_by'])

    defaults.update(kwargs)

    return MessageLog.objects.create(**defaults)
