from typing import List

from django.urls import URLPattern, path

from rent import views

urlpatterns: List[URLPattern] = [
    path('dashboard/rents', views.DashboardRentsListView.as_view(), name='dashboard-rents-list-view'),
    path('dashboard/rent/create', views.DashboardRentCreateView.as_view(), name='dashboard-rent-create-view'),
    path('dashboard/rent/<int:pk>', views.DashboardRentDetailView.as_view(), name='dashboard-rent-detail-view'),
    path('dashboard/rent/<int:pk>/update', views.DashboardRentUpdateView.as_view(), name='dashboard-rent-update-view'),
    path('dashboard/rent/<int:pk>/delete', views.DashboardRentDeleteView.as_view(), name='dashboard-rent-delete-view'),

]
