# order/models.py

from django.db import models

from django.contrib.auth.models import (
    User,
)  # Faz a importação do modelo nativo do Django `User`

# Create your models here.


class Order(models.Model):
    product = models.ManyToManyField(
        "product.Product", blank=False, null=False
    )  # Faz a importação do modelo `Product` e referencia a ele com `product.Product`
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=False, null=False
    )  # Faz a importação do modelo nativo do Django `User` e referencia a ele com `User`
