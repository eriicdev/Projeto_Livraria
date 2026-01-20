# product/serializers.py
from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(
    serializers.ModelSerializer
):  # Serializador para a model Category
    class Meta:
        model = Category  # Modelo a ser serializado
        fields = "__all__"  #  Campos a serem serializados

    def create(self, validated_data):
        validated_data.setdefault("active", True)
        return super().create(validated_data)


class ProductSerializer(
    serializers.ModelSerializer
):  # Serializador para a model Product
    class Meta:
        model = Product  # Modelo a ser serializado
        fields = "__all__"  # Campos a serem serializados

    def create(self, validated_data):
        validated_data.setdefault("active", True)
        return super().create(validated_data)
