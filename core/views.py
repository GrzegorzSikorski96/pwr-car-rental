from typing import Dict, Any

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from car.models import Car
from core.forms.AddressForm import AddressForm
from core.forms.UserAuthenticationForm import UserAuthenticationForm
from core.forms.UserRegistrationForm import UserRegistrationForm
from core.models import Address, User
from rent.models import Rent


def welcome(request):
    template = 'welcome.html'

    return render(request, template)


def dashboard(request):
    template = 'dashboard.html'

    return render(request, template, context={
        "rented": Car.objects.filter(status='rented').count(),
        "need_service": Car.objects.filter(status='need service').count(),
        "in_service": Car.objects.filter(status='in service').count(),
        "ready_to_rent": Car.objects.filter(status='ready to rent').count(),
        "employees": User.objects.filter(groups__name='employee').count(),
        "clients": User.objects.filter(groups__name='client').count(),
        "cars": Car.objects.all().count(),
        "rents": Rent.objects.all().count()
    })


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
    if request.user.is_authenticated:
        return redirect('dashboard-view')

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

            user.groups.add(Group.objects.get(name='client'))
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if 'next' in request.POST and request.POST.get('next'):
                return redirect(request.POST.get('next'))
            return redirect('dashboard-view')
    else:
        form = UserRegistrationForm()

    return render(request, 'auth/signup.html', {'form': form})


def core_logout(request):
    logout(request)

    return redirect('core-login-view')


class DashboardClientsListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.employee_views'
    model = User
    template_name = 'core/dashboard/clients.html'
    queryset = User.objects.filter(groups__name='client')


class DashboardClientDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'core.employee_views'
    model = User
    template_name = 'core/dashboard/client.html'


class DashboardClientCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'core.employee_views'
    form_class = UserRegistrationForm
    template_name = 'core/dashboard/create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)

        address = Address.objects.create(
            country=form.cleaned_data.get("country"),
            city=form.cleaned_data.get("city"),
            postal_code=form.cleaned_data.get("postal_code"),
            street=form.cleaned_data.get("street"),
            number=form.cleaned_data.get("number"),
        )
        address.save()
        obj.address = address

        return super(DashboardClientCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard-client-detail-view', kwargs={'pk': self.object.pk})  # type: ignore


class DashboardClientUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'core.employee_views'
    model = User
    form_class = UserRegistrationForm
    template_name = 'core/dashboard/update.html'

    def get_initial(self) -> Dict[str, Any]:
        user = User.objects.get(id=self.kwargs['pk'])
        user_dict = user.__dict__
        user_dict.update(user.address.__dict__)

        return user_dict

    def form_valid(self, form):
        obj = form.save(commit=False)

        obj.address.country = form.cleaned_data.get("country")
        obj.address.city = form.cleaned_data.get("city")
        obj.address.postal_code = form.cleaned_data.get("postal_code")
        obj.address.street = form.cleaned_data.get("street")
        obj.address.number = form.cleaned_data.get("number")
        obj.address.save()

        return super(DashboardClientUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard-client-detail-view', kwargs={'pk': self.object.pk})  # type: ignore


class DashboardClientDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'core.employee_views'
    model = User

    def get_success_url(self):
        return reverse('dashboard-clients-list-view')


class ClientAddressListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.client_views'
    model = Address
    template_name = 'core/client/address/addresses.html'

    def get_queryset(self) -> 'QuerySet':
        if self.request.user.is_authenticated:
            return Address.objects.filter(user=self.request.user)
        return Address.objects.none()


class ClientAddressCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'core.client_views'
    form_class = AddressForm
    template_name = 'core/client/address/create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user

        return super(ClientAddressCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('client-addresses-list-view')


class ClientAddressUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'core.client_views'
    form_class = AddressForm
    template_name = 'core/client/address/update.html'
    model = Address

    def get_success_url(self):
        return reverse('client-addresses-list-view')


class ClientAddressDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'core.client_views'
    model = Address

    def get_success_url(self):
        return reverse('client-addresses-list-view')
