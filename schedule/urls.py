from typing import List

from django.urls import path, URLPattern

from schedule import views

urlpatterns: List[URLPattern] = [
    path('schedule/generate', views.generate_schedule, name='schedule-generate'),
]
