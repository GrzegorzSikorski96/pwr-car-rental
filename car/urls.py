from typing import List

from django.urls import URLPattern, path

from car import views

urlpatterns: List[URLPattern] = [
    path('dashboard/cars', views.DashboardCarsListView.as_view(), name='dashboard-cars-list-view'),
    path('dashboard/car/create', views.DashboardCarCreateView.as_view(), name='dashboard-car-create-view'),
    path('dashboard/car/<int:pk>', views.DashboardCarDetailView.as_view(), name='dashboard-car-detail-view'),
    path('dashboard/car/<int:pk>/update', views.DashboardCarUpdateView.as_view(), name='dashboard-car-update-view'),
    path('dashboard/car/<int:pk>/delete', views.DashboardCarDeleteView.as_view(), name='dashboard-car-delete-view'),
]
