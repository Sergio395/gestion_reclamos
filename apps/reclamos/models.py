from django.db import models


# Create your models here.
class Fuente(models.Model):
    """
    Modelo que representa una fuente de reclamos.
    Contiene información acerca de la fuente, como sus siglas y nombre.
    """
    siglas = models.CharField(max_length=3)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.siglas} => {self.nombre}"


class Denunciante(models.Model):
    """
    Modelo que representa a la persona que realizó un reclamo.
    Contiene información personal acerca del denunciante,
    como su nombre, apellido, DNI, número de celular,
    número de teléfono fijo y correo electrónico.
    """
    fecha_creacion = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    correo_electronico = models.EmailField()
    celular = models.IntegerField()
    telefono_fijo = models.IntegerField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Arbol(models.Model):
    """
    Modelo que representa un árbol. Contiene información relevante
    acerca del reclamo, como la dirección donde se encuentra el árbol,
    coordenadas GPS, especie de árbol y altura del mismo.
    """
    fecha_creacion = models.DateField(auto_now_add=True)
    calle = models.CharField(max_length=50)
    numeracion = models.IntegerField()
    entre_calle_1 = models.CharField(max_length=50)
    entre_calle_2 = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    edificio = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    especie = models.CharField(max_length=50)
    altura = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"Especie {self.especie} [lat {self.latitud}, lng {self.longitud}]"


class Reclamo(models.Model):
    """
    Modelo que representa un reclamo realizado por un denunciante.
    Contiene información relevante acerca del reclamo,
    como su número de identificación, medio por el cual fue realizado,
    fuente del reclamo, fecha en que se realizó, datos del denunciante,
    datos del árbol afectado, tipo del reclamo, grado de urgencia,
    una foto del incidente (opcional), y un detalle del mismo.
    """
    fecha_creacion = models.DateField(auto_now_add=True)
    numero = models.IntegerField()
    medio = models.CharField(max_length=50)
    fuente_id = models.ForeignKey(Fuente, on_delete=models.CASCADE)
    fecha = models.DateField()
    denunciante_id = models.ManyToManyField(Denunciante)
    arbol_id = models.ManyToManyField(Arbol)
    reclamo = models.CharField(max_length=200)
    urgencia = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='img_reclamos') # img_reclamos define la ruta donde se almacenan las fotos
    detalle = models.CharField(max_length=500)

    def __str__(self):
        return f'Reclamo {self.numero}'
