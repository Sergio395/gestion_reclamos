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
    permiso = models.CharField(max_length=20, verbose_name="Permiso")

    def __str__(self):
        return f"{self.usuario} => {self.apellido}, {self.nombre}"

    class Meta:
        abstract = True
        
        

class Empresa(models.Model):
    """
    Modelo base para empresas.
    """


    fecha_alta = models.DateField(auto_now_add=True, verbose_name="Fecha_alta")
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    razon_social = models.CharField(max_length=30, verbose_name="Razon_social")
    num_proveedor = models.IntegerField(max_length=15, verbose_name="Num_proveedor")
    cuit = models.IntegerField(verbose_name="Cuit")
    correo = models.EmailField(max_length=20, verbose_name="Correo_Electronico")
    telefono = models.CharField(max_length=20, verbose_name="Telefono")

    def __str__(self):
        return f"{self.razon_social} => {self.num_proveedor}"

    class Meta:
        abstract = False
        
        
class OrdenCompra(models.Model):
    """
    Modelo base para ordenes de compras.
    """


    fecha_emision = models.DateField(auto_now_add=True, verbose_name="Fecha_emision")
    empresa = models.CharField(max_length=30, verbose_name="Empresa")
    numero = models.IntegerField(max_length=20, verbose_name="Numero")
    cantidad = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Cantidad")
    descripcion = models.TextField(verbose_name="Descripcion")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Precio_unitario")
    monto = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Monto")
    certificacion_cant = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Certificacion_cantidad")
    certificacion_monto = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="CErtificacion_monto")
    saldo_cant = models.DecimalField(max_digits=7, decimal_places=2,verbose_name="Saldo_cantidad")
    saldo_monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Saldo_monto")
    

    def __str__(self):
        return f"{self.empresa} => {self.numero}"

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
