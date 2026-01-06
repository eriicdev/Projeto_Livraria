import debug_toolbar
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),  # Adiciona a Django Debug Toolbar
    path("admin/", admin.site.urls),
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),
    # Rotas da API
    path("", include("home.urls")),
    re_path("bookstore/(?P<version>(v1|v2)/product/)", include("product.urls")),
    re_path("bookstore/(?P<version>(v1|v2)/order/)", include("order.urls")),
]
# e70bd1dfc2063dbbfb12cff4e8eac46a2862f2d1
