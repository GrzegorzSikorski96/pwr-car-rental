from rent.models import Pricing


def sample_pricing(**kwargs) -> Pricing:
    defaults = {
        'daily': 30,
        'weekly': 900,
        'monthly': 2800,
    }

    defaults.update(kwargs)

    return Pricing.objects.create(**defaults)
