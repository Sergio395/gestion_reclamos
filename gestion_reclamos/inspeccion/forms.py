from django import forms

class ContactoForm(forms.Form):
    reclamo = (( 22,"00-283706-01 Arbol caido"),(21, "01-293934-02 Arbol poda"),(19, "00-297349-01 Arbol enfermo"),)
    nombre = forms.CharField(label='Inspector designado')
    lugar = forms.CharField(label='Lugar de inspección',max_length=30)
    reclamo = forms.ChoiceField(label='Decide el reclamo ID',choices=reclamo)    
    nota = forms.CharField(label='Observaciones',widget=forms.Textarea(attrs={'row':1,'cols':23}),required=False)
    
   
class NuevaInspeccion(forms.Form):
    CHOICES = [("1", "First"), ("2", "Second")]
    numero_reclamo = forms.CharField(label='Ingrese numero de reclamos') 
    reclamo_valido = forms.CharField(label='Reclamo valido?') 
    fecha_inspeccion = forms.CharField(label='Ingrese fecha de inspeccion') 
    trabajo = forms.CharField(label='Selecciones trbajo a realizar') 
    especie = forms.CharField(label='Ingrese especie') 
    altura = forms.CharField(label='Ingrese altura (m)') 
    dap = forms.CharField(label='Ingrese DAP (cm)') 
    cableado = forms.CharField(label='Cableado cercano') 
    construccion = forms.CharField(label='Construcciones cercanas') 
    observaciones = forms.CharField(label='Observaciones') 
    urgencia = forms.CharField(label='Selecciones urgencia') 
    justificacion = forms.CharField(label='Justifique urgencia') 
    inspector = forms.CharField(label='Inspector') 
    
    
    
    
    
    
    
    
    
    
    
    
                
    
    
    
    
    