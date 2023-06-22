import django_filters
from django import forms
from django.db.models import Q

from ..models import ReclamoModel
from ..forms import Styles
from ...base.constants import choices, calles_choices


OPERATOR_CHOICES = [
    ('exact', 'Igual que'),
    ('gt', 'Mayor que'),
    ('lt', 'Menor que'),
    ('gte', 'Mayor o igual que'),
    ('lte', 'Menor o igual que'),
    ('ne', 'Distinto que'),
]


class FechaInicioFilter(django_filters.DateFilter):
    """Filtro personalizado para filtrar por fecha de inicio.

    Este filtro verifica si se proporciona una fecha de inicio en el formulario y
    filtra los resultados del queryset para que la fecha sea mayor o igual a la
    fecha de inicio especificada.
    """
    def filter(self, qs, value):
        fecha_inicio = self.parent.data.get('fecha_inicio')

        if fecha_inicio:
            lookup = f'{self.field_name}__gte'
            filter_expr = {lookup: fecha_inicio}
            return qs.filter(Q(**filter_expr))
        return qs


class FechaFinFilter(django_filters.DateFilter):
    """Filtro personalizado para filtrar por fecha de fin.

    Este filtro verifica si se proporciona una fecha de fin en el formulario y
    filtra los resultados del queryset para que la fecha sea menor o igual a la
    fecha de fin especificada.
    """
    def filter(self, qs, value):
        fecha_fin = self.parent.data.get('fecha_fin')

        if fecha_fin:
            lookup = f'{self.field_name}__lte'
            filter_expr = {lookup: fecha_fin}
            return qs.filter(Q(**filter_expr))
        return qs


class RepitanciaFilter(django_filters.NumberFilter):
    """Filtro personalizado para filtrar por repitancia.

    Este filtro verifica si se proporciona un operador y un valor de repitancia en el formulario
    y filtra los resultados del queryset según el operador y el valor de repitancia especificados.
    """
    def filter(self, qs, value):
        repitancia_operador = self.parent.data.get('repitancia_operador')

        if repitancia_operador and value:
            lookup = f'{self.field_name}__{repitancia_operador}'
            filter_expr = {lookup: value}
            return qs.filter(Q(**filter_expr))
        return qs


class ReclamoFilter(django_filters.FilterSet):
    """
    Conjunto de filtros personalizados para el modelo ReclamoModel.
    """
    # fecha_creacion = django_filters.DateFilter(
        # widget=forms.DateInput(attrs=Styles.input_styles({'type': 'date'})))
    # fecha_edicion = django_filters.DateFilter(
        # widget=forms.DateInput(attrs=Styles.input_styles({'type': 'date'})))
    numero = django_filters.NumberFilter(
        widget=forms.NumberInput(attrs=Styles.input_styles({}))
    )
    fecha_inicio = FechaInicioFilter(
        field_name='fecha_inicio',
        label='Fecha inicio',
        widget=forms.DateInput(attrs=Styles.input_styles({'type': 'date'})),
    )
    fecha_fin = FechaFinFilter(
        field_name='fecha_fin',
        label='Fecha fin',
        widget=forms.DateInput(attrs=Styles.input_styles({'type': 'date'})),
    )
    medio = django_filters.ChoiceFilter(
        widget=forms.Select(attrs=Styles.input_styles({})),
        choices=choices.MedioChoices.choices,
        empty_label=None
    )
    fuente= django_filters.ChoiceFilter(
        widget=forms.Select(attrs=Styles.input_styles({})),
        choices=choices.FuenteChoices.choices,
        empty_label=None
    )
    repitancia_operador = django_filters.ChoiceFilter(
        widget=forms.Select(attrs=Styles.input_styles({})),
        choices=OPERATOR_CHOICES,
        empty_label='< Operador >'
    )
    repitancia = RepitanciaFilter(
        widget=forms.NumberInput(attrs=Styles.input_styles({}))
    )
    localidad = django_filters.ChoiceFilter(
        widget=forms.Select(attrs=Styles.input_styles({})),
        choices=choices.LocalidadChoices.choices,
        empty_label=None
    )
    calle = django_filters.ChoiceFilter(
        widget=forms.Select(attrs=Styles.input_styles({})),
        choices=calles_choices.Calles.choices,
        empty_label=None
    )
    altura = django_filters.NumberFilter(
        widget=forms.NumberInput(attrs=Styles.input_styles({}))
    )
    reclamo = django_filters.ChoiceFilter(
        widget=forms.Select(attrs=Styles.input_styles({})),
        choices=choices.ReclamoChoices.choices,
        empty_label=None
    )
    urgencia = django_filters.ChoiceFilter(
        widget=forms.Select(attrs=Styles.input_styles({})),
        choices=choices.UrgenciaChoices.choices,
        empty_label=None
    )
    # eliminado

    class Meta:
        """
        Metadatos para el conjunto de filtros ReclamoFilter.
        """
        model = ReclamoModel
        fields = ['numero', 'fecha', 'medio', 'fuente', 'repitancia_operador', 'repitancia', 'localidad', 'calle', 'altura', 'reclamo', 'urgencia']
