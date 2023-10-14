from rest_framework import serializers
from src.core.models import AtmService


class AtmServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtmService
        fields = "__all__"
