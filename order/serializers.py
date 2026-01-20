# order/serializers.py
from rest_framework import serializers
from .models import Order


class OrderSerializer(
    serializers.ModelSerializer
):  # Serializador para a classe `Order`
    class Meta:
        model = Order  # Modelo a ser serializado
        fields = "__all__"  # Campos a serem serializados
