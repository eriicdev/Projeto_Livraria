from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from product.factories import ProductFactory, CategoryFactory
from order.factories import OrderFactory, UserFactory
from order.models import Order

class TestOrderViewSet(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.category = CategoryFactory(title='technology')
        self.product = ProductFactory(name='mouse', price=100, categories=[self.category])
        self.user = UserFactory()
        self.order = OrderFactory(product=[self.product], user=self.user)

    def test_order_list(self):
        response = self.client.get(reverse('order-list', kwargs={'version': 'v1'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()[0]
        product_data = data['product'][0]
        self.assertEqual(product_data['name'], self.product.name)
        self.assertEqual(product_data['price'], self.product.price)
        self.assertEqual(product_data['active'], self.product.active)
        self.assertEqual(product_data['categories'][0]['title'], self.category.title)

    def test_create_order(self):
        product = ProductFactory()
        user = UserFactory()
        data = {
            'products_id': [product.id],
            'user': user.id
        }
        response = self.client.post(reverse('order-list', kwargs={'version': 'v1'}),
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_order = Order.objects.get(user=user)
        self.assertTrue(created_order.product.filter(id=product.id).exists())
