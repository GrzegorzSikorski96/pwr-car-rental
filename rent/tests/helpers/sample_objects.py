from datetime import datetime

from rent.models import Pricing, Rent


def sample_pricing(**kwargs) -> Pricing:
    defaults = {
        'daily': 30,
        'weekly': 900,
        'monthly': 2800,
    }

    defaults.update(kwargs)

    return Pricing.objects.create(**defaults)


def sample_rent(**kwargs) -> Rent:
    defaults = {
        'rented_by': 1,
        'rented_at': datetime(2021, 1, 1).astimezone(),
        'rented_to': datetime(2022, 2, 3).astimezone(),
        'rented_car': 1,
    }

    defaults.update(kwargs)

    return Rent.objects.create(**defaults)
