from rest_framework import serializers


class PrioritisedDataOffice(serializers.Serializer):
    bank_id = serializers.IntegerField(read_only=True)
    priority = serializers.IntegerField(read_only=True)


class PrioritisedDataAtm(serializers.Serializer):
    atm_id = serializers.IntegerField(read_only=True)
    priority = serializers.IntegerField(read_only=True)