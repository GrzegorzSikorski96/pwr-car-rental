from django.db import models

from core.models_mixins.TimeStampMixin import TimeStampMixin


class Event(TimeStampMixin):
    title = models.CharField(max_length=150)
    start = models.DateTimeField()
    end = models.DateTimeField()
    address = models.ForeignKey('car.Availability', on_delete=models.DO_NOTHING, related_name='events')
    schedule = models.ForeignKey('schedule.Schedule', on_delete=models.DO_NOTHING, related_name='events')


class Schedule(TimeStampMixin):
    date = models.DateField()
    employee = models.ForeignKey('core.User', on_delete=models.DO_NOTHING, related_name='schedules')
