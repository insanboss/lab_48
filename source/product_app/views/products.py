from django.db.models import Q
from django.shortcuts import get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from product_app.forms import ProductForm, SimpleSearchForm
from product_app.models import Product
from django.utils.http import urlencode


# Create your views here.


class IndexProducts(ListView):
    template_name = 'products/index.html'
    context_object_name = 'products'
    model = Product
    ordering = 'categories'

    paginate_by = 5
    paginate_orphans = 3

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        context['search'] = self.search_value
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(product__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset.order_by('product', 'categories').exclude(remainder=0)


class ProductView(DetailView):
    template_name = 'products/product_view.html'
    model = Product
    context_object_name = 'product'


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/product_create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('products:product_view', kwargs={'pk': self.object.pk})


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('products:product_view', kwargs={'pk': self.object.pk})


class ProductDelete(DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('products:index')


