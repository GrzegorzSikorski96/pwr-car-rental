from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from rent.forms.RentForm import RentForm
from rent.models import Rent


class DashboardRentsListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.employee_views'
    model = Rent
    template_name = 'rent/dashboard/rents.html'
    queryset = Rent.objects.all()


class DashboardRentDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'core.employee_views'
    model = Rent
    template_name = 'rent/dashboard/rent.html'


class DashboardRentCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'core.employee_views'
    form_class = RentForm
    template_name = 'rent/dashboard/create.html'

    def get_success_url(self):
        return reverse('dashboard-rent-detail-view', kwargs={'pk': self.object.pk})  # type: ignore


class DashboardRentUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'core.employee_views'
    model = Rent
    form_class = RentForm
    template_name = 'rent/dashboard/update.html'


class DashboardRentDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'core.employee_views'
    model = Rent

    def get_success_url(self):
        return reverse('dashboard-rents-list-view')
