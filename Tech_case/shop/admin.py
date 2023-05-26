from django.contrib import admin
from .models import Product, ProductCategory

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk",
                    "name",
                    "specifications",
                    "photo",
                    "category",
                    "price"
                    )
    list_editable = ("category",)
    search_fields = ("name",)
    list_filter = ("price",)
    empty_value_display = "-пусто-"


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "slug",
    )
    search_fields = ("slug",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"
