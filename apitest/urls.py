from django.urls import path

from .views import ClientListApi, UploadCsv

urlpatterns = [
    path('api/v1/client_list', ClientListApi.as_view(), name='ClientList'),
    path('api/v1/upload_csv', UploadCsv.as_view(), name='UploadCsv')
]