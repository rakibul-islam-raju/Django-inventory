from django import forms
from django.forms.models import inlineformset_factory
from .models import Customer, Sell, SellProductItem


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "email", "phone"]


class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ["customer"]


class SellProductItemForm(forms.ModelForm):
    class Meta:
        model = SellProductItem
        fields = ["product", "price", "quantity"]


SellInlineFormset = inlineformset_factory(
    parent_model=Sell,
    model=SellProductItem,
    form=SellProductItemForm,
    can_delete=False,
    extra=2,
)
