from django.db import models
from django.utils.translation import gettext_lazy as _
from typing import Iterable, Optional
from django.contrib.auth.models import User

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
        A = "A", _("Estado A")
        B = "B", _("Estado B")
        C = "C", _("Estado C")
        D = "D", _("Estado D")

    estado = models.CharField(max_length=30, verbose_name="Estado", choices=EstadosChoices.choices, default=EstadosChoices.BLANK)
    gestion = models.CharField(max_length=30, verbose_name="Gestión")
    detalle_gestion = models.CharField(max_length=250, verbose_name="Detalle de gestión")
    equipo_trabajo = models.CharField(max_length=30, verbose_name="Equipo de trabajo")
    fecha_programada = models.DateField(auto_now_add=False, verbose_name="Fecha programada")
    fecha_solucion = models.DateField(auto_now_add=False, verbose_name="Fecha de solución")
    orden_trabajo = models.CharField(max_length=30, verbose_name="Orden de trabajo")
    arbol = models.CharField(max_length=30, verbose_name="Arbol")
    baja = models.BooleanField(default=False)

    # def __str__(self):
    #     return self

    def soft_delete(self):
        self.baja = True
        super().save()

    def restore(self):
        self.baja = False
        super().save()

    # class Meta:
    #     abstract = False