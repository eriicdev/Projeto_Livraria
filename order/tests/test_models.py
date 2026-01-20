# order/tests/test_models.py

import pytest
from django.contrib.auth import get_user_model
from product.models import Product  # ajuste conforme seu app de produtos
from order.models import Order

User = get_user_model()


@pytest.mark.django_db
def test_create_order():  # teste de criação de uma ordem com um produto
    user = User.objects.create_user(username="testuser", password="12345")
    product = Product.objects.create(
        title="Livro Teste", slug="livro-teste", price=50.0
    )

    order = Order.objects.create(user=user)  # cria o pedido sem produtos
    order.product.add(product)  # adiciona o produto ao pedido

    # Verificações
    assert product in order.product.all()
    assert order.user == user


@pytest.mark.django_db
def test_create_order_with_multiple_products():  # teste de criação de uma ordem com varios produtos
    user = User.objects.create_user(username="testuser", password="12345")
    product1 = Product.objects.create(
        title="Livro Teste 1", slug="livro-teste-1", price=50.0
    )
    product2 = Product.objects.create(
        title="Livro Teste 2", slug="livro-teste-2", price=50.0
    )

    order = Order.objects.create(user=user)  # cria o pedido sem produtos
    order.product.add(product1, product2)  # adiciona os produtos ao pedido

    # Verificações
    assert product1 in order.product.all()
    assert product2 in order.product.all()
    assert order.user == user


@pytest.mark.django_db
def test_delete_order():  # teste de exclusão de uma ordem
    user = User.objects.create_user(username="testuser", password="12345")
    product = Product.objects.create(
        title="Livro Teste", slug="livro-teste", price=50.0
    )

    order = Order.objects.create(user=user)  # cria o pedido sem produtos
    order.product.add(product)  # adiciona o produto ao pedido

    # Verificações
    assert product in order.product.all()
    assert order.user == user

    order.delete()  # deleta o pedido

    # Verificações
    assert not Order.objects.filter(id=order.id).exists()
