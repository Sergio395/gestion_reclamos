import django_filters

from ..models import ReclamoModel


class ReclamoFilter(django_filters.FilterSet):
    '''
    '''
    # campo1 = django_filters.CharFilter(lookup_expr='icontains')
    # campo2 = django_filters.NumberFilter()
    fecha_creacion = django_filters.DateFilter()
    fecha_edicion = django_filters.DateFilter()
    # medio
    numero = django_filters.NumberFilter()
    # fuente
    # fecha = django_filters.DateFilter()
    # repitancia
    # localidad
    # calle
    # altura
    # reclamo
    # urgencia
    # eliminado

    class Meta:
        '''
        '''
        model = ReclamoModel
        fields = ['fecha_creacion', 'fecha_edicion', 'numero']
