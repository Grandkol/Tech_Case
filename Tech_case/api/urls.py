from django.urls import path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import APIProductList, APIProductDetail

router_v1 = DefaultRouter()
router_v1.register("products", APIProductList.as_view, "products")

urlpatterns = [
    path("api-token-auth/", views.obtain_auth_token),
    path("products/", APIProductList.as_view()),
    path("products/<int:pk>/", APIProductDetail.as_view()),
]
