from datetime import date
from django import forms
from django.core import validators
from .models import ReclamoModel


def validate_only_alphabetic(value):
    """
    Valida que el valor recibido contenga solo letras del alfabeto.
    """
    if not value.isalpha():
        raise forms.ValidationError('Este campo solo debe contener letras.')


class Styles:
    """
    Clase de utilidad que proporciona estilos de entrada para el formulario.
    """
    @staticmethod
    def input_styles(attrs):
        """
        Devuelve un diccionario de atributos con valores por defecto.
        Recibe un diccionario con los atributos y valores personalizados del campo y
        actualiza los valores por defecto del diccionario 'default_attrs' para
        devolverlos como un diccionario único.
        """
        default_attrs = {
            'class': 'form-control',
            'style': 'border-radius: .375rem; height: 35px;'
        }
        default_attrs.update(attrs)
        return default_attrs


class ReclamoForm(forms.ModelForm):
    """
    Formulario para crear un nuevo reclamo.
    Este formulario contiene campos para ingresar información acerca de un reclamo
    a ser registrado. Los campos incluyen el número de reclamo, medio por el cual
    fue realizado, fuente de donde proviene, fecha, nombre y apellido del vecino,
    su DNI, dirección donde se generó el reclamo, urgencia del mismo, una descripción
    y fotos si las hay. Todos los campos son requeridos, excepto el correo electrónico,
    teléfono fijo, edificio, departamento y detalle. 
    """
    nombre = forms.CharField(
        label='Nombre del denunciante',
        max_length=50,
        validators=[validate_only_alphabetic],
        widget=forms.TextInput(attrs=Styles.input_styles({
            # 'placeholder': 'Nombre del denunciante'
        }))
    )
    apellido = forms.CharField(
        label='Apellido del denunciante',
        max_length=50,
        validators=[validate_only_alphabetic],
        widget=forms.TextInput(attrs=Styles.input_styles({
            # 'placeholder': 'Apellido del denunciante'
        }))
    )
    dni = forms.IntegerField(
        label='DNI',
        validators=[validators.MinValueValidator(1000000), validators.MaxValueValidator(99999999)],
        widget=forms.NumberInput(attrs=Styles.input_styles({
            'placeholder': 'e.g. 12.345.678'
        }))
    )
    celular = forms.IntegerField(
        label='Teléfono celular',
        widget=forms.NumberInput(attrs=Styles.input_styles({
            'placeholder': 'e.g. 115555555'
        }))
    )
    telefono_fijo = forms.IntegerField(
        label='Teléfono fijo',
        widget=forms.NumberInput(attrs=Styles.input_styles({
            'placeholder': 'e.g. 115555555'
        }))
    )
    correo_electronico = forms.EmailField(
        label='Correo electrónico',
        error_messages={'invalid': 'Introduce una dirección de correo electrónico válida'},
        widget=forms.EmailInput(attrs=Styles.input_styles({
            'placeholder': 'e.g. johndoe@mail.com'
        }))
    )

    class Meta:
        """
        La clase Meta se utiliza para definir opciones adicionales para el formulario.
        En este caso, se especifica el modelo asociado al formulario y los campos que
        se incluyen en el formulario.
        """
        model = ReclamoModel
        fields = [
            'medio', 'numero', 'fuente', 'fecha', 'nombre', 'apellido', 'dni',
            'celular', 'telefono_fijo', 'correo_electronico', 'localidad', 'calle',
            'altura', 'edificio', 'departamento', 'entre_calle_1', 'entre_calle_2',
            'reclamo', 'urgencia', 'foto', 'detalle'
        ]
        widgets = {
            'medio': forms.Select(attrs=Styles.input_styles({}),
                                  choices=ReclamoModel.MedioChoices.choices),
            'numero': forms.NumberInput(attrs=Styles.input_styles({}),
                                        validators=[validators.MinValueValidator(1)])
            'fuente': forms.Select(attrs=Styles.input_styles({}),
                                   choices=ReclamoModel.FuenteChoices.choices),
            'fecha': forms.DateInput(attrs=Styles.input_styles({'type': 'date', 'value': date.today().strftime('%Y-%m-%d')}),
                                     validators=[validators.MaxValueValidator(date.today)]),
            'localidad': forms.Select(attrs=Styles.input_styles({'id': 'localidad-select'}),
                                      choices=ReclamoModel.LocalidadChoices.choices),
            'calle': forms.Select(attrs=Styles.input_styles({'class': 'form-control calle-select'})),
            'altura': forms.NumberInput(attrs=Styles.input_styles({})),
            'edificio': forms.TextInput(attrs=Styles.input_styles({})),
            'departamento': forms.TextInput(attrs=Styles.input_styles({})),
            'entre_calle_1': forms.Select(attrs=Styles.input_styles({'class': 'form-control calle-select'})),
            'entre_calle_2': forms.Select(attrs=Styles.input_styles({'class': 'form-control calle-select'})),
            'reclamo': forms.Select(attrs=Styles.input_styles({}),
                                    choices=ReclamoModel.ReclamoChoices.choices),
            'urgencia': forms.Select(attrs=Styles.input_styles({}),
                                     choices=ReclamoModel.UrgenciaChoices.choices),
            'foto': forms.ClearableFileInput(attrs=Styles.input_styles({'accept': 'image/*', 'multiple': True})),
            'detalle': forms.Textarea(attrs=Styles.input_styles({'placeholder': 'Detalles del reclamo',
                                                                 'style': 'height: 10em; border-radius: .375rem;',
                                                                 'rows': 3, 'required': False})),
        }
        error_messages = {
            
        }
        required_fields = ['nombre', 'apellido', 'dni', 'celular', 'localidad', 'calle', 'altura', 'reclamo', 'urgencia']
        error_messages.update({field: {'required': 'Este campo es obligatorio.'} for field in required_fields})
    # class Styles:
    #     """
    #     Clase de utilidad que proporciona estilos de entrada para el formulario.
    #     """
    #     @staticmethod
    #     def input_styles(attrs):
    #         """
    #         Devuelve un diccionario de atributos con valores por defecto.
    #         Recibe un diccionario con los atributos y valores personalizados del campo y
    #         actualiza los valores por defecto del diccionario 'default_attrs' para
    #         devolverlos como un diccionario único.
    #         """
    #         default_attrs = {
    #             'class': 'form-control',
    #             'style': 'border-radius: .375rem; height: 35px;'
    #         }
    #         default_attrs.update(attrs)
    #         return default_attrs

    # medio = forms.ChoiceField(
    #     label='Medio',
    #     widget=forms.Select(attrs=Styles.input_styles({
    #         # 'placeholder': 'Elige un medio'
    #     })),
    #     choices=ReclamoModel.MedioChoices.choices
    # )
    # numero = forms.IntegerField(
    #     label='Número de reclamo',
    #     widget=forms.NumberInput(attrs=Styles.input_styles({
    #         # 'placeholder': 'Escribe el número de reclamo'
    #     }))
    # )
    # fuente = forms.ChoiceField(
    #     label='Fuente',
    #     widget=forms.Select(attrs=Styles.input_styles({
    #         # 'placeholder': 'Elige una fuente'
    #     })),
    #     choices=ReclamoModel.FuenteChoices.choices
    # )
    # fecha = forms.DateField(
    #     label='Fecha del reclamo',
    #     validators=[validators.MaxValueValidator(date.today)],
    #     widget=forms.DateInput(attrs=Styles.input_styles({
    #         'type': 'date',
    #         'value': date.today().strftime('%Y-%m-%d')
    #     }))
    # )
    # nombre = forms.CharField(
    #     label='Nombre del denunciante',
    #     max_length=50,
    #     validators=[validate_only_alphabetic],
    #     widget=forms.TextInput(attrs=Styles.input_styles({
    #         # 'placeholder': 'Nombre del denunciante'
    #     }))
    # )
    # apellido = forms.CharField(
    #     label='Apellido del denunciante',
    #     max_length=50,
    #     validators=[validate_only_alphabetic],
    #     widget=forms.TextInput(attrs=Styles.input_styles({
    #         # 'placeholder': 'Apellido del denunciante'
    #     }))
    # )
    # dni = forms.IntegerField(
    #     label='DNI',
    #     validators=[
    #         validators.MinValueValidator(1000000),
    #         validators.MaxValueValidator(99999999)
    #     ],
    #     widget=forms.NumberInput(attrs=Styles.input_styles({
    #         'placeholder': 'e.g. 12.345.678'
    #     }))
    # )
    # celular = forms.IntegerField(
    #     label='Teléfono celular',
    #     widget=forms.NumberInput(attrs=Styles.input_styles({
    #         'placeholder': 'e.g. 115555555'
    #     }))
    # )
    # telefono_fijo = forms.IntegerField(
    #     label='Teléfono fijo',
    #     widget=forms.NumberInput(attrs=Styles.input_styles({
    #         'placeholder': 'e.g. 115555555',
    #         'required': False,
    #     })),
    #     required=False
    # )
    # correo_electronico = forms.EmailField(
    #     label='Correo electrónico',
    #     error_messages={'invalid': 'Introduce una dirección de correo electrónico válida'},
    #     widget=forms.EmailInput(attrs=Styles.input_styles({
    #         'placeholder': 'e.g. johndoe@mail.com',
    #         'required': False,
    #     })),
    #     required=False
    # )
    # localidad = forms.ChoiceField(
    #     label='Localidad',
    #     widget=forms.Select(attrs=Styles.input_styles({
    #         # 'placeholder': 'Localidad'
    #     })),
    #     choices=ReclamoModel.LocalidadChoices.choices
    # )
    # calle = forms.ChoiceField(
    #     label='Calle',
    #     widget=forms.Select(attrs=Styles.input_styles({
    #         # 'placeholder': 'Calle'
    #     })),
    #     #! choices=CALLES CAMBIAR CON AJAX
    # )
    # altura = forms.IntegerField(
    #     label='Altura aproximada',
    #     widget=forms.NumberInput(attrs=Styles.input_styles({
    #         # 'placeholder': 'Numeración aproximada'
    #     }))
    # )
    # edificio = forms.CharField(
    #     label='Edificio',
    #     max_length=50,
    #     widget=forms.TextInput(attrs=Styles.input_styles({
    #         # 'placeholder': 'Edificio',
    #         'required': False,
    #     })),
    #     required=False
    # )
    # departamento = forms.CharField(
    #     label='Departamento',
    #     max_length=50,
    #     widget=forms.TextInput(attrs=Styles.input_styles({
    #         # 'placeholder': 'Departamento',
    #         'required': False,
    #     })),
    #     required=False
    # )
    # entre_calle_1 = forms.ChoiceField(
    #     label='Entre calle 1',
    #     widget=forms.Select(attrs=Styles.input_styles({
    #     'required': False,
    #     })),
    #     required=False,
    #     #! choices=CALLES CAMBIAR CON AJAX
    # )
    # entre_calle_2 = forms.ChoiceField(
    #     label='Entre calle 2',
    #     widget=forms.Select(attrs=Styles.input_styles({
    #         'required': False,
    #     })),
    #     required=False,
    #     #! choices=CALLES CAMBIAR CON AJAX
    # )
    # reclamo = forms.ChoiceField(
    #     label='Reclamo',
    #     widget=forms.Select(attrs=Styles.input_styles({
    #         # 'placeholder': 'Reclamo'
    #     })),
    #     choices=ReclamoModel.ReclamoChoices.choices
    # )
    # urgencia = forms.ChoiceField(
    #     label='Urgencia',
    #     widget=forms.Select(attrs=Styles.input_styles({
    #         # 'placeholder': 'Urgencia'
    #     })),
    #     choices=ReclamoModel.UrgenciaChoices.choices
    # )
    # foto = forms.FileField(
    #     label='Fotos',
    #     widget=forms.ClearableFileInput(attrs=Styles.input_styles({
    #         'accept': 'image/*',
    #         'multiple': True,
    #         'required': False,
    #     })),
    #     required=False
    # )
    # detalle = forms.CharField(
    #     label='Detalles',
    #     validators=[validators.MinLengthValidator(10)],
    #     widget=forms.Textarea(attrs=Styles.input_styles({
    #         'placeholder': 'Detalla el reclamo',
    #         'style': 'height: 10em; border-radius: .375rem;',
    #         'row': 3,
    #         'required': False,
    #     })),
    #     required=False
    # )
