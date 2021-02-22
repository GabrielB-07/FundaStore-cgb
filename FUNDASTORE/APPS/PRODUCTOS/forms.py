from django import forms
from .models import Producto

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        labels =  {'pro_nombre': 'NOMBRE','pro_precio': 'PRECIO','pro_stock': 'STOCK','pro_descripcion':'DESCRIPCIÖN'}
        
