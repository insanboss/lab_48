from django.urls import include, path
from rest_framework import routers
from api_v2 import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router1 = routers.DefaultRouter()
router1.register(r'orders', views.OrderViewSet)

app_name = 'api_v2'

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router1.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]