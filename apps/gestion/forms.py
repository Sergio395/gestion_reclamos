from django import forms


class GestionForm(forms.Form):
    reclamo = (
        ( 22,"00-283706-01 Arbol caido"),
        (21, "01-293934-02 Arbol poda"),
        (19, "00-297349-01 Arbol enfermo"),
    )
    medio = forms.CharField(label='Medio')
    fuente = forms.CharField(label='Fuente',max_length=30)
    fecha = forms.DateField(label='Fecha de reclamo')
    nombre = forms.CharField(label='Nombre',max_length=30)
    apellido = forms.CharField(label='Apellido',max_length=30)
    dni = forms.CharField(label='DNI',max_length=30)
    celular = forms.CharField(label='Teléfono Celular',max_length=30)
    tel_fijo = forms.CharField(label='Teléfono fijo',max_length=30)
    mail = forms.CharField(label='Mail',max_length=30)
    calle = forms.CharField(label='Calle',max_length=30)
    altura = forms.CharField(label='Altura',max_length=30)
    edificio = forms.CharField(label='Edificio',max_length=30)
    departamento = forms.CharField(label='Departamentp',max_length=30)
    entre_calle_1 = forms.CharField(label='Entre calle 1',max_length=30)
    entre_calle_2 = forms.CharField(label='Entre calle 2',max_length=30)
    localidad = forms.CharField(label='Localidad',max_length=30)
    urgencia = forms.CharField(label='Urgencia',max_length=30)
    detalle = forms.CharField(label='Detalle',widget=forms.Textarea(
        attrs={'row':1,'cols':23}),required=False)
    especie = forms.CharField(label='Especie',max_length=30)
    altura = forms.CharField(label='Altura (mts)',max_length=30)
    dap = forms.CharField(label='DAP (cm)',max_length=30)
    cableado_cercano = forms.CharField(label='Lugar de inspección',max_length=30)
    construccion_cercana = forms.CharField(label='Construcción cercana',max_length=30)
    inspector = forms.CharField(label='Inspector',max_length=30)
    