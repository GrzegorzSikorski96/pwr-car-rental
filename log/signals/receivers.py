from django.db.models.signals import post_save
from django.dispatch import receiver

from car.choices.car_status_choices import CarStatus
from log.models import CarLog


@receiver(post_save, sender=CarLog)
def execute_after_save(sender: CarLog, instance: CarLog, created, *args, **kwargs):
    if created:
        car = instance.car
        car.mileage = instance.mileage

        if 1000 > car.kilometers_to_service() or 30 > car.days_to_service():
            car.status = CarStatus.NEED_SERVICE_STATUS

        car.save()
