from django.db import models

from car_rental import settings
from core.models_mixins.TimeStampMixin import TimeStampMixin


class CarLog(models.Model):
    class Meta:
        ordering = ['-created_at']

    car = models.ForeignKey(
        'car.Car',
        on_delete=models.DO_NOTHING,
        related_name='logs'
    )
    mileage = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def difference_to_previous_day(self):
        prev_log: CarLog = CarLog.objects \
            .filter(car=self.car, id__lt=self.id) \
            .exclude(id=self.id) \
            .order_by('-id').first()

        if prev_log:
            return self.mileage - prev_log.mileage

        return 0


class ServiceLog(TimeStampMixin):
    class Meta:
        ordering = ['-created_at']

    car = models.ForeignKey(
        'car.Car',
        on_delete=models.DO_NOTHING,
        related_name='services'
    )
    action = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    mileage = models.IntegerField()
    next_service_mileage = models.IntegerField(null=True)
    next_service_date = models.DateField(null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='service_log'
    )
