from typing import Dict, Any

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import QuerySet
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from car.choices.car_status_choices import CarStatus
from car.forms.CarAvailabilityForm import CarAvailabilityForm
from car.forms.CarForm import CarForm
from car.forms.ServiceRequestForm import ServiceRequestForm
from car.models import Car, Engine, Servicing, Availability
from core.checkers.user_checkers import has_group
from log.messages.messages import LogMessage
from log.models import MessageLog
from rent.models import Pricing


class DashboardCarsListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.employee_views'
    model = Car
    template_name = 'car/dashboard/cars.html'
    queryset = Car.objects.all()


class ClientCarsListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.client_views'
    model = Car
    template_name = 'car/client/cars.html'

    def get_queryset(self) -> QuerySet:
        if self.request.user.is_authenticated:
            return Car.objects.filter(rent__rented_by=self.request.user)

        raise Http404


class DashboardCarDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'core.employee_views'
    model = Car
    template_name = 'car/dashboard/car.html'


class ClientCarDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'core.client_views'
    model = Car
    template_name = 'car/client/car.html'

    def get_queryset(self) -> QuerySet:
        return Car.objects.get_query(self.request.user)


class DashboardCarCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'core.employee_views'
    form_class = CarForm
    template_name = 'car/dashboard/create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)

        engine: Engine = Engine.objects.create(
            volume=form.cleaned_data.get("volume"),
            horsepower=form.cleaned_data.get("horsepower"),
            fuel_type=form.cleaned_data.get("fuel_type"),
        )

        pricing: Pricing = Pricing.objects.create(
            daily=form.cleaned_data.get("daily"),
            weekly=form.cleaned_data.get("weekly"),
            monthly=form.cleaned_data.get("monthly"),
        )

        servicing: Servicing = Servicing.objects.create(
            service_mileage_interval=form.cleaned_data.get("service_mileage_interval"),
            insured_date=form.cleaned_data.get("insured_date"),
            technical_overview_date=form.cleaned_data.get("technical_overview_date"),
        )

        obj.engine = engine
        obj.pricing = pricing
        obj.servicing = servicing
        obj.created_by = self.request.user
        obj.updated_by = self.request.user

        return super(DashboardCarCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard-car-detail-view', kwargs={'pk': self.object.pk})  # type: ignore


class DashboardCarUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'core.employee_views'
    model = Car
    form_class = CarForm
    template_name = 'car/dashboard/update.html'

    def get_initial(self) -> Dict[str, Any]:
        car = Car.objects.get(id=self.kwargs['pk'])
        car_dict = car.__dict__
        car_dict.update(car.engine.__dict__)
        car_dict.update(car.pricing.__dict__)
        car_dict.update(car.servicing.__dict__)

        return car_dict

    def form_valid(self, form):
        obj = form.save(commit=False)

        obj.engine.volume = int(form.cleaned_data.get("volume"))
        obj.engine.horsepower = int(form.cleaned_data.get("horsepower"))
        obj.engine.fuel_type = form.cleaned_data.get("fuel_type")
        obj.engine.save()

        obj.pricing.daily = int(form.cleaned_data.get("daily"))
        obj.pricing.weekly = int(form.cleaned_data.get("weekly"))
        obj.pricing.monthly = int(form.cleaned_data.get("monthly"))
        obj.pricing.save()

        obj.servicing.service_mileage_interval = int(form.cleaned_data.get("service_mileage_interval"))
        obj.servicing.insured_date = form.cleaned_data.get("insured_date")
        obj.servicing.technical_overview_date = form.cleaned_data.get("technical_overview_date")
        obj.servicing.save()

        obj.updated_by = self.request.user

        return super(DashboardCarUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard-car-detail-view', kwargs={'pk': self.object.pk})  # type: ignore


class DashboardCarDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'core.employee_views'
    model = Car

    def get_success_url(self):
        return reverse('dashboard-cars-list-view')


class CarAvailabilitiesListView(LoginRequiredMixin, ListView):
    model = Availability
    template_name = 'car/availability/availabilities.html'

    def get_queryset(self):
        return Availability.objects.filter(car_id=self.kwargs['car_id'])

    def get_context_data(self, **kwargs):
        context = super(CarAvailabilitiesListView, self).get_context_data(**kwargs)
        context['car'] = Car.objects.get(id=self.kwargs['car_id'])

        return context


class CarAvailabilitiesCreateView(LoginRequiredMixin, CreateView):
    form_class = CarAvailabilityForm
    template_name = 'car/availability/create.html'

    def get_form_kwargs(self, **kwargs):
        kwargs = super(CarAvailabilitiesCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['car'] = Car.objects.get(id=self.kwargs['car_id'])

        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CarAvailabilitiesCreateView, self).get_context_data(**kwargs)
        context['car'] = Car.objects.get(id=self.kwargs['car_id'])

        return context

    def get_success_url(self):
        return reverse('car-availabilities-list', kwargs={'car_id': self.object.car.id})  # type: ignore


class CarAvailabilitiesUpdateView(LoginRequiredMixin, UpdateView):
    model = Availability
    form_class = CarAvailabilityForm
    template_name = 'car/availability/update.html'

    def get_success_url(self):
        return reverse('car-availabilities-list', kwargs={'car_id': self.object.car.id})  # type: ignore

    def get_form_kwargs(self, **kwargs):
        kwargs = super(CarAvailabilitiesUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['car'] = Car.objects.get(id=self.kwargs['car_id'])

        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CarAvailabilitiesUpdateView, self).get_context_data(**kwargs)
        context['car'] = Car.objects.get(id=self.kwargs['car_id'])

        return context


def service_request(request, car_id: int):
    cars: QuerySet[Car] = Car.objects.get_query(request.user)
    car: Car = cars.get(id=car_id)

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            if car:
                car.status = CarStatus.NEED_SERVICE_STATUS

                if has_group(request.user, 'employee'):
                    action = LogMessage.SERVICE_REQUESTED_BY_EMPLOYEE
                else:
                    action = LogMessage.SERVICE_REQUESTED_BY_CLIENT

                car.messages.add(MessageLog(
                    car=car,
                    action=action,
                    message=request.POST.get('message', ''),
                    created_by=request.user,
                ),
                    bulk=False
                )

                car.save()

            return HttpResponseRedirect(request.POST.get('next', '/'))
    else:
        form = ServiceRequestForm()

    return render(request, 'car/car_confirm_service_request.html', {'form': form, 'car': car})
