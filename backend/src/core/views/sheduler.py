from rest_framework import viewsets
from src.core.models import Schedule
from src.core.serializers import ScheduleSerializer


class SchedulerViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
