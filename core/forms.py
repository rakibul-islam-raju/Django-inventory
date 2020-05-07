from django import forms
from .models import Office, Department, Category, Product


class OfficeForm(forms.ModelForm):

    class Meta:
        model = Office
        fields = '__all__'


class DeptForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = '__all__'


class CategotyForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
