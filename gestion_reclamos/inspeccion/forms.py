from django import forms

class ContactoForm(forms.Form):
    reclamo = (( 22,"00-283706-01 Arbol caido"),(21, "01-293934-02 Arbol poda"),(19, "00-297349-01 Arbol enfermo"),)
    nombre = forms.CharField(label='Inspector designado')
    lugar = forms.CharField(label='Lugar de inspección',max_length=30)
    reclamo = forms.ChoiceField(label='Decide el reclamo ID',choices=reclamo)    
    nota = forms.CharField(label='Observaciones',widget=forms.Textarea(attrs={'row':1,'cols':23}),required=False)
    
   
    
  