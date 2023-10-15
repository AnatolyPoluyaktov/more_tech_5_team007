from rest_framework import viewsets
from src.core.models import Office
from src.core.serializers import OfficeSerializer, DetailOfficeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from src.core.filters.office import OfficeFilterSet
import django_filters
from src.core.serializers.efficient_search_input_data import (
    EfficientSearchOfficeInputData,
)
from src.core.services.efficient_search.efficient_search_office import range_alg_offices
from src.core.serializers.prioritised_data import PrioritisedDataOffice


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

    @swagger_auto_schema(
        methods=["post"],
        request_body=EfficientSearchOfficeInputData,
    )
    @action(methods=["POST"], detail=False)
    def get_most_efficient_office(self, request, pk=None):
        data = EfficientSearchOfficeInputData(data=request.data, many=True)
        proitiesed_offices = range_alg_offices(data)
        entities = []
        for index, bank_id in enumerate(proitiesed_offices, start=1):
            entity = {"bank_id": bank_id, "proitiesed_offices": index}
            entities.append(entity)
        PrioritisedDataOffice(data=entities, many=True)
        return Response(PrioritisedDataOffice(data=entities, many=True).data)
