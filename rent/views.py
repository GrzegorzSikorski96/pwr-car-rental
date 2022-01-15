from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from django.urls import reverse
from car.forms.CarForm import CarForm
from car.models import Car, Engine
from rent.forms.RentForm import RentForm
from rent.models import Rent


class DashboardRentsListView(ListView):
    model = Rent
    template_name = 'rent/dashboard/rents.html'
    queryset = Rent.objects.all()


class DashboardRentDetailView(DetailView):
    model = Rent
    template_name = 'rent/dashboard/rent.html'


class DashboardRentCreateView(CreateView):
    form_class = RentForm
    template_name = 'rent/dashboard/create.html'

    def get_success_url(self):
        return reverse('dashboard-rent-detail-view', kwargs={'pk': self.object.pk})  # type: ignore


class DashboardRentUpdateView(UpdateView):
    model = Rent
    form_class = RentForm
    template_name = 'rent/dashboard/update.html'


class DashboardRentDeleteView(DeleteView):
    model = Rent

    def get_success_url(self):
        return reverse('dashboard-rents-list-view')
