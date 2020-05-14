from django import forms
from .models import Customer, SellProduct


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class SellProductForm(forms.ModelForm):

    class Meta:
        model = SellProduct
        fields = '__all__'
