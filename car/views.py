from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from django.urls import reverse
from car.forms.CarForm import CarForm
from car.models import Car, Engine


class DashboardBoardsListView(ListView):
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
            volume=form.cleaned_data.get("engine_volume"),
            horsepower=form.cleaned_data.get("horsepower"),
            fuel_type=form.cleaned_data.get("fuel_type"),
        )

        obj.engine = engine
        return super(DashboardCarCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard-cars-detail-view', kwargs={'pk': self.object.pk})  # type: ignore


class DashboardCarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car/dashboard/update.html'


class DashboardCarDeleteView(DeleteView):
    model = Car

    def get_success_url(self):
        return reverse('dashboard-cars-list-view')
