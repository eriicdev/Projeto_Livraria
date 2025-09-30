import pytest
from product.models.category import Category
from product.models.product import Product

@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(
        title="Categoria Teste",
        slug="categoria-teste",
        description="Descrição de teste",
        active=True
    )

    assert category.title == "Categoria Teste"
    assert category.slug == "categoria-teste"
    assert category.description == "Descrição de teste"
    assert category.active is True

    # Verifica __str__ do Category
    assert str(category) == "Categoria Teste"

@pytest.mark.django_db
def test_create_product_with_categories():
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

    assert product.name == "Livro Django"
    assert product.description == "Descrição do livro"
    assert product.price == 100
    assert product.active is True

    # verifica categorias associadas
    assert product.categories.count() == 2
    assert category1 in product.categories.all()
    assert category2 in product.categories.all()

    # verifica __str__ do Product
    assert str(product) == "Livro Django"
