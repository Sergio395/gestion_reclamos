from django import forms
from django.contrib.admin import widgets


class ContactoForm(forms.Form):
    reclamo = (
        (22, "00-283706-01 Arbol caido"),
        (21, "01-293934-02 Arbol poda"),
        (19, "00-297349-01 Arbol enfermo"),
    )
    nombre = forms.CharField(label='Inspector designado')
    lugar = forms.CharField(label='Lugar de inspección', max_length=30)
    reclamo = forms.ChoiceField(label='Decide el reclamo ID', choices=reclamo)
    nota = forms.CharField(label='Observaciones', widget=forms.Textarea(
        attrs={'row': 1, 'cols': 23}), required=False)


class NuevaInspeccion(forms.Form):
    # esta informacion deberia venir de la BBDD ---------------------------
    reclamos = (
        (1, ""),
        (2, "01-293934-02"),
        (3, "00-297349-01"),
        (4, "00-283706-01")
    )
    especies = (
        (1, ""),
        (2, "jacaranda"),
        (3, "ceibo"),
        (4, "lapacho")
    )
    trabajos = (
        (1, ""),
        (2, "Poda integral 1"),
        (3, "Poda integral 2"),
        (4, "Poda integral 3"),
        (5, "Poda reductiva 1"),
        (6, "Poda reductiva 2"),
        (7, "Poda reductiva 4"),
        (8, "Tala"),
        (9, "Extracción"),
        (10, "Corte de raices")
    )
    urgencias = (
        (1, ""),
        (2, "Alta"),
        (3, "Media"),
        (4, "Baja")
    )
    inspectores = (
        (1, ""),
        (2, "Pep Guardiola"),
        (3, "Miguel conejito Alejandro"),
        (4, "Angela Merkel")
    )
    # --------------------------------------------------------------
    seleccion = (
        (1, 'No'),
        (2, 'Si')
    )
    numero_reclamo = forms.ChoiceField(label='Selecciona el ID del reclamo', widget=forms.Select(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}), choices=reclamos)
    reclamo_valido = forms.ChoiceField(label='Reclamo valido?', widget=forms.RadioSelect(
        attrs={'class': 'col'}), choices=seleccion)
    fecha_inspeccion = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    trabajo = forms.ChoiceField(label='Seleccione trbajo a realizar', widget=forms.Select(
        attrs={'class': 'form-control', 'style': 'height: 2.5em;'}), choices=trabajos)
    especie = forms.ChoiceField(label='Seleccione especie', widget=forms.Select(
        attrs={'class': 'form-control', 'style': 'height: 2.5em;'}), choices=especies)
    altura = forms.CharField(label='Ingrese altura (m)', widget=forms.TextInput(
        attrs={'placeholder': 'Ingrese altura en metros', 'class': 'form-control', 'style': 'height: 2.5em;'}))
    dap = forms.CharField(label='Ingrese DAP (cm)', widget=forms.TextInput(
        attrs={'placeholder': 'Ingrese DAP en centrimetro s/decimales', 'class': 'form-control', 'style': 'height: 2.5em;'}))
    cableado = forms.CharField(label='Cableado cercano', widget=forms.Textarea(
        attrs={'placeholder': 'Indique si existe cableado y tipo', 'class': 'form-control', 'style': 'height: 5em;'}), required=False)
    construccion = forms.CharField(label='Construcciones cercanas', widget=forms.Textarea(
        attrs={'placeholder': 'Indique tipo de construcción cercana', 'class': 'form-control', 'style': 'height: 5em;'}), required=False)
    observaciones = forms.CharField(label='Observaciones', widget=forms.Textarea(
        attrs={'placeholder': 'Ingrese observaciones relevantes', 'class': 'form-control', 'style': 'height: 10em;'}), required=False)
    urgencia = forms.ChoiceField(label='Selecciones urgencia', widget=forms.Select(
        attrs={'class': 'form-control', 'style': 'height: 2.5em;'}), choices=urgencias)
    justificacion = forms.CharField(label='Justifique urgencia', widget=forms.Textarea(
        attrs={'placeholder': 'Justifique brevemente la urgencia', 'class': 'form-control', 'style': 'height: 5em;'}), required=False)
    inspector = forms.ChoiceField(label='inspector', widget=forms.Select(
        attrs={'class': 'form-control', 'style': 'height: 2.5em;'}), choices=inspectores)
