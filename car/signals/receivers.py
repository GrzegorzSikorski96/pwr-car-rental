from django.db.models.signals import post_save
from django.dispatch import receiver

from car.choices.car_status_choices import CarStatus
from car.models import Car, ScheduleService


@receiver(post_save, sender=Car)
def execute_after_save(sender: Car, instance: Car, created, *args, **kwargs):
    if not created:
        if instance.status == CarStatus.NEED_SERVICE_STATUS:
            service: 'ScheduleService' = ScheduleService()
            service.car = instance
            service.save()
