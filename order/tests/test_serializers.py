# order/tests/test_serializers.py

import pytest
from decimal import Decimal
from django.contrib.auth import get_user_model
from product.models import Product
from order.serializers import OrderSerializer

User = get_user_model()


@pytest.mark.django_db
def test_order_serializer_valid():  # teste de criação de um pedido com unico produto
    # Criando um usuário e um produto válidos
    user = User.objects.create_user(username="testuser", password="testpass")
    product = Product.objects.create(
        title="Product 1",
        slug="product-1",
        description="desc",
        price=Decimal("9.99"),
        active=True,
    )

    data = {
        "product": [product.id],
        "user": user.id,
    }

    serializer = OrderSerializer(data=data)

    assert serializer.is_valid(), serializer.errors


@pytest.mark.django_db
def test_order_serializer_mutiple_products():  # teste de criação de um pedido com varios produtos
    # Criando um usuário e produtos válidos
    user = User.objects.create_user(username="testuser", password="testpass")
    product1 = Product.objects.create(
        title="Product 1",
        slug="product-1",
        description="desc",
        price=Decimal("9.99"),
        active=True,
    )
    product2 = Product.objects.create(
        title="Product 2",
        slug="product-2",
        description="desc",
        price=Decimal("9.99"),
        active=True,
    )

    data = {
        "product": [product1.id, product2.id],
        "user": user.id,
    }

    serializer = OrderSerializer(data=data)

    assert serializer.is_valid(), serializer.errors
