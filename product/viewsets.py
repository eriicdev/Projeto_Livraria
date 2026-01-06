# product/viewsets.py

from rest_framework.viewsets import ModelViewSet  # viewset padrao
from product.models import Product, Category  # models
from product.serializers import ProductSerializer, CategorySerializer  # serializers
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)  # autenticação
from rest_framework.permissions import IsAuthenticated  # permissoes
from rest_framework.exceptions import ParseError, NotFound


# viewset para produtos
class ProductViewSet(ModelViewSet):
    # serializers
    serializer_class = ProductSerializer

    # autenticação

    # Removiso a necessidade de autenticação no Produtos
    # authentication_classes = [
    #     SessionAuthentication,
    #     BasicAuthentication,
    #     TokenAuthentication,
    #     ]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Product.objects.all()
        params = self.request.query_params

        # Filtro por ativo
        active_filter = params.get("active", None)
        if active_filter is not None:
            if active_filter.lower() == "true":
                queryset = queryset.filter(active=True)
            elif active_filter.lower() == "false":
                queryset = queryset.filter(active=False)

        # Filtro por categoria
        category_filter = params.get("category", None)
        if category_filter is not None:
            try:
                category_filter = int(category_filter)
                queryset = queryset.filter(categories__id=category_filter)
            except ValueError:
                raise ParseError(detail=f"Category [{category_filter}] not valid")
            except Category.DoesNotExist:
                raise NotFound(detail=f"Category [{category_filter}] not exists")

        return queryset


# viewset para categorias
class CategoryViewSet(ModelViewSet):
    # serializers
    serializer_class = CategorySerializer

    # removendo a necessidade de autenticação no Categorias
    # authentication_classes = [
    #     SessionAuthentication,
    #     BasicAuthentication,
    #     TokenAuthentication,
    #     ]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Category.objects.all()

        # Filtro por ativo
        active_filter = self.request.query_params.get("active", None)
        if active_filter is not None:
            if active_filter.lower() == "true":
                queryset = queryset.filter(active=True)
            elif active_filter.lower() == "false":
                queryset = queryset.filter(active=False)

        return queryset
