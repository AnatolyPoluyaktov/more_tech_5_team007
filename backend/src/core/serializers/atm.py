from rest_framework import serializers
from src.core.models import Atm


class AtmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atm
        fields = [
            "id",
            "address",
            "latitude",
            "longitude",
            "all_day",
        ]


class DetailAtmSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Atm
        fields = "__all__"
