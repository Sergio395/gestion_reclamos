from django.db import models
from apps.reclamos.models import  Reclamo, Arbol
from apps.administracion.models import Usuario
 

    
class Trabajos(models.Model):
    
    """
    Modelo que contiene todos los tipos de trabajos existentes.
    """
    
    tipo_poda   = models.CharField(max_length=50, verbose_name="Tipo_poda", null=False)
    ubicacion   = models.CharField(max_length=50, verbose_name="Ubicacion", null=False)
    tipo_arbol  = models.CharField(max_length=50, verbose_name="Tipo_arbol", null=False)
    codigo      = models.CharField(max_length=50, verbose_name="Codigo", null=False)
    coeficiente = models.CharField(max_length=50, verbose_name="Coeficiente", null=False)
    descripcion = models.CharField(max_length=250, verbose_name="Descripcion", null=False)    

    def __str__(self):
         
        return f"{self.codigo} {self.descripcion}"


    
class inspecciones(models.Model):
    
    """
    Modelo que representa una inspeccion. Contiene información sobre la inspeccion realizada y se ejecuta una por arbol
    la misma esta vinculada con la tabla arbol. En esta instacia se dividide el reclamo en diferentes arboles.
  
     """
     
     
    #UrgenciaChoices = (('BLANK ' , ' '), ('BAJA','BAJA'),('MEDIA','MEDIA'),('ALTA','ALTA'))  
    no_requiere_inspeccion 	=  models.BooleanField(default=False)           
    fecha_de_inspeccion	=  models.DateField(auto_now_add=False, verbose_name="Fecha de inspeccion")
    reclamo = models.ForeignKey(Reclamo, verbose_name=("Reclamo"), on_delete=models.CASCADE)
    trabajo_a_realizar	=  models.ForeignKey(Trabajos, verbose_name=("trabajos"), on_delete=models.CASCADE)       
    especie_altura	= models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Especie_altura")
    dap = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Dap")
    cableado_cercano = models.CharField(max_length=50, verbose_name="Cableado_cercano",default="")
    construccion_cercana = models.CharField(max_length=50, verbose_name="Construccion_cercana")	
    observaciones_sitio= models.CharField(max_length=50, verbose_name="Observaciones" ,default="")	
    urgencia_trabajo = models.CharField (max_length=5, verbose_name="Urgencia", choices=Reclamo.UrgenciaChoices.choices,
                                        default=Reclamo.UrgenciaChoices.BLANK) 
    justificacion = models.CharField(max_length=50, verbose_name="Justificacion")	
    inspector = models.OneToOneField(Usuario, verbose_name=("inspector"), on_delete=models.CASCADE) 	
    fecha_carga_inspeccion=	models.DateField(auto_now_add=False, verbose_name="Fecha_carga_inspeccion")
    codigo_trabajo = models.CharField(max_length=50, verbose_name="Codigo_trabajo")
    arbol = models.ForeignKey(Arbol,verbose_name=("arbol"), on_delete=models.CASCADE)
    eliminado=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.reclamo} {self.codigo_trabajo} {self.arbol}"

    def soft_delete(self):
        self.eliminado = True
        super().save()

    def restore(self):
        self.eliminado = False
        super().save()