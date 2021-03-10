from django import forms

from product_app.models import category_choices


class ProductForm(forms.Form):
    product = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=2000, required=False, widget=forms.Textarea)
    categories = forms.ChoiceField(choices=category_choices, required=True)
    remainder = forms.IntegerField(min_value=0)
    cost = forms.DecimalField(max_digits=7, decimal_places=2)
