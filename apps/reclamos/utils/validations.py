from django import forms


def validate_only_alphabetic(value):
    """
    Valida que el valor recibido contenga solo letras del alfabeto.
    """
    if not value.isalpha():
        raise forms.ValidationError('Este campo solo debe contener letras.')
