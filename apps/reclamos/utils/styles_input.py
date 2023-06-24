class Styles:
    """
    Clase de utilidad para personalizar los atributos de widget para el formulario.
    """
    @staticmethod
    def input_styles(attrs):
        """Devuelve un diccionario de atributos con valores por defecto.

        Recibe un diccionario con los atributos y valores personalizados del campo y actualiza los valores por defecto del diccionario 'default_attrs' para devolverlos como un diccionario único.
        """
        default_attrs = {
            'class': 'form-control',
            'style': 'border-radius: .375rem; height: 35px;'
        }
        default_attrs.update(attrs)
        return default_attrs
