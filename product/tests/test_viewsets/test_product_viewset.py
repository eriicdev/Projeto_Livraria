from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from product.factories import ProductFactory, CategoryFactory
from product.models import Product

class TestProductViewSet(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.product = ProductFactory(name='pro controller', price=200)

    def test_get_all_product(self):
        response = self.client.get(reverse('product-list', kwargs={'version': 'v1'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data[0]['name'], self.product.name)
        self.assertEqual(data[0]['price'], self.product.price)
        self.assertEqual(data[0]['active'], self.product.active)

    def test_create_product(self):
        category = CategoryFactory()
        data = {
            'name': 'notebook',
            'price': 800,
            'categories_id': [category.id]
        }
        response = self.client.post(reverse('product-list', kwargs={'version': 'v1'}),
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_product = Product.objects.get(name='notebook')
        self.assertEqual(created_product.name, 'notebook')
        self.assertEqual(created_product.price, 800)
        self.assertIn(category, created_product.categories.all())
