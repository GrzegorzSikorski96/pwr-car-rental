from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={'placeholder': 'Email here...', 'class': 'form-control'})
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password here...', 'class': 'form-control'}),
    )
