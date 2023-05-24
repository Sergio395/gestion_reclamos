from django.db import models
from django.utils.translation import gettext_lazy as _
# from ..inspeccion.models import Arbol
# from ..reclamos.models import Reclamo

# Create your models here.
class Gestion(models.Model):
    """
    Modelo para la tabla gestion.
    Se relaciona con Arbol en una relación muchos a muchos, porque un arbol puede estar en solo una orden de trabajo, pero una orden de trabajo puede contener muchos árboles
    """
    class EstadosChoices(models.TextChoices):
        """
        Clase que representa las opciones de estados de un reclamo.
        Las opciones son limitadas y predefinidas, y se utilizan para
        restringir los valores permitidos en el campo 'estados' del modelo
        Gestion.
        """
        BLANK = "", _("")
        EA = "A", _("Estado A")
        EB = "B", _("Estado B")
        EC = "C", _("Estado C")
        ED = "D", _("Estado D")

    estado = models.CharField(max_length=30, verbose_name="Estado", choices=EstadosChoices.choices, default=EstadosChoices.BLANK)
    gestion = models.CharField(max_length=30, verbose_name="Gestión")
    detalle_gestion = models.CharField(max_length=250, verbose_name="Detalle de gestión")
    equipo_trabajo = models.CharField(max_length=30, verbose_name="Equipo de trabajo")
    fecha_programada = models.DateField(auto_now_add=True, verbose_name="Fecha programada")
    fecha_solucion = models.DateField(auto_now_add=True, verbose_name="Fecha de solución")
    orden_trabajo = models.CharField(max_length=30, verbose_name="Orden de trabajo")
    # reclamo = models.ManyToManyField(Reclamo, verbose_name="Reclamo")
    eliminado = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.gestion}, {self.arbol}, {self.fecha_programada}, {self.fecha_solucion}"

    class Meta:
        abstract = False