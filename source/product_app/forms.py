from django import forms

from product_app.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product', 'description', 'categories', 'remainder', 'cost']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")



