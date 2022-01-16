import datetime

from car.forms.EngineForm import EngineForm
from car.models import Car


class CarForm(EngineForm):
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
            'service_mileage_interval',
            'insured_date',
            'technical_overview_date',
        ]

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['manufacturer'].widget.attrs['class'] = 'form-control'
        self.fields['manufacturer'].widget.attrs['placeholder'] = 'Manufacturer...'

        self.fields['model'].widget.attrs['class'] = 'form-control'
        self.fields['model'].widget.attrs['placeholder'] = 'Model...'

        self.fields['mileage'].widget.attrs['class'] = 'form-control'
        self.fields['mileage'].widget.attrs['placeholder'] = 'Mileage...'

        self.fields['production_date'].widget.attrs['class'] = 'form-control'
        self.fields['production_date'].widget.attrs['placeholder'] = 'Production date...'
        self.fields['production_date'].initial = datetime.date.today()

        self.fields['air_conditioning'].widget.attrs['class'] = 'form-control'
        self.fields['air_conditioning'].widget.attrs['placeholder'] = 'Air conditioning...'

        self.fields['transmission_type'].widget.attrs['class'] = 'form-control'
        self.fields['transmission_type'].widget.attrs['placeholder'] = 'Transmission type...'

        self.fields['body_type'].widget.attrs['class'] = 'form-control'
        self.fields['body_type'].widget.attrs['placeholder'] = 'Body type...'

        self.fields['drivetrain_type'].widget.attrs['class'] = 'form-control'
        self.fields['drivetrain_type'].widget.attrs['placeholder'] = 'Drivetrain type...'

        self.fields['daily_rent_price'].widget.attrs['class'] = 'form-control'
        self.fields['daily_rent_price'].widget.attrs['placeholder'] = 'Daily rent price...'

        self.fields['weekly_rent_price'].widget.attrs['class'] = 'form-control'
        self.fields['weekly_rent_price'].widget.attrs['placeholder'] = 'Weekly rent price...'

        self.fields['monthly_rent_price'].widget.attrs['class'] = 'form-control'
        self.fields['monthly_rent_price'].widget.attrs['placeholder'] = 'Monthly rent price...'

        self.fields['seats'].widget.attrs['class'] = 'form-control'
        self.fields['seats'].widget.attrs['placeholder'] = 'Seats...'

        self.fields['trunk_volume'].widget.attrs['class'] = 'form-control'
        self.fields['trunk_volume'].widget.attrs['placeholder'] = 'Trunk volume...'

        self.fields['service_mileage_interval'].widget.attrs['class'] = 'form-control'
        self.fields['service_mileage_interval'].widget.attrs['placeholder'] = 'Service mileage interval...'

        self.fields['insured_date'].widget.attrs['class'] = 'form-control'
        self.fields['insured_date'].widget.attrs['placeholder'] = 'Insured date...'

        self.fields['technical_overview_date'].widget.attrs['class'] = 'form-control'
        self.fields['technical_overview_date'].widget.attrs['placeholder'] = 'Technical overview date...'
