# product/models.py

from django.db import models

# Create your models here.


class Category(models.Model):  # Modelo de categoria de produtos
    title = models.CharField(max_length=255)  # Titulo da categoria
    slug = models.SlugField(unique=True)  # Slug da categoria para usar na URL
    description = models.TextField(
        max_length=500, blank=True, null=True
    )  # Descrição da categoria
    active = models.BooleanField(default=True)  # Se a categoria está ativa ou não

    def __str__(self):
        return self.title  # Retorna o título da categoria


class Product(models.Model):  # Modelo de produtos
    title = models.CharField(max_length=255)  # Título do produto
    slug = models.SlugField(unique=True)  # Slug do produto para usar na URL
    description = models.TextField(
        max_length=500, blank=True, null=True
    )  # Descrição do produto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
    active = models.BooleanField(default=True)  # Se o produto está ativo ou não
    categories = models.ManyToManyField(
        "Category", blank=True
    )  # Categorias do produto, relacionamento muitos para muitos
