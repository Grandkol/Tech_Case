from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = "shop"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "search/", views.Search.as_view(template_name="shop/index.html"),
        name="search"
    ),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("signout/", views.signout, name="signout"),
    path("login/", LoginView.as_view(template_name="users/login.html"),
         name="login"),
    path("create/", views.AddProduct.as_view(), name="add_product"),
    path("<int:product_id>/edit/", views.edit_product, name="product_edit"),
    path(
        "<int:product_id>/delete/", views.DeleteProduct.as_view(),
        name="product_delete"
    ),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
]
