from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from core.forms.UserAuthenticationForm import UserAuthenticationForm
from core.forms.UserRegistrationForm import UserRegistrationForm
from core.models import Address


def welcome(request):
    template = 'welcome.html'

    return render(request, template)


def dashboard(request):
    template = 'dashboard.html'

    return render(request, template)


def core_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard-view')

    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST and request.POST.get('next'):
                return redirect(request.POST.get('next'))
            return redirect('dashboard-view')
    else:
        form = UserAuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})


def core_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            address = Address.objects.create(
                country=request.POST.get('country'),
                city=request.POST.get('city'),
                postal_code=request.POST.get('postal_code'),
                street=request.POST.get('street'),
                number=request.POST.get('number'),
            )
            user.address = address
            user.save()

            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard-view')

    else:
        form = UserRegistrationForm()

    return render(request, 'auth/signup.html', {'form': form})


def core_logout(request):
    logout(request)

    return redirect('core-login-view')
