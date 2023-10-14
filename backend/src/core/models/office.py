from django.db import models
from backend.src.core.choices.office_status import OfficeStatuses


class Office(models.Model):
    sale_point_name = models.CharField(max_length=255, help_text="Наименование ТП")
    address = models.CharField(max_length=255, help_text="Адрес ТП")
    status = models.CharField(max_length=6, choices=OfficeStatuses.choices)
