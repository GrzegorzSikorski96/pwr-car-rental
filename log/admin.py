from django.contrib import admin

from log.models import ServiceLog, CarLog, MessageLog

admin.site.register(ServiceLog)
admin.site.register(CarLog)
admin.site.register(MessageLog)
