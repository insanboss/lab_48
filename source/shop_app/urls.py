from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('product_app.urls')),
    path('api/v2/', include('api_v2.urls')),
]
