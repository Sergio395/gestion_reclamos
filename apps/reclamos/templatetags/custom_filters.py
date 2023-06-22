from django import template


register = template.Library()


@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Aplica una clase CSS al campo del formulario a través de un filtro DTL.
    """
    return field.as_widget(attrs={'class': css_class})


@register.filter(name='to_int')
def to_int(value):
    """
    Convierte un valor de tipo string a tipo int.
    """
    try:
        return int(value)
    except ValueError:
        return value
