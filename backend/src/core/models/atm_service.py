from django.db import models


class AtmService(models.Model):
    atm = models.ForeignKey("Atm", on_delete=models.CASCADE, related_name="services")
    service = models.CharField(max_length=255)
    service_capability = models.CharField(max_length=255)
    service_activity = models.CharField(max_length=255)
