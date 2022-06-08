import datetime

from django import forms
from django.forms import ModelForm
from django.utils.dateparse import parse_datetime
from django.utils.datetime_safe import strftime
from django.utils.encoding import force_str

from car.choices.fuel_type_choices import FuelType
from car.forms.CarAvailabilityAddressForm import CarAvailabilityAddressForm
from car.models import Engine, Car, Availability
from core.models import Address, UserCarPickupAddress


class CarAvailabilityForm(ModelForm):
    start = forms.DateTimeField(
        label='Start',
        initial=datetime.date.today(),
        localize=True,
        widget=forms.DateTimeInput(attrs={'placeholder': 'Start...', 'class': 'form-control', 'type': 'datetime-local'}, format="%Y-%m-%dT%H:%M")
    )
    end = forms.DateTimeField(
        label='End',
        initial=datetime.date.today(),
        localize=True,
        widget=forms.DateTimeInput(attrs={'placeholder': 'End...', 'class': 'form-control', 'type': 'datetime-local'}, format="%Y-%m-%dT%H:%M")
    )
    car = forms.ModelChoiceField(
        label='Car',
        queryset=Car.objects.all(),
        disabled=True,
        widget=forms.Select(attrs={'placeholder': 'Car...', 'class': 'form-control'})
    )
    address = forms.ModelChoiceField(
        label='Address',
        queryset=UserCarPickupAddress.objects.filter(id=None),
        widget=forms.Select(attrs={'placeholder': 'Address...', 'class': 'form-control'})
    )

    class Meta:
        model = Availability
        fields = [
            'start',
            'end',
            'car',
            'address'
        ]

    def __init__(self, user, car, *args, **kwargs):
        super(CarAvailabilityForm, self).__init__(*args, **kwargs)

        self.fields['car'].queryset = Car.objects.get_query(user=user)
        self.fields['car'].initial = Car.objects.get_query(user=user).get(id=car.id)
        self.fields['address'].queryset = UserCarPickupAddress.objects.filter(user=user)
