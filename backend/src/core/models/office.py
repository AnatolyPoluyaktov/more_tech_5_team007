from django.db import models
from src.core.choices.office_status import OfficeStatuses


class Office(models.Model):
    sale_point_name = models.CharField(max_length=255, help_text="Наименование ТП")
    address = models.CharField(max_length=255, help_text="Адрес ТП")
    status = models.CharField(max_length=6, choices=OfficeStatuses.choices)
    rko = models.BooleanField()
    office_type = models.CharField(max_length=255)
    sale_point_format = models.CharField(max_length=255)
    suo_avialability = models.BooleanField()
    workloads = models.JSONField()
    has_ramp = models.BooleanField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    metro_station = models.CharField(max_length=255, null=True)
