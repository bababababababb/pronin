from django.test import TestCase

from task.settings import BASE_DIR

class TestApi(TestCase):
    def test_upload(self):
        file_path = BASE_DIR / 'deals.csv'
        with open(file_path, 'r', encoding='UTF-8') as file:
            response = self.client.post('api/v1/upload_csv', data={'deals': file})
