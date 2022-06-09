from django.db.models import QuerySet, Q

from car.models import ScheduleService
from core.models import Address


class AddressesFromScheduledServicesExtractor:
    def extract(self, services: 'QuerySet[ScheduleService]') -> 'QuerySet[Address]':
        addresses = Address.objects.filter(
            Q(is_depot=True) |
            Q(scheduled_services__in=services) |
            Q(availabilities__service__in=services)
        ).distinct()

        return addresses
