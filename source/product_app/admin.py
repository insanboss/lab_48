from django.contrib import admin
from product_app.models import Product, ProductOrder, Order

# Register your models here.


admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Order)