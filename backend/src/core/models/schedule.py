from django.db import models
from backend.src.core.choices.days_of_week import DaysOfWeek
from backend.src.core.choices.service_modes import ServiceModes


class Schedule(models.Model):
    office = models.ForeignKey("Office", on_delete=models.CASCADE, related_name="schedules")
    days_of_week = models.CharField(max_length=3, choices=DaysOfWeek.choices)
    open_time = models.TimeField()
    close_time = models.TimeField()
    service_mode = models.PositiveSmallIntegerField(choices=ServiceModes.choices)
    is_serves = models.BooleanField(default=True)
    is_weekend = models.BooleanField(default=True)
