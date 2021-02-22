from django import forms

class FormularioContactenos(forms.Form):
    nombre = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=128)
    telefono = forms.CharField(max_length=64)
    mensaje = forms.CharField(widget=forms.Textarea)

   