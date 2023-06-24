from datetime import date
from django import forms
from django.core import validators

from .models import ReclamoModel, DenuncianteModel
from .utils.styles_input import Styles
from ..base.constants import choices, calles_choices
from .utils.validations import validate_only_alphabetic


# * ==================== RECLAMO FORM ==================== *

class ReclamoForm(forms.ModelForm):
    """
    Formulario para crear o editar un reclamo.
    """
    class Meta:
        """
        Clase Meta para definir opciones adicionales para el formulario.
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
                'class': 'form-control calle-select'}),
                                  choices=calles_choices.Calles.choices),
            'altura': forms.NumberInput(attrs=Styles.input_styles({})),
            'edificio': forms.TextInput(attrs=Styles.input_styles({})),
            'departamento': forms.TextInput(attrs=Styles.input_styles({})),
            'entre_calle_1': forms.Select(attrs=Styles.input_styles({
                'class': 'form-control calle-select'}),
                                          choices=calles_choices.Calles.choices),
            'entre_calle_2': forms.Select(attrs=Styles.input_styles({
                'class': 'form-control calle-select'}),
                                          choices=calles_choices.Calles.choices),
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
        """
        Inicializa el formulario y personaliza algunos campos y validadores.
        """
        super().__init__(*args, **kwargs)
        self.fields['numero'].validators.append(validators.MinValueValidator(1))
        self.fields['fecha'].validators.append(validators.MaxValueValidator(date.today()))
        self.fields['fecha'].widget = forms.TextInput(
            attrs=Styles.input_styles({
                'type': 'date',
                'value': self.instance.fecha.strftime('%Y-%m-%d') if self.instance.fecha else date.today().strftime('%Y-%m-%d')
        }))
        self.fields['detalle'].validators.append(validators.MinLengthValidator(10))


# * ==================== DENUNCIANTE FORM ==================== *

class DenuncianteForm(forms.ModelForm):
    """
    Formulario para crear o editar un denunciante.
    """
    class Meta:
        """
        Clase Meta para definir opciones adicionales para el formulario.
        """
        model = DenuncianteModel
        fields = [
            'dni', 'correo_electronico', 'nombre', 'apellido',
            'celular', 'telefono_fijo'
        ]
        widgets = {
            'dni': forms.NumberInput(attrs=Styles.input_styles({})),
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
        """
        Inicializa el formulario y personaliza algunos campos y validadores.
        """
        super().__init__(*args, **kwargs)
        self.fields['dni'].validators.append(validators.MinValueValidator(1000000))
        self.fields['dni'].validators.append(validators.MaxValueValidator(99999999))
        self.fields['nombre'].validators.append(validate_only_alphabetic)
        self.fields['apellido'].validators.append(validate_only_alphabetic)
