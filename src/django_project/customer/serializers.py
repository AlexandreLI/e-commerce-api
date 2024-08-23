from rest_framework import serializers


class ProductCustomerReservationSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    status = serializers.CharField()


class CustomerReservationSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()


class CustomerReservationResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    product = ProductCustomerReservationSerializer()
    customer = CustomerReservationSerializer()
    reserved_at = serializers.DateTimeField()
