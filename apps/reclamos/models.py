from django.db import models
from ..base.constants import choices


# Create your models here.
class DenuncianteModel(models.Model):
    """Modelo que representa a la persona que realizó un reclamo.

    Contiene información personal acerca del denunciante,
    como su nombre, apellido, DNI, número de celular,
    número de teléfono fijo y correo electrónico.
    """
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_edicion = models.DateField(auto_now=True, verbose_name="Fecha de edición")
    dni = models.BigIntegerField(verbose_name="DNI")
    correo_electronico = models.EmailField(blank=True, null=True, verbose_name="Correo electrónico")
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    celular = models.BigIntegerField(verbose_name="Teléfono celular")
    telefono_fijo = models.BigIntegerField(blank=True, null=True, verbose_name="Teléfono fijo")

    def __str__(self):
        """ Devuelve una representación en forma de cadena del denunciante.
        """
        return f"{self.apellido}, {self.nombre} DNI: {self.dni}"


class ReclamoModel(models.Model):
    """ Modelo que representa un reclamo realizado por un denunciante.

    Contiene información relevante acerca del reclamo,
    como su número de identificación, medio por el cual fue realizado,
    fuente del reclamo, fecha en que se realizó, datos del denunciante,
    datos del árbol afectado, tipo del reclamo, grado de urgencia,
    una foto del incidente (opcional), y un detalle del mismo.
    """
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_edicion = models.DateField(auto_now=True, verbose_name="Fecha de edición")
    medio = models.CharField(max_length=50, verbose_name="Medio",
                             choices=choices.MedioChoices.choices,
                             default=choices.MedioChoices.BLANK)
    numero = models.IntegerField(verbose_name="Número de reclamo")
    fuente = models.CharField(max_length=50, verbose_name="Fuente",
                              choices=choices.FuenteChoices.choices,
                              default=choices.FuenteChoices.BLANK)
    fecha = models.DateField(verbose_name="Fecha del reclamo")
    denunciantes = models.ManyToManyField(DenuncianteModel, verbose_name="Denunciante")
    localidad = models.CharField(max_length=50, verbose_name="Localidad",
                                 choices=choices.LocalidadChoices.choices,
                                 default=choices.LocalidadChoices.BLANK)
    calle = models.CharField(max_length=100, verbose_name="Calle")
    entre_calle_1 = models.CharField(max_length=100, blank=True, null=True,
                                     verbose_name="Entre calle 1")
    entre_calle_2 = models.CharField(max_length=100, blank=True, null=True,
                                     verbose_name="Entre calle 2")
    altura = models.IntegerField(verbose_name="Altura")
    edificio = models.CharField(max_length=50, blank=True, null=True, verbose_name="Edificio")
    departamento = models.CharField(max_length=50, blank=True, null=True, verbose_name="Departamento")
    reclamo = models.CharField(max_length=200, verbose_name="Reclamo",
                               choices=choices.ReclamoChoices.choices,
                               default=choices.ReclamoChoices.BLANK)
    urgencia = models.CharField(max_length=5, verbose_name="Urgencia",
                                choices=choices.UrgenciaChoices.choices,
                                default=choices.UrgenciaChoices.BLANK)
    foto = models.ImageField(upload_to='img_reclamos/', null=True,
                             blank=True, verbose_name="Fotos")
    detalle = models.CharField(max_length=500, blank=True, null=True, verbose_name="Detalles")
    eliminado = models.BooleanField(default=False)

    def soft_delete(self):
        """ Realiza una eliminación lógica del reclamo.
        """
        self.eliminado=True
        super().save()

    def restore(self):
        """ Restaura un reclamo previamente eliminado.
        """
        self.eliminado = False
        super().save()

    def __str__(self):
         """ Devuelve una representación en forma de cadena del reclamo.
         """
        return f'Reclamo {self.numero}'
