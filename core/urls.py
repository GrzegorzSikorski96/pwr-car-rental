from typing import List

from django.urls import path, URLPattern

from core import views

urlpatterns: List[URLPattern] = [
    path('', views.dashboard, name='dashboard-view'),
]
