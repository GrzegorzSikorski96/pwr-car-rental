import datetime

from django.db import models
from django.utils import timezone

from car.choices.body_type_choices import BodyType
from car.choices.drivetrain_type_choices import DrivetrainType
from car.choices.fuel_type_choices import FuelType
from car.choices.transmission_type_choices import TransmissionType
from car_rental import settings
from core.models_mixins.TimeStampMixin import TimeStampMixin
from log.models import ServiceLog


class Car(TimeStampMixin):
    manufacturer = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    mileage = models.PositiveIntegerField(default=1000)
    production_date = models.DateField()
    air_conditioning = models.BooleanField(default=False)
    transmission_type = models.CharField(max_length=15, choices=TransmissionType.TRANSMISSION_TYPE_CHOICES)
    body_type = models.CharField(max_length=20, choices=BodyType.BODY_TYPE_CHOICES)
    drivetrain_type = models.CharField(max_length=25, choices=DrivetrainType.DRIVETRAIN_TYPE_CHOICES)
    daily_rent_price = models.PositiveIntegerField()
    weekly_rent_price = models.PositiveIntegerField()
    monthly_rent_price = models.PositiveIntegerField()
    seats = models.PositiveIntegerField()
    trunk_volume = models.PositiveIntegerField()
    service_mileage_interval = models.PositiveIntegerField(default=15000)
    insured_date = models.DateField(default=timezone.now)
    technical_overview_date = models.DateField(default=timezone.now)
    engine = models.ForeignKey(
        'car.Engine',
        on_delete=models.DO_NOTHING,
        related_name='cars'
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='created_cars'
    )

    def save(self, *args, **kwargs) -> None:
        create = False if self.pk else True
        super(Car, self).save(*args, **kwargs)

        if create:
            ServiceLog.objects.create(
                car=self,
                action="Car added to rental system.",
                description="",
                mileage=self.mileage,
                next_service_mileage=self.mileage + self.service_mileage_interval,
                next_service_date=datetime.date(self.created_at.year + 1, self.created_at.month, self.created_at.day),
                created_by=self.created_by,
            )

    def delete(self, **kwargs):
        for service in self.services.all():
            service.delete()

        for log in self.logs.all():
            log.delete()

        if hasattr(self, 'rent'):
            self.rent.delete()

        super(Car, self).delete()

    def last_service(self):
        return self.services.first()

    def __str__(self):
        return "#%d - %s %s" % (self.pk, self.manufacturer, self.model)


class Engine(models.Model):
    volume = models.CharField(max_length=50, null=True)
    horsepower = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=20, choices=FuelType.FUEL_TYPES_CHOICES)

    def __str__(self):
        return "#%d - %s cc, %s hp, %s" % (self.pk, self.volume, self.horsepower, self.fuel_type)
