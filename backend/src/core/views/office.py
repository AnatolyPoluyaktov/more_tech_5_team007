from rest_framework import viewsets
from src.core.models import Office
from src.core.serializers import OfficeSerializer, DetailOfficeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from src.core.filters.office import OfficeFilterSet
import django_filters


class OfficeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    filterset_class = OfficeFilterSet
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    action_serializers = {
        "retrieve": DetailOfficeSerializer,
        "list": OfficeSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(OfficeViewSet, self).get_serializer_class()

    @action(methods=["POST"], detail=False)
    def get_most_efficient_office(self, request, pk=None):
        return Response({"message": f"Custom GET action executed for instance {pk}."})
