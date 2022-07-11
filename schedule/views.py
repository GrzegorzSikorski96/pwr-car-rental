from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from schedule.models import Schedule
from schedule.services.generate_schedule_service import GenerateScheduleService


class DashboardSchedulesListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.employee_views'
    model = Schedule
    template_name = 'schedule/schedules.html'


class DashboardSchedulesDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'core.employee_views'
    model = Schedule
    template_name = 'schedule/schedule.html'


class GenerateSchedule(PermissionRequiredMixin, View):
    permission_required = 'core.employee_views'

    def post(self, request):
        generate_schedule_service = GenerateScheduleService()
        generate_schedule_service.generate()

        return HttpResponseRedirect(reverse('dashboard-schedules-list-view'))

# def generate_schedule(request):
#     generate_schedule_service = GenerateScheduleService()
#     generate_schedule_service.generate()
#
#     return HttpResponse({'status': 'success', 'code': 200}, content_type='application/json')
