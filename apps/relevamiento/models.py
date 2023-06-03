from django.db import models
# from ..inspeccion.models import InspeccionModel
from ..base.constants import choices


# Create your models here.
class EspecieArbolModel(models.Model):
    """
    Modelo que contiene los tipos de especie de arboles.
    """
    fecha_creacion = models.DateField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    fecha_edicion = models.DateField(
        auto_now=True,
        verbose_name="Fecha de edición"
    )
    nombre_cientifico = models.CharField(
        max_length=50,
        verbose_name="Nombre cientifico",
        null = True,
        blank = True
    )
    nombre_vulgar = models.CharField(
        max_length=50,
        verbose_name="Nombre vulgar",
        null = True,
        blank = True
    )
    nombre_completo = models.CharField(
        max_length=50,
        verbose_name="Nombre completo",
        null = True,
        blank = True
    )

    class Meta:
        verbose_name = "Especie"
        verbose_name_plural = "Especies"

    def __str__(self):
        return f"{self.nombre_completo}"


class ArbolModel(models.Model):
    """
    Modelo que contiene todos los datos del arbol.
    """
    fecha_creacion = models.DateField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    fecha_edicion = models.DateField(
        auto_now=True,
        verbose_name="Fecha de edición"
    )
    codigo_arbol = models.CharField()
    especie = models.ForeignKey(
        EspecieArbolModel,
        on_delete=models.CASCADE
    )
    altura = models.CharField()
    dap = models.CharField()
    latitud = models.CharField()
    longitud = models.CharField()
    inclinacion = models.CharField()
    estado_copa = models.CharField()
    estado_tronco = models.CharField()
    estado_raiz = models.CharField()
    estado_plantera = models.CharField()
    estado_vereda = models.CharField()
    interferencias = models.CharField()
    enfermedades = models.CharField()
    riesgo = models.CharField(
        max_length = 100,
        choices = choices.RiesgoChoices.choices,
        default = choices.RiesgoChoices.BLANK
    )
    # inspeccion = models.ForeignKey(
    #     InspeccionModel,
    #     null = True,
    #     blank = True,
    #     on_delete = models.CASCADE
    # )

    class Meta:
        verbose_name = "Árbol"
        verbose_name_plural = "Árboles"

    def __str__(self):
        return f"Código {self.codigo_arbol}"
