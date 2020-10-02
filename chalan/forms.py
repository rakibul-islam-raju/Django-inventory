from django import forms
from .models import Chalan_In, Chalan_Out


class ChalanInCreateForm(forms.ModelForm):

    class Meta:
        model = Chalan_In
        fields = ['chalan_name',
                'product',
                'quantity',
                'price',
                'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': '2'}),
        }


class ChalanOutCreateForm(forms.ModelForm):

    class Meta:
        model = Chalan_Out
        fields = ['chalan',
                'chalan_name',
                'product',
                'quantity',
                'price',
                'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': '2'}),
        }
