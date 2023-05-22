from django.db import models
from django.utils.translation import gettext_lazy as _
# from ..inspeccion.models import Arbol
from ..reclamos.models import Reclamo

# Create your models here.
class Gestion(models.Model):
    """
    Modelo para la tabla gestion
    """
    class EstadosChoices(models.TextChoices):
        """
        Clase que representa las opciones de estados de un reclamo.
        Las opciones son limitadas y predefinidas, y se utilizan para
        restringir los valores permitidos en el campo 'estados' del modelo
        Gestion.
        """
        BLANK = "", _("")
        EA = "EA", _("Estado A")
        EB = "EB", _("Estado B")
        EC = "EC", _("Estado C")
        ED = "ED", _("Estado D")

    estado = models.CharField(max_length=30, 
                              verbose_name="Estado", 
                              choices=EstadosChoices.choices,
                              default=EstadosChoices.BLANK)
    gestion = models.CharField(max_length=30, 
                               verbose_name="Gestión")
    detalle_gestion = models.CharField(max_length=250,
                                       verbose_name="Detalle de gestión")
    equipo_trabajo = models.CharField(max_length=30, 
                                      verbose_name="Equipo de trabajo")
    fecha_programada = models.DateField(auto_now_add=True, 
                                        verbose_name="Fecha programada")
    fecha_solucion = models.DateField(auto_now_add=True, 
                                      verbose_name="Fecha de solución")
    orden_trabajo = models.CharField(max_length=30, 
                                      verbose_name="Orden de trabajo")
    # arbol = models.ForeignKey(Arbol, on_delete=models.CASCADE)
    reclamo = models.ManyToManyField(Reclamo, verbose_name="Reclamo")
    borrado = models.BooleanField(verbose_name="Borrado lógico",
                                  null=False, 
                                  blank=False, 
                                  default=False)


    def __str__(self):
        return f"{self.gestion} => {self.fecha_programada}, {self.fecha_solucion}"

    class Meta:
        abstract = False
    


# class Usuario(models.Model):
#     """
#     Modelo base para usuarios.
#     """
#     fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
#     nombre = models.CharField(max_length=30, verbose_name="Nombre")
#     apellido = models.CharField(max_length=30, verbose_name="Apellido")
#     usuario = models.CharField(max_length=15, verbose_name="Usuario")
#     correo_electronico = models.EmailField(verbose_name="Correo electrónico")
#     clave = models.CharField(max_length=20, verbose_name="Clave")

#     def __str__(self):
#         return f"{self.usuario} => {self.apellido}, {self.nombre}"

#     class Meta:
#         abstract = True


# class Operador(Usuario):
#     """
#     Modelo para operadores, que hereda del modelo Usuario.
#     """
#     def cargar_reclamo(self):
#         """
#         Método para cargar reclamo.
#         """
#         pass

#     def seguir_reclamo(self):
#         """
#         Método para seguir reclamo.
#         """
#         pass


# class Inspector(Usuario):
#     """
#     Modelo para inspectores, que hereda del modelo Usuario.
#     """
#     def cargar_reclamo(self):
#         """
#         Método para cargar reclamo.
#         """
#         pass

#     def inspeccionar_reclamo(self):
#         """
#         Método para inspeccionar reclamo.
#         """
#         pass


# class Gestor(Usuario):
#     """
#     Modelo para gestores, que hereda del modelo Usuario.
#     """
#     def gestionar_reclamo(self):
#         """
#         Método para gestionar reclamo.
#         """
#         pass


# class Administrador(Usuario):
#     """
#     Modelo para administradores, que hereda del modelo Usuario.
#     """
#     def administrar_reclamo(self):
#         """
#         Método para administrar reclamo.
#         """
#         pass

#     def administrar_usuario(self):
#         """
#         Método para administrar usuario.
#         """
#         pass
