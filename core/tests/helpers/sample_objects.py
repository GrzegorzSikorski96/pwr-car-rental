from typing import Optional, List

from django.contrib.auth import get_user_model

from core.models import Address, User


def sample_user(groups: Optional[List[int]] = None, **kwargs) -> User:
    defaults = {
        'email': 'username@example.com',
        'password': 'password',
        'first_name': 'first_vendor',
        'last_name': 'last_manager',
        'phone_number': 'last_manager',
        'is_superuser': True,
    }
    defaults.update(kwargs)

    user = get_user_model().objects.create_user(**defaults)

    if groups:
        user.groups.set(groups)

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
