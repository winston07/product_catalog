from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.
from zebrands.models import Product


class ProductTestCase(TestCase):
    # def setUp(self):
    #     Product.objects.all()

    def test_get_education(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)
        print('client==>')
