from django.db import models
from django.utils.timezone import now

from car.choices.car_status_choices import CarStatus


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

    def save(self, *args, **kwargs) -> None:
        create = False if self.pk else True
        super(Rent, self).save(*args, **kwargs)

        if create:
            self.rented_car.status = CarStatus.RENTED_STATUS
            self.rented_car.save()


class Pricing(models.Model):
    daily = models.PositiveIntegerField()
    weekly = models.PositiveIntegerField()
    monthly = models.PositiveIntegerField()
