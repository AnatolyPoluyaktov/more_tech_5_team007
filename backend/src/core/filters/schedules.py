import django_filters
from src.core.models import Schedule


class ScheduleFilterSet(django_filters.FilterSet):
    class Meta:
        model = Schedule
        fields = {
            "id": ["exact"],
            "office": ["exact"],
            "days_of_week": ["exact"],
            "open_time": ["exact", "lte", "gte"],
            "close_time": ["exact", "lte", "gte"],
            "service_mode": ["exact"],
            "is_serves": ["exact"],
            "is_weekend": ["exact"],
        }
