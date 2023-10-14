from rest_framework import viewsets
from src.core.models import AtmService
from src.core.serializers import AtmServiceSerializer
from src.core.filters.services import AtmServiceFilterSet
import django_filters


class AtmServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AtmService.objects.all()
    serializer_class = AtmServiceSerializer
    filterset_class = AtmServiceFilterSet
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
