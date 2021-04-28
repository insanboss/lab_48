from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import (
    RegisterView, MyLogoutView, MyOrderList,
)

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', MyLogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='create'),
    path('my_order_list/', MyOrderList.as_view(), name='my_order_list'),
]