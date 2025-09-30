import pytest
from product.models.category import Category
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer
from product.serializers.product_serializer import ProductSerializer

@pytest.mark.django_db
def test_category_serializer():
    category = Category.objects.create(
        title="Categoria Teste",
        slug="categoria-teste",
        description="Descrição de teste",
        active=True
    )

    serializer = CategorySerializer(category)
    data = serializer.data

    assert "title" in data
    assert "slug" in data
    assert "description" in data
    assert "active" in data

    assert data["title"] == "Categoria Teste"
    assert data["slug"] == "categoria-teste"
    assert data["description"] == "Descrição de teste"
    assert data["active"] is True

@pytest.mark.django_db
def test_product_serializer():
    # cria categorias
    category1 = Category.objects.create(
        title="Categoria 1",
        slug="categoria-1"
    )
    category2 = Category.objects.create(
        title="Categoria 2",
        slug="categoria-2"
    )

    # cria produto e associa categorias
    product = Product.objects.create(
        name="Livro Django",
        description="Descrição do livro",
        price=100,
        active=True
    )
    product.categories.add(category1, category2)

    serializer = ProductSerializer(product)
    data = serializer.data

    assert "name" in data
    assert "description" in data
    assert "price" in data
    assert "active" in data
    assert "categories" in data

    assert data["name"] == "Livro Django"
    assert data["description"] == "Descrição do livro"
    assert data["price"] == 100
    assert data["active"] is True
    assert len(data["categories"]) == 2
    category_titles = [c["title"] for c in data["categories"]]
    assert "Categoria 1" in category_titles
    assert "Categoria 2" in category_titles
