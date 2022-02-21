from django.db import models
from django.utils.timezone import now


class Rent(models.Model):
    rented_by = models.ForeignKey(
        'core.User',
        on_delete=models.DO_NOTHING,
        related_name='rents'
    )
    rented_at = models.DateTimeField(default=now)
    rented_to = models.DateTimeField(
        null=True
    )
    rented_car = models.OneToOneField(
        'car.Car',
        on_delete=models.DO_NOTHING,
        related_name='rent',
    )


class Pricing(models.Model):
    daily = models.PositiveIntegerField()
    weekly = models.PositiveIntegerField()
    monthly = models.PositiveIntegerField()
