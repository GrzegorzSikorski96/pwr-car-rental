from django.db import models

from car.choices.body_type_choices import BodyType
from car.choices.drive_type_choices import DriveType
from car.choices.fuel_type_choices import FuelType
from car.choices.transmission_type_choices import TransmissionType


class Car(models.Model):
    manufacturer = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    mileage = models.PositiveIntegerField(default=1000)
    production_date = models.DateField()
    air_conditioning = models.BooleanField(default=False)
    transmission_type = models.CharField(max_length=15, choices=TransmissionType.TRANSMISSION_TYPE_CHOICES)
    body_type = models.CharField(max_length=20, choices=BodyType.BODY_TYPE_CHOICES)
    drive_type = models.CharField(max_length=25, choices=DriveType.DRIVE_TYPE_CHOICES)
    daily_rent_price = models.PositiveIntegerField()
    weekly_rent_price = models.PositiveIntegerField()
    monthly_rent_price = models.PositiveIntegerField()
    seats = models.PositiveIntegerField()
    trunk_volume = models.PositiveIntegerField()
    engine = models.ForeignKey(
        'car.Engine',
        on_delete=models.DO_NOTHING,
        related_name='cars'
    )


class Engine(models.Model):
    volume = models.CharField(max_length=50, null=True)
    horsepower = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=20, choices=FuelType.FUEL_TYPES_CHOICES)
