from django import forms
from django.forms import ModelForm

from car.models import Servicing


class ServicingForm(ModelForm):
    service_mileage_interval = forms.IntegerField(
        label='Service mileage interval',
        widget=forms.NumberInput(attrs={'placeholder': 'Service mileage interval...', 'class': 'form-control'})
    )
    insured_date = forms.DateField(
        label='Insured date (mm/dd/yyyy)',
        widget=forms.DateInput(attrs={'placeholder': 'Insured date...', 'class': 'form-control', 'type': 'date'})
    )
    technical_overview_date = forms.DateField(
        label='Technical overview date (mm/dd/yyyy)',
        widget=forms.DateInput(
            attrs={'placeholder': 'Technical overview date...', 'class': 'form-control', 'type': 'date'})
    )

    class Meta:
        model = Servicing
        fields = [
            'service_mileage_interval',
            'insured_date',
            'technical_overview_date',
        ]

    def __init__(self, *args, **kwargs):
        super(ServicingForm, self).__init__(*args, **kwargs)
