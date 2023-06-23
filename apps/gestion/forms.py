from django import forms
from django.contrib.admin import widgets
from .models import GestionModel

class GestionForm(forms.ModelForm):
    ESTADOS = (
        ('A', 'Estado A'),
        ('B', 'Estado B'),
        ('C', 'Estado C')
    )

    estado = forms.ChoiceField(
        label='Estado', 
        widget=forms.Select(
            attrs={
                'placeholder' :'Seleccione un estado',
                'class': 'form-control', 
                'style': 'height: 2.5em'}), 
            choices=ESTADOS)
    gestion = forms.CharField(
        label='Gestión', 
        widget=forms.TextInput(
            attrs={
                'placeholder' :'Número de Gestion',
                'class': 'form-control', 
                'style': 'height: 2.5em;'})
    )
    detalle_gestion = forms.CharField(
        label='Detalle de gestión', 
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Detalle de gestión', 
                'class': 'form-control', 
                'style': 'height: 10em;'}), 
            required=False)
    equipo_trabajo = forms.CharField(
        label='Equipo de trabajo', 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Equipo de trabajo', 
                'class': 'form-control', 
                'style': 'height: 2.5em;'}), 
            required=False)
    fecha_programada = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control'}))
    fecha_solucion = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control'}))
    orden_trabajo = forms.CharField(
        label='Orden de trabajo', 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Orden de trabajo', 
                'class': 'form-control', 
                'style': 'height: 2.5em'}), 
            required=False)
    arbol = forms.CharField(
        label='Equipo de trabajo', 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Arbol', 
                'class': 'form-control', 
                'style': 'height: 2.5em;'}), 
            required=False)
    # inspecciones = forms.ChoiceField(
    #     label='Inspecciones', 
    #     widget=forms.Select(
    #         attrs={
    #             'placeholder' :'Seleccione una inspeccion',
    #             'class': 'form-control', 
    #             'style': 'height: 2.5em'}),
    #         required=False)
    
    # baja = forms.BooleanField(
    #     label='Baja',
        # widget=forms.CharField(
        #     attrs={
        #         'placeholder': 'Baja', 
        #         'class': 'form-control', 
        #         'style': 'height: 2.5em;'}),
            # required=False)
    
    class Meta:
        model = GestionModel
        fields = '__all__'
        
class BusquedaForm(forms.Form):
    campos = (
        ('none',' --- '),
        ('id','Inspeccion Nro'),
        ('inspector','Inspector'),
        ('reclamo','Reclamo'),
        ('trabajo_a_realizar','Trabajo a realizar'),
        ('urgencia_trabajo','Urgencia de trabajo'),
        ('arbol','Árbol'),
        ('especie','Especie'),
        ('especie_altura','Especie altura'),
        ('justificacion','Justificación'),
        ('no_requiere_inspecion','No requiere inspección'),
        ('observaciones','Observaciones'),
    )

    fechas = (
        ('none', ' --- '),
        ('fecha_carga_de_inspeccion','Fecha carga de inspección'),
        ('fecha_de_inspeccion','Fecha de inspección'),
    )
    
    criterio1_valor = forms.CharField( 
        label='Criterio 1', 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Texto a buscar en criterio 1',
                'class': 'form-control', 
                'style': 'height: 2.5em'}),
            required=False)
    criterio1_campo = forms.ChoiceField(
        label='Campo', 
        widget=forms.Select(
            attrs={
                'placeholder': 'Campo a filtrar', 
                'class': 'form-control-desplegable mx-auto', 
                'style': 'height: 2.5em'}), 
            choices=campos)
    
    criterio2_valor = forms.CharField( 
        label='Criterio 2', 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Texto a buscar en criterio 2',
                'class': 'form-control mx-auto', 
                'style': 'height: 2.5em'}),
                required=False)
    criterio2_campo = forms.ChoiceField(
        label='Campo', 
        widget=forms.Select(
            attrs={
                'placeholder': 'Campo a filtrar', 
                'class': 'form-control-desplegable mx-auto', 
                'style': 'height: 2.5em'}), 
            choices=campos)
    
    criterio3_valor = forms.CharField( 
        label='Criterio 3', 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Texto a buscar en criterio 3',
                'class': 'form-control mx-auto', 
                'style': 'height: 2.5em'}),
                required=False)
    criterio3_campo = forms.ChoiceField(
        label='Campo', 
        widget=forms.Select(
            attrs={
                'placeholder': 'Campo a filtrar', 
                'class': 'form-control-desplegable mx-auto', 
                'style': 'height: 2.5em'}), 
            choices=campos)

    criterio4_valor = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control mx-auto', 
                'style': 'height: 2.5em'}),
                required=False)
    criterio4_campo = forms.ChoiceField(
        label='Fecha a buscar', 
        widget=forms.Select(
            attrs={
                'placeholder': 'Fecha a filtrar', 
                'class': 'form-control-desplegable mx-auto', 
                'style': 'height: 2.5em'}), 
            choices=fechas)
    
