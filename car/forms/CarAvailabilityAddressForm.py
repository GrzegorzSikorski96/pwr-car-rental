from django import forms
from django.forms import ModelForm

from core.models import UserCarPickupAddress


class CarAvailabilityAddressForm(ModelForm):
    country = forms.CharField(
        label='Country',
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Country...', 'class': 'form-control'})
    )
    city = forms.CharField(
        label="City",
        strip=False,
        widget=forms.TextInput(attrs={'placeholder': 'City...', 'class': 'form-control'}),
    )
    postal_code = forms.CharField(
        label="Postal code",
        strip=False,
        widget=forms.TextInput(attrs={'placeholder': 'Postal code...', 'class': 'form-control'}),
    )
    street = forms.CharField(
        label="Street",
        strip=False,
        widget=forms.TextInput(attrs={'placeholder': 'Street...', 'class': 'form-control'}),
    )
    number = forms.CharField(
        label="House number",
        strip=False,
        widget=forms.TextInput(attrs={'placeholder': 'House number...', 'class': 'form-control'}),
    )

    class Meta:
        model = UserCarPickupAddress
        fields = ['country', 'city', 'postal_code', 'street', 'number']
