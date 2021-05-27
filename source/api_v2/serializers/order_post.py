from rest_framework import serializers
from product_app.models import Order, ProductOrder


class OrderProductSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    class Meta:
        model = ProductOrder
        fields = ('id', 'quantity', 'order', 'product')
        read_only_fields = ('order',)


class OrderSerializer(serializers.ModelSerializer):
    OrderProduct = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('user_name', 'user', 'address', 'telephone', 'created_at', 'OrderProduct')

    def create(self, validated_data):
        order_product = validated_data.pop('OrderProduct')
        order = Order.objects.create(**validated_data)
        for field in order_product:
            print(field)
            p = ProductOrder.objects.create(order=order, product=field['product'], quantity=field['quantity'])
            print(p)
        validated_data['OrderProduct'] = order_product
        return validated_data
