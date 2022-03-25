import datetime

from django import forms

from car.choices.body_type_choices import BodyType
from core.choices.boolean_choices import BooleanChoices
from car.choices.drivetrain_type_choices import DrivetrainType
from car.choices.transmission_type_choices import TransmissionType
from car.forms.EngineForm import EngineForm
from car.forms.ServicingForm import ServicingForm
from car.models import Car
from rent.forms.PricingForm import PricingForm


class CarForm(EngineForm, PricingForm, ServicingForm):
    manufacturer = forms.CharField(
        label='Manufacturer',
        widget=forms.TextInput(attrs={'placeholder': 'Manufacturer...', 'class': 'form-control'})
    )
    model = forms.CharField(
        label='Model',
        widget=forms.TextInput(attrs={'placeholder': 'Model...', 'class': 'form-control'})
    )
    mileage = forms.IntegerField(
        label='Mileage',
        widget=forms.NumberInput(attrs={'placeholder': 'Mileage...', 'class': 'form-control'})
    )
    registration_number = forms.CharField(
        label='Registration number',
        widget=forms.TextInput(attrs={'placeholder': 'Mileage...', 'class': 'form-control'})
    )
    production_date = forms.DateField(
        label='Production date',
        initial=datetime.date.today(),
        widget=forms.DateInput(attrs={'placeholder': 'Production date...', 'class': 'form-control', 'type': 'date'})
    )
    air_conditioning = forms.ChoiceField(
        choices=BooleanChoices.BooleanChoices,
        label='Air conditioning',
        widget=forms.Select(attrs={'placeholder': 'Air conditioning...', 'class': 'form-control'})
    )
    transmission_type = forms.ChoiceField(
        choices=TransmissionType.TRANSMISSION_TYPE_CHOICES,
        label='Transmission type',
        widget=forms.Select(attrs={'placeholder': 'Transmission type...', 'class': 'form-control'})
    )
    body_type = forms.ChoiceField(
        choices=BodyType.BODY_TYPE_CHOICES,
        label='Body type',
        widget=forms.Select(attrs={'placeholder': 'Body type...', 'class': 'form-control'})
    )
    drivetrain_type = forms.ChoiceField(
        choices=DrivetrainType.DRIVETRAIN_TYPE_CHOICES,
        label='Drivetrain type',
        widget=forms.Select(attrs={'placeholder': 'Drivetrain type...', 'class': 'form-control'})
    )
    seats = forms.IntegerField(
        label='Seats',
        widget=forms.NumberInput(attrs={'placeholder': 'Seats...', 'class': 'form-control'})
    )
    trunk_volume = forms.IntegerField(
        label='Trunk volume (luggage)',
        widget=forms.NumberInput(attrs={'placeholder': 'Trunk volume...', 'class': 'form-control'})
    )

    class Meta:
        model = Car
        fields = [
            'manufacturer',
            'model',
            'mileage',
            'production_date',
            'air_conditioning',
            'transmission_type',
            'body_type',
            'drivetrain_type',
            'seats',
            'trunk_volume',
        ]
