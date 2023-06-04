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
    codigo_arbol = models.CharField(
        max_length=50
    )
    especie = models.ForeignKey(
        EspecieArbolModel,
        on_delete=models.CASCADE
    )
    altura = models.CharField(
        max_length=50
    )
    dap = models.CharField(
        max_length=50
    )
    latitud = models.CharField(
        max_length=50
    )
    longitud = models.CharField(
        max_length=50
    )
    inclinacion = models.CharField(
        max_length=50
    )
    estado_copa = models.CharField(
        max_length=50
    )
    estado_tronco = models.CharField(
        max_length=50
    )
    estado_raiz = models.CharField(
        max_length=50
    )
    estado_plantera = models.CharField(
        max_length=50
    )
    estado_vereda = models.CharField(
        max_length=50
    )
    interferencias = models.CharField(
        max_length=50
    )
    enfermedades = models.CharField(
        max_length=50
    )
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
