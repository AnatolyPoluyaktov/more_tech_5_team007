from django.db import models


class Atm(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    all_day = models.BooleanField()
