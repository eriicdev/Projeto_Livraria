#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny   # ← alterado

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    permission_classes = [AllowAny]  # ← rota pública
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
