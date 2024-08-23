from rest_framework import serializers


class ProductResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    status = serializers.CharField()
