from rest_framework import serializers


class ReservationResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    customer_id = serializers.UUIDField()
    product_id = serializers.UUIDField()
    reserved_at = serializers.DateTimeField()


class ReservationRequestSerializer(serializers.Serializer):
    customer_id = serializers.UUIDField()
