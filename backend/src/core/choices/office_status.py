from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


class OfficeStatuses(TextChoices):
    OPEN = "open", _("открытая")
    CLOSED = "closed", _("Закрытая")
