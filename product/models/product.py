from django.db import models
from product.models.category import Category

class Product(models.Model):
    name = models.CharField(max_length=100)  # substitui title por name
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True)  # plural fica mais claro