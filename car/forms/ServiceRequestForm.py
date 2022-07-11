from django import forms
from django.forms import ModelForm

from car.models import Servicing


class ServiceRequestForm(ModelForm):
    message = forms.CharField(
        label='Reason of service request',
        widget=forms.Textarea(attrs={'placeholder': 'Reason of service request...', 'class': 'form-control'})
    )

    class Meta:
        model = Servicing
        fields = [
            'message',
        ]
