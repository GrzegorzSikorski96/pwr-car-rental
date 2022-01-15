from django.forms import ModelForm

from rent.models import Rent


class RentForm(ModelForm):
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
        self.fields['rented_at'].widget.attrs['class'] = 'form-control'
        self.fields['rented_at'].widget.attrs['placeholder'] = 'Rented at...'

        self.fields['rented_to'].widget.attrs['class'] = 'form-control'
        self.fields['rented_to'].widget.attrs['placeholder'] = 'Rented to...'

        self.fields['rented_by'].widget.attrs['class'] = 'form-control'
        self.fields['rented_by'].widget.attrs['placeholder'] = 'Rented by...'

        self.fields['rented_car'].widget.attrs['class'] = 'form-control'
        self.fields['rented_car'].widget.attrs['placeholder'] = 'Rented car...'
