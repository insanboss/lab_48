from rest_framework import serializers

from product_app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'description', 'categories', 'remainder', 'cost']
