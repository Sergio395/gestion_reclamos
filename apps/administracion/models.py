from django.db import models
from typing import Iterable, Optional
from django.contrib.auth.models import User

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
    permiso = models.CharField(max_length=20, verbose_name="Permiso")
    eliminado=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.usuario} => {self.apellido}, {self.nombre}"

    class Meta:
        abstract = True
        
        
        
        
class Empresa(models.Model):
    
    """
    Modelo base para empresas.
    """


    fecha_alta = models.DateField(verbose_name="Fecha_alta")
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    razon_social = models.CharField(max_length=30, verbose_name="Razon_social")
    num_proveedor = models.IntegerField(verbose_name="Num_proveedor")
    cuit = models.IntegerField(verbose_name="Cuit")
    correo = models.EmailField(max_length=20, verbose_name="Correo_Electronico")
    telefono = models.CharField(max_length=20, verbose_name="Telefono")
    orden_compra = models.IntegerField(verbose_name="OC", null=True)
    eliminado=models.BooleanField(default=0)
    
    def __str__(self):
        return f"{self.razon_social} - {self.orden_compra}"
    
    def soft_delete(self):
        self.eliminado = True
        super().save()
        
    def restore(self):
        self.eliminado = False
        super().save()

    # class Meta:
        # abstract = False
        
        

class OrdenCompra(models.Model):
    """
    Modelo base para ordenes de compras.
       
    """

    fecha_emision = models.DateField(auto_now_add=True, verbose_name="Fecha_emision")
    empresa = models.OneToOneField(Empresa,  on_delete=models.CASCADE,verbose_name="Empresa", primary_key=True)
    numero = models.IntegerField(verbose_name="Numero")
    cantidad = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Cantidad")
    descripcion = models.TextField(verbose_name="Descripcion")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Precio_unitario")
    monto = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Monto")
    certificacion_cant = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Certificacion_cantidad")
    certificacion_monto = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="CErtificacion_monto")
    saldo_cant = models.DecimalField(max_digits=7, decimal_places=2,verbose_name="Saldo_cantidad")
    saldo_monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Saldo_monto")
    eliminado=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.numero}"
    
    def soft_delete(self):
        self.eliminado = True
        super().save()

    def restore(self):
        self.eliminado = False
        super().save()
        
        # class Meta:
        # abstract = False
        
class Cuadrante(models.Model):
    
    """
    Modelo base para cuadrantes.
    """


    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    punto1_lat  = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Punto_1_latitud")
    punto1_long = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Punto_1_longitud")
    punto2_lat  = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Punto_2_latitud")
    punto2_long = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Punto_2_longitud")
    punto3_lat  = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Punto_3_latitud")
    punto3_long = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Punto_3_longitud")
    punto4_lat  = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Punto_4_latitud")
    punto4_long = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Punto_4_longitud")
    eliminado=models.BooleanField(default=False)
    
    def __str__(self):
        
        return f"{self.nombre}"

    class Meta:
        abstract = False



















# class Operador(Usuario):
    # """
    # Modelo para operadores, que hereda del modelo Usuario.
    # """
    # def cargar_reclamo(self):
        # """
        # Método para cargar reclamo.
        # """
        # pass

    # def seguir_reclamo(self):
        # """
        # Método para seguir reclamo.
        # """
        # pass


# class Inspector(Usuario):
    # """
    # Modelo para inspectores, que hereda del modelo Usuario.
    # """
    # def cargar_reclamo(self):
        # """
        # Método para cargar reclamo.
        # """
        # pass

    # def inspeccionar_reclamo(self):
        # """
        # Método para inspeccionar reclamo.
        # """
        # pass


# class Gestor(Usuario):
    # """
    # Modelo para gestores, que hereda del modelo Usuario.
    # """
    # def gestionar_reclamo(self):
        # """
        # Método para gestionar reclamo.
        # """
        # pass


# class Administrador(Usuario):
    # """
    # Modelo para administradores, que hereda del modelo Usuario.
    # """
    # def administrar_reclamo(self):
        # """
        # Método para administrar reclamo.
        # """
        # pass

    # def administrar_usuario(self):
        # """
        # Método para administrar usuario.
        # """
        # pass
