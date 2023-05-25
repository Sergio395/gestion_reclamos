from django.db import models
from ..gestion.models import Gestion


# Create your models here.
class Arbol(models.Model):
    """
    Modelo que representa un árbol. Contiene información relevante
    acerca del reclamo, como la dirección donde se encuentra el árbol,
    coordenadas GPS, especie de árbol y altura del mismo.
    Agregue el campo gestion en relacion uno a muchos porque entiendo que cada arbol tiene o va a tener un número de gestion, y un numero de gestion puede contener varios árboles
    """
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    calle = models.CharField(max_length=50, verbose_name="Calle")
    numeracion = models.IntegerField(verbose_name="Numeración")
    entre_calle_1 = models.CharField(max_length=50, verbose_name="Entre calle")
    entre_calle_2 = models.CharField(max_length=50, verbose_name="y calle")
    localidad = models.CharField(max_length=50, verbose_name="Localidad")
    edificio = models.CharField(max_length=50, verbose_name="Edificio")
    departamento = models.CharField(max_length=50, verbose_name="Departamento")
    latitud = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitud")
    longitud = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitud")
    especie = models.CharField(max_length=30, verbose_name="Especie")
    altura = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Altura")
    # gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.especie} [lat {self.latitud}, lng {self.longitud}]"