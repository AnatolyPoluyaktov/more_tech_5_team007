from rest_framework import viewsets
from src.core.models import Office
from src.core.serializers import OfficeSerializer, DetailOfficeSerializer


class OfficeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    action_serializers = {
        'retrieve': DetailOfficeSerializer,
        'list': OfficeSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(MyModelViewSet, self).get_serializer_class()
