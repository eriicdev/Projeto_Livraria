import pytest
from django.contrib.auth.models import User
from product.models.product import Product
from order.models import Order
from order.serializers.order_serializer import OrderSerializer

@pytest.mark.django_db
def test_order_serializer_returns_total_and_products():
    # cria usuário
    user = User.objects.create_user(username="testeuser", password="12345")

    # cria produtos
    product1 = Product.objects.create(name="Livro Django", price=50.0)
    product2 = Product.objects.create(name="Livro Python", price=70.0)

    # cria order e adiciona produtos
    order = Order.objects.create(user=user)
    order.product.add(product1, product2)

    # serializa
    serializer = OrderSerializer(order)

    # validações
    data = serializer.data
    assert "product" in data
    assert "total" in data
    assert data["total"] == 120.0  # 50 + 70
    assert len(data["product"]) == 2
    assert data["product"][0]["name"] in ["Livro Django", "Livro Python"]
