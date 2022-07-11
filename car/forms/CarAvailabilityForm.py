import datetime

from django import forms
from django.forms import ModelForm

from car.models import Car, Availability
from core.models import Address


class CarAvailabilityForm(ModelForm):
    start = forms.DateTimeField(
        label='Start',
        initial=datetime.date.today(),
        localize=True,
        widget=forms.DateTimeInput(
            attrs={'placeholder': 'Start...', 'class': 'form-control', 'type': 'datetime-local'},
            format="%Y-%m-%dT%H:%M")
    )
    end = forms.DateTimeField(
        label='End',
        initial=datetime.date.today(),
        localize=True,
        widget=forms.DateTimeInput(attrs={'placeholder': 'End...', 'class': 'form-control', 'type': 'datetime-local'},
                                   format="%Y-%m-%dT%H:%M")
    )
    car = forms.ModelChoiceField(
        label='Car',
        queryset=Car.objects.all(),
        disabled=True,
        widget=forms.Select(attrs={'placeholder': 'Car...', 'class': 'form-control'})
    )
    address = forms.ModelChoiceField(
        label='Address',
        queryset=Address.objects.none(),
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

        self.fields['address'].queryset = Address.objects.filter(user=car.rent.rented_by)
