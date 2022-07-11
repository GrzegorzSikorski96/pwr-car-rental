import datetime

from django import forms
from django.db.models import Q
from django.forms import ModelForm

from car.choices.car_status_choices import CarStatus
from car.models import Car
from core.models import User
from rent.models import Rent


class RentForm(ModelForm):
    rented_at = forms.DateField(
        label='Rented at',
        initial=datetime.date.today(),
        widget=forms.DateInput(attrs={'placeholder': 'Rented at...', 'class': 'form-control', 'type': 'date'})
    )
    rented_to = forms.DateField(
        label='Rented to',
        initial=datetime.date.today(),
        widget=forms.DateInput(attrs={'placeholder': 'Rented to...', 'class': 'form-control', 'type': 'date'})
    )
    rented_by = forms.ModelChoiceField(
        label='Rented by',
        queryset=User.objects.filter(groups__name='client'),
        widget=forms.Select(attrs={'placeholder': 'Production date...', 'class': 'form-control'})
    )
    rented_car = forms.ModelChoiceField(
        label='Rented car',
        queryset=None,
        widget=forms.Select(attrs={'placeholder': 'Rented car...', 'class': 'form-control'})
    )

    class Meta:
        model = Rent
        fields = [
            'rented_at',
            'rented_to',
            'rented_by',
            'rented_car',
        ]

    def __init__(self, *args, **kwargs):
        super(RentForm, self).__init__(*args, **kwargs)

        if hasattr(self.instance, 'rented_car'):
            self.fields['rented_car'].queryset = Car.objects.filter(
                Q(status=CarStatus.READY_TO_RENT_STATUS) | Q(id=self.instance.rented_car.id))
        else:
            self.fields['rented_car'].queryset = Car.objects.filter(status=CarStatus.READY_TO_RENT_STATUS)
