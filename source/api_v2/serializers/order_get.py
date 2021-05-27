from rest_framework import serializers

from api_v2.serializers import ProductSerializer
from product_app.models import Order, ProductOrder


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductOrder
        fields = ('id', 'quantity', 'order', 'product')
        read_only_fields = ('order',)


class OrderGetSerializer(serializers.ModelSerializer):
    OrderProduct = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('user_name', 'user', 'address', 'telephone', 'created_at', 'OrderProduct')
