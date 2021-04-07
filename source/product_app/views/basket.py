from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.base import View

from product_app.forms import User_data
from product_app.models import Product, Basket, Order, ProductOrder


class BasketAdd(View):

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        if product.remainder > 0:
            try:
                basket = Basket.objects.get(product__pk=product.pk)
                basket.quantity += 1
                basket.save()
            except Basket.DoesNotExist:
                Basket.objects.create(product=product, quantity=1)
            product.remainder -= 1
            product.save()
        return redirect('index')


class BasketProducts(ListView):
    model = Basket
    template_name = 'basket/basket.html'
    context_object_name = 'baskets'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        print(context)
        total = 0
        for basket in Basket.objects.all():
            total += basket.get_total()
        context['total'] = total
        context['form'] = User_data()
        print(context)
        return context


class RemoveProduct(DeleteView):
    model = Basket
    success_url = reverse_lazy('basket')

    def get(self, request, *args, **kwargs):
        product = self.get_object().product
        product.remainder += self.get_object().quantity
        product.save()
        return super().delete(request)


class MakeOrder(CreateView):
    model = Order
    form_class = User_data
    success_url = reverse_lazy('basket')

    def form_valid(self, form):
        order = form.save()
        for basket in Basket.objects.all():
            ProductOrder.objects.create(order=order, product=basket.product, quantity=basket.quantity)
            basket.delete()
        return super(MakeOrder, self).form_valid(form)
