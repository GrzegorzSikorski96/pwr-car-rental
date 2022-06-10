from typing import List

from django.urls import path, URLPattern

from schedule import views

urlpatterns: List[URLPattern] = [
    path('schedules', views.DashboardSchedulesListView.as_view(), name='dashboard-schedules-list-view'),
    path('schedule/<int:pk>', views.DashboardSchedulesDetailView.as_view(), name='dashboard-schedule-detail-view'),
    path('schedule/generate', views.GenerateSchedule.as_view(), name='schedule-generate'),
]
