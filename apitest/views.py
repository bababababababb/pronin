from rest_framework import generics, views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

import csv
import json
from codecs import iterdecode

from .serializers import ClientListSerializer, CsvUploadSerializer
from .models import Client, Order

class ClientListApi(generics.ListAPIView):
    serializer_class = ClientListSerializer
    queryset = Client.objects.all().order_by('-spent_money')[:5]


class UploadCsv(views.APIView):
    parser_classes = [MultiPartParser]
    queryset = Order.objects.all()
    def post(self, request, *args, **kwargs):
        deals = request.FILES.get('deals')

        # File's name and extension validators
        if not deals:
            return Response({'Status': 'Error', 'Desc': 'There is no deals.csv file'})
        if not deals.name.endswith('.csv'):
            return Response({'Status': 'Error', 'Desc': 'File deals must be a .csv format'})

        reader = csv.DictReader(iterdecode(deals, 'utf-8'))

        # File's column names validator
        # keys_list = list(next(reader).keys())
        # fields_list = [_.name for _ in Order._meta.get_fields()]
        # fields_list.remove('id')
        # if keys_list != fields_list:
        #     return Response({'Status': 'Error', 'Desc': 'File deals.csv in uncorrect format'})

        Order.objects.all().delete()
        for deal in reader:

            Order.objects.create(**deal)

        return Response({'Status': 'OK'})
