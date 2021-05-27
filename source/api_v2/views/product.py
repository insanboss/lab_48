from rest_framework import viewsets

from api_v2.serializers.order_post import OrderSerializer
from api_v2.serializers.order_get import OrderGetSerializer
from product_app.models import Product, Order
from api_v2.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    # serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OrderSerializer
        elif self.request.method == "GET":
            return OrderGetSerializer
