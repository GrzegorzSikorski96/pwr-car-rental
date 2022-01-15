from django.contrib import admin

from log.models import ServiceLog, CarLog

admin.site.register(ServiceLog)
admin.site.register(CarLog)
