from typing import List

from django.urls import path, URLPattern

from log import views

urlpatterns: List[URLPattern] = [
    path('log/<int:car_id>', views.daily_mileage_report, name='daily-mileage-log'),
]
