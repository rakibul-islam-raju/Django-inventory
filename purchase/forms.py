from django import forms
from .models import *


# class SupplierForm(forms.ModelForm):

#     class Meta:
#         model = Supplier
#         fields = ['name',
#                 'email',
#                 'phone',
#                 'address']

#         widgets = {
#             'address': forms.Textarea(attrs={'rows': '2'}),
#         }


class PurchaseProductForm(forms.ModelForm):

    class Meta:
        model = PurchaseProduct
        fields = [
            'product',
            'price',
            'quantity',
            'payment_type',
            'bank',
            'check_no',
            'check_date',
            'remark'
        ]

        widgets = {
            'remark': forms.Textarea(attrs={'rows': '2'}),
            'check_date': forms.DateInput(attrs={'type': 'date'}, format='%d/%m/%Y')
        }


class PurchaseProductEditForm(forms.ModelForm):

    class Meta:
        model = PurchaseProduct
        fields = [
            'product',
            'price',
            'quantity',
            'payment_type',
            'bank',
            'check_no',
            'check_date',
            'remark'
        ]

        widgets = {
            'remark': forms.Textarea(attrs={'rows': '2'}),
            'check_date': forms.DateInput(attrs={'type': 'date'}, format='%d/%m/%Y')
        }
