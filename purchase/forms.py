from django import forms
from .models import Supplier, PurchaseProduct


class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'address']


class PurchaseProductForm(forms.ModelForm):

    class Meta:
        model = PurchaseProduct
        fields = '__all__'
        # fields = ['name', 'price', 'quantity', 'description', 'warehouse']
