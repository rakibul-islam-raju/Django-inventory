from django import forms
from .models import Customer, SellProduct


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']

        widgets = {
            'address': forms.Textarea(attrs={'rows': '2'}),
        }


class SellProductForm(forms.ModelForm):

    class Meta:
        model = SellProduct
        fields = [
            'customer',
            'product',
            'price',
            'quantity',
            'description'
        ]

        widgets = {
            'description': forms.Textarea(attrs={'rows': '2'}),
        }
