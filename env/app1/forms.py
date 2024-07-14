from django import forms

from . models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name',  'price', 'description','is_published']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }