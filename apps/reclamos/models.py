from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Denunciante(models.Model):
    """
    Modelo que representa a la persona que realizó un reclamo.
    Contiene información personal acerca del denunciante,
    como su nombre, apellido, DNI, número de celular,
    número de teléfono fijo y correo electrónico.
    """
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI")
    correo_electronico = models.EmailField(verbose_name="Correo electrónico")
    celular = models.IntegerField(verbose_name="Celular")
    telefono_fijo = models.IntegerField(verbose_name="Telefono fijo")

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Arbol(models.Model):
    """
    Modelo que representa un árbol. Contiene información relevante
    acerca del reclamo, como la dirección donde se encuentra el árbol,
    coordenadas GPS, especie de árbol y altura del mismo.
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

    def __str__(self):
        return f"{self.especie} [lat {self.latitud}, lng {self.longitud}]"


class Reclamo(models.Model):
    """
    Modelo que representa un reclamo realizado por un denunciante.
    Contiene información relevante acerca del reclamo,
    como su número de identificación, medio por el cual fue realizado,
    fuente del reclamo, fecha en que se realizó, datos del denunciante,
    datos del árbol afectado, tipo del reclamo, grado de urgencia,
    una foto del incidente (opcional), y un detalle del mismo.
    """

    class FuenteChoices(models.TextChoices):
        """
        Clase que representa las opciones de fuente de un reclamo.
        Las opciones son limitadas y predefinidas, y se utilizan para
        restringir los valores permitidos en el campo 'fuente' del modelo
        Reclamo.
        """
        OFICINA_1 = "1", _("Oficina 1")
        OFICINA_2 = "2", _("Oficina 2")
        OFICINA_3 = "3", _("Oficina 3")
        OFICINA_4 = "4", _("Oficina 4")
        OFICINA_5 = "5", _("Oficina 5")
        OFICINA_6 = "6", _("Oficina 6")
        OFICINA_7 = "7", _("Oficina 7")
        OFICINA_8 = "8", _("Oficina 8")
        OFICINA_9 = "9", _("Oficina 9")
        OFICINA_10 = "10", _("Oficina 10")

    class UrgenciaChoices(models.TextChoices):
        """
        Clase que representa las opciones de urgencia de un reclamo.
        Las opciones son limitadas y predefinidas, y se utilizan para
        restringir los valores permitidos en el campo 'urgencia' del modelo
        Reclamo.
        """
        NINGUNA = "0", _("Ninguna")
        BAJA = "1", _("Baja")
        MEDIA = "2", _("Media")
        ALTA = "3", _("Alta")

    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    numero = models.IntegerField(verbose_name="Número")
    medio = models.CharField(max_length=20, verbose_name="Medio")
    fuente = models.CharField(max_length=5, verbose_name="Fuente", choices=FuenteChoices.choices)
    fecha = models.DateField(verbose_name="Fecha del reclamo")
    denunciantes = models.ManyToManyField(Denunciante, verbose_name="Denunciante")
    arboles = models.ManyToManyField(Arbol, verbose_name="Arbol")
    reclamo = models.CharField(max_length=200, verbose_name="Reclamo")
    urgencia = models.CharField(max_length=5, verbose_name="Urgencia", choices=UrgenciaChoices.choices, default=UrgenciaChoices.NINGUNA)
    foto = models.ImageField(upload_to='img_reclamos', null=True, blank=True, verbose_name="Fotos") # img_reclamos define la ruta donde se almacenan las fotos
    detalle = models.CharField(max_length=500, verbose_name="Detalles")
    reclamo_valido = models.BooleanField(default=0, verbose_name="Reclamo válido")

    def __str__(self):
        return f'Reclamo {self.numero}'
