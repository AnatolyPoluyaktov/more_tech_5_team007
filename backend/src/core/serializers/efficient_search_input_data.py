from rest_framework import serializers
from src.core.models import Office


class EfficientSearchOfficeInputData(serializers.Serializer):
    bank_id = serializers.PrimaryKeyRelatedField(queryset=Office.objects.all())
    distance_auto = serializers.IntegerField()
    distance_foot = serializers.IntegerField()
    distance_moto = serializers.IntegerField()
    time_auto = serializers.TimeField()
    time_foot = serializers.TimeField()
    time_moto = serializers.TimeField()
    person_per_window = serializers.FloatField()
    registered_person_per_service = serializers.FloatField()
