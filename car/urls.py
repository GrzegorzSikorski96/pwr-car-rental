from typing import List

from django.urls import URLPattern, path

from car import views

urlpatterns: List[URLPattern] = [
    path('cars', views.DashboardBoardsListView.as_view(), name='dashboard-cars-list-view'),
    path('car/create', views.DashboardCarCreateView.as_view(), name='dashboard-car-create-view'),
    path('car/<int:pk>', views.DashboardCarDetailView.as_view(), name='dashboard-cars-detail-view'),

]
