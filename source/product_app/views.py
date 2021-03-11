from django.shortcuts import render, get_object_or_404, redirect

from product_app.forms import ProductForm
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


def product_create_view(request):
    if request.method == 'GET':
        product = ProductForm()
        return render(request, 'product_create.html', context={'form': product})
    elif request.method == 'POST':
        product = ProductForm(data=request.POST)
        if product.is_valid():
            product = Product(
                product=product.cleaned_data.get('product'),
                description=product.cleaned_data.get('description'),
                categories=product.cleaned_data.get('categories'),
                remainder=product.cleaned_data.get('remainder'),
                cost=product.cleaned_data.get('cost'),
            )
            product.save()
        else:
            return render(request, 'product_create.html', context={'form': product})
        return redirect('product_view', pk=product.id)


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            "product": product.product,
            "description": product.description,
            "categories": product.categories,
            "remainder": product.remainder,
            "cost": product.cost,
        })
        return render(request, 'product_update.html', context={'form': form, "id": product.id})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.product = form.cleaned_data.get('product')
            product.description = form.cleaned_data.get('description')
            product.categories = form.cleaned_data.get('categories')
            product.remainder = form.cleaned_data.get('remainder')
            product.cost = form.cleaned_data.get('cost')

            product.save()
        else:
            return render(request, 'product_update.html', context={'form': form, "id": product.id})
        return redirect('product_view', pk=product.id)


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')
