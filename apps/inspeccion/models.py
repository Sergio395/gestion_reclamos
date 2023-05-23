from django.db import models

 

# Create your models here.
class Arbol(models.Model):
    """
    Modelo que representa un árbol. Contiene información relevante
    acerca del reclamo, como la dirección donde se encuentra el árbol,
    coordenadas GPS, especie de árbol y altura del mismo. Este model carga informacion desde la app relevamiento de arbolado.
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
    
    
    
class inspeccion(models.Model):
    """
    Modelo que representa una inspeccion. Contiene información sobre la inspeccion realizada y se ejecuta una por arbol
    la misma esta vinculada con la tabla arbol. En esta instacia se dividide el reclamo en diferentes arboles.
  
 
 
    """
    """
    UrgenciaChoices = (('BLANK ' , ' '), ('BAJA','BAJA'),('MEDIA','MEDIA'),('ALTA','ALTA'))
    
    
    
    
    
    
    
              
    no_requiere_inspeccion 	=  models.BooleanField(default=False)           
    fecha_de_inspeccion	=  models.DateField(auto_now_add=False, verbose_name="Fecha de inspeccion")
    
    # trabajo_a_realizar	=  models.CharField (max_length=5, verbose_name="Urgencia", choices=TrabajoChoices.choices,
                                            # default=TrabajoChoices.BLANK) 
       
    especie_altura	= models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Especie_altura")
    dap = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Dap")
    cableado_cercano = models.CharField(max_length=50, verbose_name="Cableado_cercano")
    construccion_cercana = models.CharField(max_length=50, verbose_name="Construccion_cercana")	
    observaciones_sitio= models.CharField(max_length=50, verbose_name="Observaciones")	
    urgencia_trabajo = models.CharField (max_length=5, verbose_name="Urgencia", choices=UrgenciaChoices.choices,
                                        default=UrgenciaChoices.BLANK) 
    justificacion = models.CharField(max_length=50, verbose_name="Justificacion")	
    inspector = models.OneToOneField("Usuarios", verbose_name=("inspector"), on_delete=models.CASCADE) 	
    fecha_carga_inspeccion=	models.DateField(auto_now_add=False, verbose_name="Fecha_carga_inspeccion")
    codigo_trabajo = models.CharField(max_length=50, verbose_name="Codigo_trabajo")



    def __str__(self):
        return f"{self.especie} [lat {self.latitud}, lng {self.longitud}]
    
    """