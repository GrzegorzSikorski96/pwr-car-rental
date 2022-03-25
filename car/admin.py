from django.contrib import admin

from car.models import Car, Engine, CompanyCar, Servicing

admin.site.register(Car)
admin.site.register(Engine)
admin.site.register(Servicing)
admin.site.register(CompanyCar)
