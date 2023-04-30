from django import forms
from django.contrib.admin import widgets


class AdminForm(forms.Form):
    pass

class Userform(forms.Form):
    
      pass 

    #usuario = forms.CharField (label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    # password= forms.CharField (label='Contraseña', widget=forms.RadioSelect(
        # attrs={'class': 'col'}), choices='')
    # permisos= forms.CharField (label='Inspector designado',
        # attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'})

class Empresaform(forms.Form):
    
      pass 
  
class Nuevaform(forms.Form):    
   

    nombre = forms.CharField (label='Nombre', max_length=20 ,widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    
    razon= forms.CharField (label='Razón social',  max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    
    proveedor= forms.IntegerField (label='N° proveedor', widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    
    cuit= forms.CharField (label='N° Cuit',max_length=9, min_length=9,widget=forms.TextInput(
     attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    
    correo= forms.EmailField(label='Correo',widget=forms.TextInput(
     attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    
    telefono= forms.IntegerField (label='Telefono',widget=forms.TextInput(
     attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    
    
class Newuserform(forms.Form):    
   
    usuario = forms.CharField (label='Usuario', max_length=20 ,widget=forms.TextInput(
    attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    
    nombre = forms.CharField (label='Nombre', max_length=20 ,widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    
    apellido= forms.CharField (label='Apellido',  max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    
    contra= forms.IntegerField (label='Contraseña', widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    
    permiso= forms.CharField (label='Permisos',max_length=9, min_length=9,widget=forms.TextInput(
     attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    
    legajo= forms.EmailField(label='Legajo',widget=forms.TextInput(
     attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    
    
    








