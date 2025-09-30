import pytest
from django.contrib.auth.models import User
from product.models.product import Product
from order.models import Order

@pytest.mark.django_db
def test_create_order_with_user():
    # cria usuário
    user = User.objects.create_user(username="testeuser", password="12345")

    # cria produtos
    product1 = Product.objects.create(name="Livro Django", price=50.0)
    product2 = Product.objects.create(name="Livro Python", price=70.0)

    # cria order e associa ao usuário
    order = Order.objects.create(user=user)

    # adiciona produtos ao order
    order.product.add(product1, product2)

    # validações
    assert order.user.username == "testeuser"
    assert order.product.count() == 2
    assert product1 in order.product.all()
    assert product2 in order.product.all()
