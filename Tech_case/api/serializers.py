from rest_framework import serializers

from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        exclude = (
            "photo",
            "manufacturer",
        )
        model = Product
