from django import forms
from django.forms import ModelForm

from car.choices.fuel_type_choices import FuelType
from car.models import Engine


class EngineCreateForm(ModelForm):
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
        super(EngineCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label + '...'
