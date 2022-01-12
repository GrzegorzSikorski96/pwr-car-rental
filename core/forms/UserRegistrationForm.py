from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.forms.AddressForm import AddressForm
from core.models import User


class UserRegistrationForm(UserCreationForm, AddressForm):
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={'placeholder': 'Email...', 'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password...', 'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation...', 'class': 'form-control'}),
    )
    first_name = forms.CharField(
        label="First name",
        strip=False,
        widget=forms.TextInput(attrs={'placeholder': 'First name...', 'class': 'form-control'}),
    )
    last_name = forms.CharField(
        label="Last name",
        strip=False,
        widget=forms.TextInput(attrs={'placeholder': 'Last name...', 'class': 'form-control'}),
    )
    phone_number = forms.CharField(
        label="Phone number",
        strip=False,
        widget=forms.TextInput(attrs={'placeholder': 'Phone number...', 'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', ]
