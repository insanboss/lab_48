from django import forms

from product_app.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product', 'description', 'categories', 'remainder', 'cost']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")



class User_data(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_name', 'address', 'telephone']

