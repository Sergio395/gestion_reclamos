from datetime import date
from django import forms
from django.core import validators
from .models import ReclamoModel, DenuncianteModel
from ..base.constants import choices


def validate_only_alphabetic(value):
    """Valida que el valor recibido contenga solo letras del alfabeto.
    """
    if not value.isalpha():
        raise forms.ValidationError('Este campo solo debe contener letras.')


class Styles:
    """Clase de utilidad para personalizar los atributos de widget para el formulario.
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


class ReclamoForm(forms.ModelForm):
    """Formulario para crear o editar un reclamo.
    """
    class Meta:
        """Clase Meta para definir opciones adicionales para el formulario.
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
        """Inicializa el formulario y personaliza algunos campos y validadores.
        """
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
    """Formulario para crear o editar un denunciante.
    """
    class Meta:
        """Clase Meta para definir opciones adicionales para el formulario.
        """
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
        """Inicializa el formulario y personaliza algunos campos y validadores.
        """
        super().__init__(*args, **kwargs)
        self.fields['dni'].validators.append(validators.MinValueValidator(1000000))
        self.fields['dni'].validators.append(validators.MaxValueValidator(99999999))
        self.fields['nombre'].validators.append(validate_only_alphabetic)
        self.fields['apellido'].validators.append(validate_only_alphabetic)
