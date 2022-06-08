from typing import List

from django.urls import URLPattern, path

from car import views

urlpatterns: List[URLPattern] = [
    path('dashboard/cars', views.DashboardCarsListView.as_view(), name='dashboard-cars-list-view'),
    path('dashboard/car/create', views.DashboardCarCreateView.as_view(), name='dashboard-car-create-view'),
    path('dashboard/car/<int:pk>', views.DashboardCarDetailView.as_view(), name='dashboard-car-detail-view'),
    path('dashboard/car/<int:pk>/update', views.DashboardCarUpdateView.as_view(), name='dashboard-car-update-view'),
    path('dashboard/car/<int:pk>/delete', views.DashboardCarDeleteView.as_view(), name='dashboard-car-delete-view'),

    path('client/cars', views.ClientCarsListView.as_view(), name='client-cars-list-view'),
    path('client/car/<int:pk>', views.ClientCarDetailView.as_view(), name='client-car-detail-view'),

    path('car/<int:car_id>/service/request', views.service_request, name='car-service-request'),

    path('car/<int:car_id>/availabilities', views.CarAvailabilitiesListView.as_view(), name='car-availabilities-list'),
    path('car/<int:car_id>/availabilities/create', views.CarAvailabilitiesCreateView.as_view(), name='car-availabilities-create'),
    path('car/<int:car_id>/availabilities/<int:pk>/update', views.CarAvailabilitiesUpdateView.as_view(), name='car-availabilities-update'),
]
