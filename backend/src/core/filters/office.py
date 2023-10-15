import django_filters
from src.core.models import Office


class OfficeFilterSet(django_filters.FilterSet):
    class Meta:
        model = Office
        fields = [
            "id",
            "status",
            "office_type",
            "sale_point_format",
            "suo_avialability",
            "has_ramp",
            "metro_station",
        ]
