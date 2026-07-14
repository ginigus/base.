from django import forms
from .models import Customer, Product

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'city']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'price']