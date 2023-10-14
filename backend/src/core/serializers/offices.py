from rest_framework import serializers
from src.core.models import Office


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = [
            "id",
            "sale_point_name",
            "address",
            "latitude",
            "longitude",
            "status",
            "office_type",
        ]


class DetailOfficeSerializer(serializers.ModelSerializer):
    schedules = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Office
        fields = "__all__"
