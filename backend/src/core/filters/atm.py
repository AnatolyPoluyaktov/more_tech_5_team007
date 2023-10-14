import django_filters
from src.core.models import Atm


class AtmFilterSet(django_filters.FilterSet):
    class Meta:
        model = Atm
        fields = ["id", "all_day", "status"]
