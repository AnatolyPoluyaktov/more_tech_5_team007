from rest_framework import viewsets
from src.core.models import AtmService
from src.core.serializers import AtmServiceSerializer


class AtmServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AtmService.objects.all()
    serializer_class = AtmServiceSerializer
