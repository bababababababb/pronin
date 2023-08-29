from rest_framework import generics, views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

import csv
import json
from codecs import iterdecode

from .serializers import ClientSerializer, CsvUploadSerializer
from .models import Client, Order

class ClientListApi(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all().order_by('-spent_money')[:5]


class UploadCsv(views.APIView):
    parser_classes = [MultiPartParser]
    queryset = Order.objects.all()
    def post(self, request, *args, **kwargs):
        deals = request.FILES.get('deals')

        if not deals:
            return Response({'Status': 'Error', 'Desc': 'There is no deals.csv file'})
        if not deals.name.endswith('.csv'):
            return Response({'Status': 'Error', 'Desc': 'File deals must be a .csv format'})

        reader = csv.DictReader(iterdecode(deals, 'utf-8'))

        serializer = CsvUploadSerializer(data=list(reader), many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'OK'})
        return Response({'Status': "Error", 'Desc': 'File deals.csv in uncorrect format'})