class BusquedaGestionForm(forms.Form):
    campos = (
        ('none',' --- '),
        ('id','Gestión nro'),
        ('estado','Estado'),
        ('equipo_de_trabajo','Equipo de trabajo'),
        ('arbol','Árbol'),
        ('detalle_de_gestion','Detalle de gestión'),
        ('inspeccion_id','Inspección nro'),
        ('urgencia_de_trabajo','Urgencia trabajo'),
        ('reclamo','Reclamo'),
        ('medio','Medio'),
        ('urgencia','Urgencia'),
    )

    fechas = (
        ('none', ' --- '),
        ('fecha_programada','Fecha programada'),
        ('fecha_solucion','Fecha solución'),
        ('fecha_inspeccion','Fecha inspección'),
        ('fecha_creacion','Fecha de creación'),
    )
    
    criterio1_valor = forms.CharField( 
        label='Criterio 1', 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Texto a buscar en criterio 1',
                'class': 'form-control', 
                'style': 'height: 2.5em',
                'name': 'c1_v'}),
            required=False)
    criterio1_campo = forms.ChoiceField(
        label='Campo', 
        widget=forms.Select(
            attrs={
                'placeholder': 'Campo a filtrar', 
                'class': 'form-control-desplegable mx-auto', 
                'style': 'height: 2.5em',
                'name': 'c1_c'}), 
            choices=campos)
    
    criterio2_valor = forms.CharField( 
        label='Criterio 2', 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Texto a buscar en criterio 2',
                'class': 'form-control mx-auto', 
                'style': 'height: 2.5em',
                'name': 'c2_v'}),
                required=False)
    criterio2_campo = forms.ChoiceField(
        label='Campo', 
        widget=forms.Select(
            attrs={
                'placeholder': 'Campo a filtrar', 
                'class': 'form-control-desplegable mx-auto', 
                'style': 'height: 2.5em',
                'name': 'c2_c'}), 
            choices=campos)
    
    criterio3_valor = forms.CharField( 
        label='Criterio 3', 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Texto a buscar en criterio 3',
                'class': 'form-control mx-auto', 
                'style': 'height: 2.5em',
                'name': 'c3_v'}),
                required=False)
    criterio3_campo = forms.ChoiceField(
        label='Campo', 
        widget=forms.Select(
            attrs={
                'placeholder': 'Campo a filtrar', 
                'class': 'form-control-desplegable mx-auto', 
                'style': 'height: 2.5em',
                'name': 'c3_c'}), 
            choices=campos)

    criterio4_valor = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control mx-auto', 
                'style': 'height: 2.5em',
                'name': 'c4_v'}),
                required=False)
    criterio4_campo = forms.ChoiceField(
        label='Fecha a buscar', 
        widget=forms.Select(
            attrs={
                'placeholder': 'Fecha a filtrar', 
                'class': 'form-control-desplegable mx-auto', 
                'style': 'height: 2.5em',
                'name': 'c4_c'}), 
            choices=fechas)

# class GesContacto(forms.Form):
#     medio = forms.CharField(
#         label='Medio',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Medio', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     fuente = forms.CharField(
#         label='Fuente', 
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Fuente', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     fecha = forms.DateField(
#         label='Fecha de reclamo',
#         widget=forms.DateInput(
#             attrs={
#                 'type': 'date',
#                 'placeholder': 'Fecha de reclamo', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     nombre = forms.CharField(
#         label='Nombre', 
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Nombre', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     apellido = forms.CharField(
#         label='Apellido', 
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Apellido', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     dni = forms.CharField(
#         label='DNI', 
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'type': 'number',
#                 'placeholder': 'DNI', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     celular = forms.CharField(
#         label='Teléfono Celular', 
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Teléfono Móvil', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     tel_fijo = forms.CharField(
#         label='Teléfono fijo', 
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Teléfono fijo', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     mail = forms.CharField(
#         label='E-mail', 
#         max_length=30,
#         widget=forms.EmailInput(
#             attrs={
#                 'type': 'email',
#                 'placeholder': 'correo@servidor.com', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     calle = forms.CharField(
#         label='Calle',
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Calle', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     altura = forms.CharField(
#         label='Altura',
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'type': 'number',
#                 'placeholder': 'Altura', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     edificio = forms.CharField(
#         label='Edificio',
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Edificio', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     departamento = forms.CharField(
#         label='Departamentp',
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Departamento', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     entre_calle_1 = forms.CharField(
#         label='Entre calle 1',
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Entre calles 1', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     entre_calle_2 = forms.CharField(
#         label='Entre calle 2',
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Entre calles 2', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     localidad = forms.CharField(
#         label='Localidad',
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Localidad', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     urgencia = forms.CharField(
#         label='Urgencia',
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Urgencia', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     detalle = forms.CharField(
#         label='Detalle',
#         widget=forms.Textarea(
#             attrs={
#                 'placeholder': 'Detalles', 
#                 'class': 'form-control', 
#                 'style': 'height: 10em'}),
#         required=False)

