# import datetime
# from django.contrib.admin import widgets
from django import forms

from django.forms import ValidationError, ModelForm, DateField, RadioSelect 
from .models import inspecciones


class FotoPesoMaxValido:
    def __init__(self, foto_max_peso=5):
        self.foto_max_peso = foto_max_peso

    def __call__(self, value):
        peso = value.peso_max_peso * 1048576
        max_peso = self.foto_max_peso

        if peso > max_peso:
            raise ValidationError(
                f"El peso máximo de la foto es de {self.foto_max_peso}MB")
        return value


class ContactoForm(forms.Form):
    reclamo = (
        (22, "00-283706-01 Arbol caido"),
        (21, "01-293934-02 Arbol poda"),
        (19, "00-297349-01 Arbol enfermo"),
    )
    nombre = forms.CharField(label='Inspector Designado', min_length=2, max_length=25, widget=forms.TextInput(
        attrs={'placeholder': 'Ingrese su Apellido', 'class': 'form-control', 'style': 'height: 2.5em;'}))
    lugar = forms.CharField(label='Lugar de inspección', max_length=25, widget=forms.TextInput(
        attrs={'placeholder': '¿Qué lugar inspecciona?', 'class': 'form-control', 'style': 'height: 2.5em;'}))
    reclamo = forms.ChoiceField(label='Decide el reclamo ID', choices=reclamo)
    nota = forms.CharField(label='Observaciones', widget=forms.Textarea(
        attrs={'placeholder': 'Ingrese comentarios si son necesarios', 'class': 'form-control', 'style': 'height: 5em;'}), required=False)
    foto = forms.ImageField(
        validators=[FotoPesoMaxValido(foto_max_peso=2)], required=False)
    
    

class NuevaInspeccion(forms.ModelForm):
    
    class Meta:
        model = inspecciones
        fields = ['no_requiere_inspeccion',  'fecha_de_inspeccion', 'reclamo','trabajo_a_realizar', 'disposicion',
                'trabajo_a_realizar','especie','especie_altura','dap','cableado_cercano','construccion_cercana','observaciones_sitio',
                'urgencia_trabajo','justificacion','inspector','fecha_carga_inspeccion','arbol','foto'] 
        widgets = {
            #"no_requiere_inspeccion": forms.RadioSelect( attrs={ 'style': 'height: 2.5em;'}),
            'fecha_de_inspeccion': forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'style': 'height: 2.5em;'}),
            'reclamo' : forms.Select(attrs={ 'placeholder': 'Seleccione reclamos',"class" : 'form-control', 'style': 'height: 2.5em;'}),
            'trabajo_a_realizar' : forms.Select(attrs={ 'placeholder': 'Seleccione trabajo a realizar',"class" : 'form-control', 'style': 'height: 2.5em;'}),
            'disposicion' :  forms.Select(attrs={"class" : 'form-control', 'style': 'height: 2.5em;'}),
            'especie_altura' : forms.TextInput (attrs={'placeholder': 'Ingrese altura en metros', 'class': 'form-control', 'style': 'height: 2.5em;'}),
            'dap' :  forms.TextInput (attrs={'placeholder': 'Ingrese DAP en centimetros', 'class': 'form-control', 'style': 'height: 2.5em;'}),
            'cableado_cercano' : forms.Textarea (attrs={'placeholder': 'Indique si existe cableado y tipo', 'class': 'form-control', 'rows': 3}), 
            'construccion_cercana' : forms.Textarea (attrs={'placeholder': 'Indique si existe  construcciones proximas al árbol y caracteristicas', 'class': 'form-control', 'rows': 3}), 
            'observaciones_sitio' : forms.Textarea (attrs={'placeholder': 'Observaciones', 'class': 'form-control','rows': 8}), 
            'urgencia_trabajo' : forms.Select (attrs={"class" : 'form-control', 'style': 'height: 2.5em;'}),
            'justificacion' : forms.Textarea (attrs={'placeholder': 'Justifique brevemente la urgencia', 'class': 'form-control', 'rows': 3}), 
            'inspector' :  forms.Select(attrs={'placeholder': 'Selecciones inspector',"class" : 'form-control', 'style': 'height: 2.5em;'}),
            'fecha_carga_inspeccion' : forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'style': 'height: 2.5em;'}),            
            'arbol' : forms.Select(attrs={"class" : 'form-control', 'style': 'height: 2.5em;'}),
            'especie' : forms.Select(attrs={"class" : 'form-control', 'style': 'height: 2.5em;'}),
            'foto' : forms.FileInput(attrs={"class" : 'form-control', 'style': 'height: 2.5em;'})
            #'codigo_trabajo' : forms.TextInput (attrs={'placeholder': 'Generar número', 'class': 'form-control', 'style': 'height: 2.5em;'}),

        }

class NuevaCertificacion(forms.Form):
    nombre = forms.CharField(label='')
