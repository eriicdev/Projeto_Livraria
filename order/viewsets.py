from rest_framework import viewsets
from rest_framework.exceptions import ParseError, NotFound
from django.contrib.auth.models import User
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated

from .serializers import OrderSerializer
from .models import Order


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.all()

        if user.is_staff:
            user_filter = self.request.query_params.get("user", None)
            if user_filter is not None:
                if not user_filter.isdigit():
                    raise ParseError(detail=f"User [{user_filter}] not valid")
                if not User.objects.filter(id=user_filter).exists():
                    raise NotFound(detail=f"User [{user_filter}] not exists")
                queryset = queryset.filter(user=user_filter)
            return queryset

        else:
            queryset = queryset.filter(user=user)
            if not queryset.exists():
                raise NotFound(detail="Você não tem nenhum pedido registrado.")
            return queryset
