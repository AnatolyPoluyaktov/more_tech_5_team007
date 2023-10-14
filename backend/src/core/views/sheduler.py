from rest_framework import viewsets
from src.core.models import Schedule
from src.core.serializers import ScheduleSerializer
from src.core.filters.schedules import ScheduleFilterSet
import django_filters


class SchedulerViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filterset_class = ScheduleFilterSet
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
