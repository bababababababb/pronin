from rest_framework import serializers

from .models import Client, Order


class ClientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class CsvCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


