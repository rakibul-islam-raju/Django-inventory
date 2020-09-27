from django import forms
from .models import Supplier, PurchaseProduct


class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'address']

        widgets = {
            'address': forms.Textarea(attrs={'rows': '2'}),
        }


class PurchaseProductForm(forms.ModelForm):

    class Meta:
        model = PurchaseProduct
        fields = ['category', 'name', 'price', 'quantity', 'description', 'warehouse', 'supplier']

        widgets = {
            'description': forms.Textarea(attrs={'rows': '2'}),
        }
