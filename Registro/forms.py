#Importamos la libreria Forms

from xmlrpc.client import DateTime

from django import forms

#Importamos nuestros modelos

from Registro.models import Register

class FormRegistro(forms.ModelForm):
    class Meta:
        model= Register
        fields= '__all__' #Agregamos todos los campos que creamos en los modelos
       # widgets = {'Nacimiento': forms.DateInput(attrs={'type': 'date'})}
       # widgets = {'Fecha': forms.DateInput(attrs={'type': 'date'})}
