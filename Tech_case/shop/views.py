from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, logout
from django.core.paginator import Paginator
from django.views.generic.list import ListView

from django.views.generic import CreateView, View
from django.urls import reverse_lazy

from Tech_case import settings
from .forms import CreationForm, ProductForm
from .models import Product

User = get_user_model()


def get_page(request, product_list):
    paginator = Paginator(product_list, settings.QUANTITY)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def index(request):
    products = Product.objects.all()
    page_obj = get_page(request, products)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "shop/index.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        "product": product,
        "request": request.user,
    }
    return render(request, "shop/product_detail.html", context)


class AddProduct(View):
    def get(self, request):
        form = ProductForm()
        context = {
            "form": form,
        }
        return render(request, "shop/add_product.html", context)

    def post(self, request):
        form = ProductForm(
            request.POST or None,
            files=request.FILES or None,
        )
        context = {
            "form": form,
        }
        if form.is_valid():
            product = form.save(commit=False)
            product.manufacturer = request.user
            product.save()
            return redirect("shop:index")
        return render(request, "shop/add_product.html", context)


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(
        request.POST or None, files=request.FILES or None, instance=product
    )
    context = {
        "product": product,
        "form": form,
        "is_edit": True,
    }
    if form.is_valid():
        product = form.save()
        product.save()
        return redirect("shop:index")
    return render(request, "shop/edit_product.html", context)


class DeleteProduct(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        form = ProductForm()
        context = {"product": product, "request": request.user, "form": form}
        return render(request, "shop/delete_product.html", context)

    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
        return redirect("shop:index")
        return render(request, "shop/delete_product.html")


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("shop:index")
    template_name = "users/signup.html"


class Search(ListView):
    """Поиск продуктов"""

    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(
            name__icontains=self.request.GET.get("q")
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context


def signout(request):
    logout(request)
    return redirect("shop:index")
