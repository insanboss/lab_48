from django.shortcuts import render, get_object_or_404
from product_app.models import Product

# Create your views here.


def index_view(request):
    products = Product.objects.exclude(remainder=0).order_by('categories', 'product')
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def product_view(request, pk):

    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={'product': product})
