from rest_framework import serializers

from .models import Client, Order


class ClientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class CsvUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'customer',
            'item',
            'total',
            'quantity',
            'date'
        )

    def create(self, validated_data):
        pass


