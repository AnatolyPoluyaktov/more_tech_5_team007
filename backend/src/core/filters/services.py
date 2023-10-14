import django_filters
from src.core.models import AtmService
from django_filters import NumberFilter


class AtmServiceFilterSet(django_filters.FilterSet):
    atm_id = NumberFilter(method="get_atm_serivce_by_atm")

    class Meta:
        model = AtmService
        fields = [
            "id",
            "atm_id",
            "service",
            "service_capability",
            "service_activity",
        ]

    def get_atm_serivce_by_atm(self, name, value):
        return self.queryset.filter(atm_id=value)
