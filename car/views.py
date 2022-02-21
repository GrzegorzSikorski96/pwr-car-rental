from typing import Dict, Any

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from django.urls import reverse
from car.forms.CarForm import CarForm
from car.models import Car, Engine
from rent.models import Pricing


class DashboardCarsListView(ListView):
    model = Car
    template_name = 'car/dashboard/cars.html'
    queryset = Car.objects.all()


class DashboardCarDetailView(DetailView):
    model = Car
    template_name = 'car/dashboard/car.html'


class DashboardCarCreateView(CreateView):
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

        obj.engine = engine
        obj.pricing = pricing
        obj.created_by = self.request.user
        obj.updated_by = self.request.user

        return super(DashboardCarCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard-car-detail-view', kwargs={'pk': self.object.pk})  # type: ignore


class DashboardCarUpdateView(UpdateView):
    permission_required = 'core.client'
    model = Car
    form_class = CarForm
    template_name = 'car/dashboard/update.html'

    def get_initial(self) -> Dict[str, Any]:
        car = Car.objects.get(id=self.kwargs['pk'])
        car_dict = car.__dict__
        car_dict.update(car.engine.__dict__)
        car_dict.update(car.pricing.__dict__)

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

        obj.updated_by = self.request.user

        return super(DashboardCarUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard-car-detail-view', kwargs={'pk': self.object.pk})  # type: ignore


class DashboardCarDeleteView(DeleteView):
    model = Car

    def get_success_url(self):
        return reverse('dashboard-cars-list-view')