# class GesInspector(forms.Form):
#     nombre = forms.CharField(
#         label='Inspector designado',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Inspector designado', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     lugar = forms.CharField(
#         label='Lugar de inspección', 
#         max_length=30, 
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Lugar de inspección', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     reclamo = forms.CharField(
#         label = 'Decide el reclamo ID', 
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'ID de reclamo', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     nota = forms.CharField(
#         label='Observaciones', 
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control', 
#                 'style': 'height: 10em'}), 
#             required=False)

# class GesInspeccion(forms.Form):
#     especies = (
#         (1, ""),
#         (2, "jacaranda"),
#         (3, "ceibo"),
#         (4, "lapacho")
#     )
#     trabajos = (
#         (1, ""),
#         (2, "Poda integral 1"),
#         (3, "Poda integral 2"),
#         (4, "Poda integral 3"),
#         (5, "Poda reductiva 1"),
#         (6, "Poda reductiva 2"),
#         (7, "Poda reductiva 4"),
#         (8, "Tala"),
#         (9, "Extracción"),
#         (10, "Corte de raices")
#     )
#     urgencias = (
#         (1, ""),
#         (2, "Alta"),
#         (3, "Media"),
#         (4, "Baja")
#     )
#     inspectores = (
#         (1, ""),
#         (2, "Pep Guardiola"),
#         (3, "Miguel conejito Alejandro"),
#         (4, "Angela Merkel")
#     )

#     seleccion = (
#         (1, 'No'),
#         (2, 'Si')
#     )
#     numero_reclamo = forms.ChoiceField( 
#         label='Selecciona el ID del reclamo', 
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control  mx-auto', 
#                 'style': 'height: 2em'}))
#     reclamo_valido = forms.ChoiceField(
#         label='Reclamo valido?', 
#         widget=forms.RadioSelect(
#             attrs={
#                 'class': 'col'}), 
#             choices=seleccion)
#     fecha_inspeccion = forms.DateField(
#         widget=forms.DateInput(
#             attrs={
#                 'type': 'date', 
#                 'class': 'form-control'}))
#     trabajo = forms.ChoiceField(
#         label='Seleccione trabajo a realizar', 
#         widget=forms.Select(
#             attrs={
#                 'placeholder': 'Trabajo a realizar', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}), 
#             choices=trabajos)
#     especie = forms.ChoiceField(
#         label='Seleccione especie', 
#         widget=forms.Select(
#             attrs={
#                 'placeholder': 'Seleccione una especie', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}), 
#             choices=especies)
#     altura = forms.CharField(
#         label='Ingrese altura (m)', 
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Ingrese altura en metros', 
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     dap = forms.CharField(
#         label='Ingrese DAP (cm)', 
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Ingrese DAP en centrimetro s/decimales', 'class': 'form-control', 
#                 'style': 'height: 2.5em'}))
#     cableado = forms.CharField(
#         label='Cableado cercano', 
#         widget=forms.Textarea(
#             attrs={
#                 'placeholder': 'Indique si existe cableado y tipo', 
#                 'class': 'form-control', 
#                 'style': 'height: 5em'}), 
#             required=False)
#     construccion = forms.CharField(
#         label='Construcciones cercanas', 
#         widget=forms.Textarea(
#             attrs={
#                 'placeholder': 'Indique tipo de construcción cercana', 
#                 'class': 'form-control', 
#                 'style': 'height: 5em'}), 
#                 required=False)
#     observaciones = forms.CharField(
#         label='Observaciones', 
#         widget=forms.Textarea(
#             attrs={
#                 'placeholder': 'Ingrese observaciones relevantes', 
#                 'class': 'form-control', 
#                 'style': 'height: 10em'}), 
#                 required=False)
#     urgencia = forms.ChoiceField(
#         label='Selecciones urgencia',
#         widget=forms.Select(
#             attrs={
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}), 
#             choices=urgencias)
#     justificacion = forms.CharField(
#         label='Justifique urgencia', 
#         widget=forms.Textarea(
#             attrs={
#                 'placeholder': 'Justifique brevemente la urgencia', 
#                 'class': 'form-control', 
#                 'style': 'height: 5em'}), 
#                 required=False)
#     inspector = forms.ChoiceField(
#         label='inspector', 
#         widget=forms.Select(
#             attrs={
#                 'class': 'form-control', 
#                 'style': 'height: 2.5em'}), 
#             choices=inspectores)
