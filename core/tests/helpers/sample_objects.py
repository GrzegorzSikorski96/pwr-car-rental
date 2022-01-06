from django.contrib.auth import get_user_model

from core.models import Address, Contact, User


def sample_user(**kwargs) -> User:
    defaults = {
        'email': 'username@example.com',
        'password': 'password',
        'first_name': 'first_vendor',
        'last_name': 'last_manager',
        'is_superuser': True,
        'address_id': sample_address().id,
    }
    defaults.update(kwargs)

    user = get_user_model().objects.create_user(**defaults)

    return user


def sample_address(**kwargs) -> Address:
    defaults = {
        'country': 'Poland',
        'city': 'Wrocław',
        'postal_code': '51-661',
        'street': 'Legnicka',
        'number': '13A',
    }
    defaults.update(kwargs)

    return Address.objects.create(**defaults)


def sample_contact(**kwargs) -> Contact:
    defaults = {
        'value': 'example@example.com',
        'type': 'email',
    }
    defaults.update(kwargs)

    return Contact.objects.create(**defaults)
