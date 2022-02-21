from django import forms
from django.forms import ModelForm

from rent.models import Pricing


class PricingForm(ModelForm):

    daily = forms.IntegerField(
        label='Daily rent price',
        widget=forms.NumberInput(attrs={'placeholder': 'Daily rent price...', 'class': 'form-control'})
    )
    weekly = forms.IntegerField(
        label='Weekly rent price',
        widget=forms.NumberInput(attrs={'placeholder': 'Weekly rent price...', 'class': 'form-control'})
    )
    monthly = forms.IntegerField(
        label='Monthly rent price',
        widget=forms.NumberInput(attrs={'placeholder': 'Monthly rent price...', 'class': 'form-control'})
    )

    class Meta:
        model = Pricing
        fields = [
            'daily',
            'weekly',
            'monthly',
        ]

    def __init__(self, *args, **kwargs):
        super(PricingForm, self).__init__(*args, **kwargs)
