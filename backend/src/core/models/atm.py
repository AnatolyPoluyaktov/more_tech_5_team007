from django.db import models
from src.core.choices.atm_statuses import AtmStatuses


class Atm(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    status = models.CharField(choices=AtmStatuses.choices)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    all_day = models.BooleanField()
