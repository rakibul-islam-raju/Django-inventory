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
            "product",
            "price",
            "quantity",
            "remark",
        ]

        widgets = {
            "remark": forms.Textarea(attrs={"rows": "2"}),
        }


class PurchaseProductEditForm(forms.ModelForm):
    class Meta:
        model = PurchaseProduct
        fields = [
            "product",
            "price",
            "quantity",
            "remark",
        ]

        widgets = {
            "remark": forms.Textarea(attrs={"rows": "2"}),
        }
