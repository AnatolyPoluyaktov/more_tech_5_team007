from rest_framework import viewsets
from src.core.models import Atm
from src.core.serializers import AtmSerializer, DetailAtmSerializer
from src.core.filters.atm import AtmFilterSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from src.core.serializers.efficient_search_input_data import EfficientSearchOAtmInputData
import django_filters
from src.core.services.efficient_search.efficient_search_atm import range_alg_atms
from src.core.serializers.prioritised_data import PrioritisedDataAtm
class AtmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Atm.objects.all()
    serializer_class = 1
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

    @swagger_auto_schema(methods=["post"], request_body=EfficientSearchOAtmInputData)
    @action(methods=["POST"], detail=False)
    def get_most_efficient_office(self, request, pk=None):
        data = EfficientSearchOAtmInputData(data=request.data, many=True)
        proitiesed_offices = range_alg_atms(data)
        entities = []
        for index, bank_id in enumerate(proitiesed_offices, start=1):
            entity = {"bank_id": bank_id, "proitiesed_offices": index}
            entities.append(entity)
        PrioritisedDataAtm(data=entities, many=True)
        return Response(PrioritisedDataAtm(data=entities, many=True).data)
