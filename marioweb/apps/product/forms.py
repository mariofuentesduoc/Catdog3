from django import forms 
from apps.product.models import Product 

class productForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'description',
            'cost',
            'size',
        ]   

        labels = {
            'description': "Descripción",
            'cost' :"Valor",
            'size' : "Tamaño",

        }

        widgets = {
            'description': forms.TextInput(attrs={'class':'validate'}),
            'cost': forms.TextInput(attrs={'class':'validate'}),
            'size': forms.TextInput(attrs={'class':'validate'}),

        }