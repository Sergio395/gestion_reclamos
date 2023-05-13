from django.db import models

from django.db import models


# Create your models here.
class Usuario(models.Model):
    """
    Modelo base para usuarios.
    """
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    usuario = models.CharField(max_length=15, verbose_name="Usuario")
    correo_electronico = models.EmailField(verbose_name="Correo electrónico")
    clave = models.CharField(max_length=20, verbose_name="Clave")

    def __str__(self):
        return f"{self.usuario} => {self.apellido}, {self.nombre}"

    class Meta:
        abstract = True


class Operador(Usuario):
    """
    Modelo para operadores, que hereda del modelo Usuario.
    """
    def cargar_reclamo(self):
        """
        Método para cargar reclamo.
        """
        pass

    def seguir_reclamo(self):
        """
        Método para seguir reclamo.
        """
        pass


class Inspector(Usuario):
    """
    Modelo para inspectores, que hereda del modelo Usuario.
    """
    def cargar_reclamo(self):
        """
        Método para cargar reclamo.
        """
        pass

    def inspeccionar_reclamo(self):
        """
        Método para inspeccionar reclamo.
        """
        pass


class Gestor(Usuario):
    """
    Modelo para gestores, que hereda del modelo Usuario.
    """
    def gestionar_reclamo(self):
        """
        Método para gestionar reclamo.
        """
        pass


class Administrador(Usuario):
    """
    Modelo para administradores, que hereda del modelo Usuario.
    """
    def administrar_reclamo(self):
        """
        Método para administrar reclamo.
        """
        pass

    def administrar_usuario(self):
        """
        Método para administrar usuario.
        """
        pass
