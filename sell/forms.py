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
        # fields = ['warehouse', 'customer', 'product', 'status', 'description']
        fields = ['warehouse', 'customer','product', 'price', 'quantity', 'status', 'description']

        widgets = {
            'description': forms.Textarea(attrs={'rows': '2'}),
        }
