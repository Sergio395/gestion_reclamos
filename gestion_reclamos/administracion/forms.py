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



