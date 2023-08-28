from rest_framework import generics, views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

import csv
import json
from codecs import iterdecode

from .serializers import ClientListSerializer, CsvCreateSerializer
from .models import Client, Order

class ClientListApi(generics.ListAPIView):
    serializer_class = ClientListSerializer
    queryset = Client.objects.all().order_by('-spent_money')[:5]


class UploadCsv(views.APIView):
    parser_classes = [MultiPartParser]
    queryset = Order.objects.all()
    def post(self, request, *args, **kwargs):
        deals = request.FILES.get('deals')
        reader = csv.DictReader(iterdecode(deals, 'utf-8'))

        Order.objects.all().delete()
        for deal in reader:
            Order.objects.create(**deal)
            print(Order.objects.all()[0].customer)
        return Response({'Status': 'OK'})
