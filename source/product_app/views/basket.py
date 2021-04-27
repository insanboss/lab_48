from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.base import View
from django.contrib.auth import get_user_model
from product_app.forms import User_data
from product_app.models import Product, Basket, Order, ProductOrder
from django.contrib.sessions.models import Session


class BasketAdd(View):

    def get(self, request, *args, **kwargs):
        session = request.session.get('basket', [])
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        if product.remainder > 0:
            try:
                basket = Basket.objects.get(product__pk=product.pk, pk__in=session)
                basket.quantity += 1
                basket.save()
            except Basket.DoesNotExist:
                basket = Basket.objects.create(product=product, quantity=1)
                session.append(basket.pk)
            product.remainder -= 1
            request.session['basket'] = session
            product.save()
        return redirect('products:index')


class BasketProducts(ListView):
    model = Basket
    template_name = 'basket/basket.html'
    context_object_name = 'baskets'

    def get_queryset(self):
        session = self.request.session.get('basket', [])
        return Basket.objects.filter(pk__in=session)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        total = 0
        for basket in self.get_queryset():
            total += basket.get_total()
        context['total'] = total
        context['form'] = User_data()
        return context


class RemoveProduct(DeleteView):
    model = Basket
    success_url = reverse_lazy('products:basket')

    def get(self, request, *args, **kwargs):
        session = request.session.get('basket', [])
        product = self.get_object().product
        product.remainder += self.get_object().quantity
        session.remove(self.get_object().pk)
        request.session['basket'] = session
        product.save()
        return super().delete(request)


class MakeOrder(CreateView):
    model = Order
    form_class = User_data
    success_url = reverse_lazy('products:basket')

    def get_queryset(self):
        session = self.request.session.get('basket', [])
        return Basket.objects.filter(pk__in=session)

    def form_valid(self, form):
        user = self.request.user
        order = form.save()
        if user.is_authenticated:
            order.user = self.request.user
        order.save()
        for basket in self.get_queryset():
            ProductOrder.objects.create(order=order, product=basket.product, quantity=basket.quantity)
            basket.delete()
        self.request.session['basket'] = []
        return super(MakeOrder, self).form_valid(form)
