# prduct/tests/test_serializers.py

import pytest
from product.serializers import ProductSerializer


@pytest.mark.django_db
def test_product_serializer_valid():
    data = {
        "title": "Test Product",
        "slug": "test-product",
        "description": "Test description",
        "price": 9.99,
    }
    serializer = ProductSerializer(data=data)
    assert serializer.is_valid(), serializer.errors  # printa erro se falhar


@pytest.mark.django_db
def test_product_serializer_invalid():
    data = {"title": "sem titulo", "price": 9.99, "active": True}
    serializer = ProductSerializer(data=data)
    assert not serializer.is_valid()
    assert "slug" in serializer.errors  # valida que slug está causando erro
