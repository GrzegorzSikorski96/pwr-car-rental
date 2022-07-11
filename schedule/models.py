from django.db import models

from core.models_mixins.TimeStampMixin import TimeStampMixin


class Event(TimeStampMixin):
    title = models.CharField(max_length=150)
    start = models.DateTimeField()
    end = models.DateTimeField()
    address = models.ForeignKey('core.Address', on_delete=models.DO_NOTHING, related_name='events')
    schedule = models.ForeignKey('schedule.Schedule', on_delete=models.DO_NOTHING, related_name='events')


class Schedule(TimeStampMixin):
    date = models.DateField()
    employee = models.ForeignKey('core.User', on_delete=models.DO_NOTHING, related_name='schedules')
    is_archive = models.BooleanField(default=False)
    time = models.IntegerField()

    class Meta:
        ordering = ['is_archive', 'employee_id']
