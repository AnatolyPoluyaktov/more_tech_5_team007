from rest_framework import viewsets
from src.core.models import Atm
from src.core.serializers import AtmSerializer, DetailAtmSerializer
from src.core.filters.atm import AtmFilterSet
import django_filters


class AtmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Atm.objects.all()
    serializer_class = AtmSerializer
    filterset_class = AtmFilterSet
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    action_serializers = {
        "retrieve": DetailAtmSerializer,
        "list": AtmSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(AtmViewSet, self).get_serializer_class()
