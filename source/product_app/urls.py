from django.urls import path
from product_app.views import (
    IndexProducts,
    ProductView,
    ProductCreate,
    ProductUpdate,
    ProductDelete,
    BasketAdd,
    BasketProducts,
    RemoveProduct,
    MakeOrder,
)

app_name = 'products'

urlpatterns = [
    path('', IndexProducts.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreate.as_view(), name='product_add'),
    path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('basket/<int:pk>/add/', BasketAdd.as_view(), name='basket_add'),
    path('basket/', BasketProducts.as_view(), name='basket'),
    path('basket/<int:pk>/remove/', RemoveProduct.as_view(), name='remove_product'),
    path('basket/order/', MakeOrder.as_view(), name='make_order'),
]
