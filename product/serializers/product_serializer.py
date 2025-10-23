from rest_framework import serializers
from product.models.category import Category
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    # Representação das categorias (read-only)
    categories = CategorySerializer(read_only=True, many=True)
    # Para criar/atualizar categorias pelo ID (write-only)
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        many=True
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'name',           # ⚡ Corrigido: era 'title' no modelo você trocou por 'name'
            'description',
            'price',
            'active',
            'categories',     # ⚡ Adicionado vírgula e corrigido nome do campo
            'categories_id'   # ⚡ Corrigido: adicionado vírgula
        ]

    def create(self, validated_data):
        categories_data = validated_data.pop('categories_id', [])
        product = Product.objects.create(**validated_data)
        product.categories.set(categories_data)  # ⚡ melhor do que loop
        return product
