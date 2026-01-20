#  product/tests/test_models.py

import pytest
import uuid
from product.models import Category, Product


@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(
        title="Test Category",
        slug=f"test-product-{uuid.uuid4()}",
        description="Test description",
    )
    assert category.title == "Test Category"
    assert category.active is True


@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title="Test Product",
        slug=f"test-product-{uuid.uuid4()}",
        description="Test description",
        price=9.99,
    )
    assert product.title == "Test Product"
    assert product.active is True
    assert product.price == 9.99


@pytest.mark.django_db
def test_create_product_with_multiple_categories():
    category1 = Category.objects.create(
        title="Category 1",
        slug=f"category-1-{uuid.uuid4()}",
        description="Category 1 description",
    )
    category2 = Category.objects.create(
        title="Category 2",
        slug=f"category-2-{uuid.uuid4()}",
        description="Category 2 description",
    )
    product = Product.objects.create(
        title="Test Product",
        slug=f"test-product-{uuid.uuid4()}",
        description="Test description",
        price=9.99,
    )
    # Associa as categorias após criar o produto
    product.categories.set([category1, category2])
    product.save()

    assert product.categories.count() == 2
