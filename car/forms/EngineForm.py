from django import forms
from django.forms import ModelForm

from car.choices.fuel_type_choices import FuelType
from car.models import Engine


class EngineForm(ModelForm):
    engine_volume = forms.IntegerField(
        label='Engine volume',
        widget=forms.NumberInput(attrs={'placeholder': 'Volume...', 'class': 'form-control'})
    )
    horsepower = forms.CharField(
        label='Engine horsepower',
        widget=forms.TextInput(attrs={'placeholder': 'Horsepower...', 'class': 'form-control'})
    )
    fuel_type = forms.ChoiceField(
        label='Engine fuel type',
        choices=FuelType.FUEL_TYPES_CHOICES,
        widget=forms.Select(attrs={'placeholder': 'Horsepower...', 'class': 'form-control'})
    )

    class Meta:
        model = Engine
        fields = [
            'volume',
            'horsepower',
            'fuel_type',
        ]

    def __init__(self, *args, **kwargs):
        super(EngineForm, self).__init__(*args, **kwargs)
        self.fields['engine_volume'].widget.attrs['class'] = 'form-control'
        self.fields['engine_volume'].widget.attrs['placeholder'] = 'Volume...'

        self.fields['horsepower'].widget.attrs['class'] = 'form-control'
        self.fields['horsepower'].widget.attrs['placeholder'] = 'Horsepower...'

        self.fields['fuel_type'].widget.attrs['class'] = 'form-control'
        self.fields['fuel_type'].widget.attrs['placeholder'] = 'Fuel type...'
