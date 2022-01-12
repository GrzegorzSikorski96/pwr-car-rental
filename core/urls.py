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

#
# <div class="input-group mb-3">
#           {{ form.username }}
#           <div class="input-group-append">
#             <div class="input-group-text">
#               <span class="fas fa-envelope"></span>
#             </div>
#           </div>
#         </div>
#         <div class="input-group mb-3">
#           {{ form.password }}
#           <div class="input-group-append">
#             <div class="input-group-text">
#               <span class="fas fa-lock"></span>
#             </div>
#           </div>
#         </div>
#         <div class="input-group mb-3">
#           {{ form.password1 }}
#           <div class="input-group-append">
#             <div class="input-group-text">
#               <span class="fas fa-lock"></span>
#             </div>
#           </div>
#         </div>
