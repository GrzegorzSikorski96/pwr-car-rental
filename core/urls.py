from typing import List

from django.urls import path, URLPattern

from core import views

urlpatterns: List[URLPattern] = [
    path('', views.welcome, name='welcome-view'),
    path('login', views.core_login, name='core-login-view'),
    path('register', views.core_register, name='core-register-view'),
    path('logout', views.core_logout, name='core-logout'),

    path('dashboard', views.dashboard, name='dashboard-view'),

    path('dashboard/clients', views.DashboardClientsListView.as_view(), name='dashboard-clients-list-view'),
    path('dashboard/client/create', views.DashboardClientCreateView.as_view(), name='dashboard-client-create-view'),
    path('dashboard/client/<int:pk>', views.DashboardClientDetailView.as_view(), name='dashboard-client-detail-view'),
    path('dashboard/client/<int:pk>/update', views.DashboardClientUpdateView.as_view(),
         name='dashboard-client-update-view'),
    path('dashboard/client/<int:pk>/delete', views.DashboardClientDeleteView.as_view(),
         name='dashboard-client-delete-view'),

    path('client/addresses', views.ClientAddressListView.as_view(), name='client-addresses-list-view'),
    path('client/addresses/create', views.ClientAddressCreateView.as_view(), name='client-addresses-create-view'),
    path('client/addresses/<int:pk>/update', views.ClientAddressUpdateView.as_view(),
         name='client-addresses-update-view'),
    path('client/addresses/<int:pk>/delete', views.ClientAddressDeleteView.as_view(),
         name='client-addresses-delete-view'),
]
