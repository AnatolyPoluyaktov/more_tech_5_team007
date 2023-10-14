from django.db import models
from django.utils.translation import gettext_lazy as _


class ServiceModes(models.IntegerChoices):
    Legal = 1, _("Legal Entity")
    Individual = 2, _("Individual Person")
