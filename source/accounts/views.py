from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView

from product_app.models import Product, Basket
from .forms import MyUserCreationForm


class RegisterView(CreateView):
    model = User
    template_name = 'registration/user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('products:index')
        return next_url


class MyLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        session = self.request.session.get('basket', [])
        baskets = Basket.objects.filter(pk__in=session)
        print(baskets)
        for basket in baskets:
            basket.product.remainder += basket.quantity
            basket.product.save()
            basket.delete()
        return super(MyLogoutView, self).dispatch(request, *args, **kwargs)
