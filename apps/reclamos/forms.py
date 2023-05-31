from datetime import date
from django import forms
from django.core import validators
from .models import ReclamoModel, DenuncianteModel
from ..base.choices import choices, calles_por_localidades



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
    class Meta:
        """
        La clase Meta se utiliza para definir opciones adicionales para el formulario.
        En este caso, se especifica el modelo asociado al formulario y los campos que
        se incluyen en el formulario.
        """
        model = ReclamoModel
        fields = [
            'medio', 'numero', 'fuente', 'fecha', 'localidad', 'calle', 'entre_calle_1',
            'entre_calle_2', 'altura', 'edificio', 'departamento', 'reclamo', 'urgencia', 'detalle'
        ]
        widgets = {
            'medio': forms.Select(attrs=Styles.input_styles({}),
                                    choices=choices.MedioChoices.choices),
            'numero': forms.NumberInput(attrs=Styles.input_styles({})),
            'fuente': forms.Select(attrs=Styles.input_styles({}),
                                    choices=choices.FuenteChoices.choices),
            # 'fecha': forms.DateInput(),
            'localidad': forms.Select(attrs=Styles.input_styles({'id': 'localidad-select'}),
                                        choices=choices.LocalidadChoices.choices),
            'calle': forms.Select(attrs=Styles.input_styles({
                'class': 'form-control calle-select'})),
            'altura': forms.NumberInput(attrs=Styles.input_styles({})),
            'edificio': forms.TextInput(attrs=Styles.input_styles({})),
            'departamento': forms.TextInput(attrs=Styles.input_styles({})),
            'entre_calle_1': forms.Select(attrs=Styles.input_styles({
                'class': 'form-control calle-select'})),
            'entre_calle_2': forms.Select(attrs=Styles.input_styles({
                'class': 'form-control calle-select'})),
            'reclamo': forms.Select(attrs=Styles.input_styles({}),
                                    choices=choices.ReclamoChoices.choices),
            'urgencia': forms.Select(attrs=Styles.input_styles({}),
                                        choices=choices.UrgenciaChoices.choices),
            # 'foto': forms.ClearableFileInput(attrs=Styles.input_styles({
            #     'accept': 'image/*', 'multiple': True})),
            'detalle': forms.Textarea(attrs=Styles.input_styles({'placeholder': 'Detalles del reclamo',
                                                                    'style': 'height: 10em; border-radius: .375rem;',
                                                                    'rows': 3})),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero'].validators.append(validators.MinValueValidator(1))
        self.fields['fecha'].validators.append(validators.MaxValueValidator(date.today()))
        self.fields['detalle'].validators.append(validators.MinLengthValidator(10))
        self.fields['fecha'].widget = forms.TextInput(
            attrs=Styles.input_styles({
                'type': 'date',
                'value': self.instance.fecha.strftime('%Y-%m-%d') if self.instance.fecha else date.today().strftime('%Y-%m-%d')
        }))


class DenuncianteForm(forms.ModelForm):
    class Meta:
        model = DenuncianteModel
        fields = [
            'dni', 'correo_electronico', 'nombre', 'apellido',
            'celular', 'telefono_fijo'
        ]
        widgets = {
            'dni': forms.NumberInput(attrs=Styles.input_styles({
                'placeholder': 'e.g. 12345678'})),
            'correo_electronico': forms.EmailInput(attrs=Styles.input_styles({
                'placeholder': 'e.g. johndoe@ejemplomail.com'})),
            'nombre': forms.TextInput(attrs=Styles.input_styles({})),
            'apellido': forms.TextInput(attrs=Styles.input_styles({})),
            'celular': forms.NumberInput(attrs=Styles.input_styles({
                'placeholder': 'e.g. 115555555'})),
            'telefono_fijo': forms.NumberInput(attrs=Styles.input_styles({
                'placeholder': 'e.g. 115555555'}))
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dni'].validators.append(validators.MinValueValidator(1000000))
        self.fields['dni'].validators.append(validators.MaxValueValidator(99999999))
        self.fields['correo_electronico'].validators.append(
            validators.EmailValidator(message='Introduce una dirección de correo electrónico válida'))
        self.fields['nombre'].validators.append(validate_only_alphabetic)
        self.fields['apellido'].validators.append(validate_only_alphabetic)































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
