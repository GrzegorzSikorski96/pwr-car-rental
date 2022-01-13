from typing import List

from django.urls import path, URLPattern

from core import views

urlpatterns: List[URLPattern] = [
    path('', views.welcome, name='welcome-view'),
    path('login', views.core_login, name='core-login-view'),
    path('register', views.core_register, name='core-register-view'),
    path('logout', views.core_logout, name='core-logout'),
    path('dashboard', views.dashboard, name='dashboard-view'),
]
