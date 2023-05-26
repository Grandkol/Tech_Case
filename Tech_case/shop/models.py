from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    specifications = models.TextField(verbose_name="Характристики товара")
    photo = models.ImageField(upload_to="products", verbose_name="Фото товара")
    category = models.ForeignKey(
        "ProductCategory",
        on_delete=models.CASCADE,
        verbose_name="Категория",
        null=True
    )
    price = models.IntegerField(null=True,
                                verbose_name="Цена"
                                )
    manufacturer = models.CharField(max_length=255,
                                    verbose_name="Производитель"
                                    )

    class Meta:
        db_table = "Products"
        ordering = ["-price", "name"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")
    slug = models.SlugField(verbose_name="URL")

    class Meta:
        db_table = "ProductCategories"
        ordering = ["name", "id"]
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"

    def __str__(self):
        return self.name
