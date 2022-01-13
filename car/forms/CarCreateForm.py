from django.forms import ModelForm

from car.forms.EngineCreateForm import EngineCreateForm
from car.models import Car


class CarCreateForm(EngineCreateForm):
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
            'daily_rent_price',
            'weekly_rent_price',
            'monthly_rent_price',
            'seats',
            'trunk_volume',
        ]

    def __init__(self, *args, **kwargs):
        super(CarCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label + '...'

