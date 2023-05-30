from django.db import models

from .choices import lugares, reclamo, trabajos, inspectores,especies,urgencias

class Inspeccion(models.Model):
        
    fecha_inspeccion = models.DateField(verbose_name='Fecha de inspección')
    reclamo = models.CharField(max_length=100, verbose_name="Reclamo a inspeccionar",choices=reclamo, default='01')
    inspector = models.CharField(max_length=100, verbose_name="Inspector",choices=inspectores,default='01')
    lugar = models.CharField(max_length=100, choices=lugares,default='ZN')
    nota = models.CharField(max_length=300, verbose_name="nota",null=False,blank=True)
    foto = models.ImageField(upload_to='img_reclamos', null=True, blank=True, verbose_name="Fotos")
    especie=models.CharField(max_length=100, verbose_name="Especie",choices=especies,default='1')
    trabajo = models.CharField(max_length=100, choices=trabajos,default='1')
    def __str__(self):
        return "{} - {}, {} // {} ".format(self.reclamo, self.inspector, self.lugar,self.fecha_inspeccion)
    
    class Meta:
        verbose_name = "Inspeccion"
        verbose_name_plural = "Inspecciones"
        db_table = "inspeccion"
        ordering = ['fecha_inspeccion','lugar', 'reclamo']
    
class Arbol(models.Model):
    
    inspeccion = models.ForeignKey(Inspeccion, null=True, blank=True, on_delete=models.CASCADE)
    
    
    urgencia=models.CharField(max_length=100,choices=urgencias,default='1')
    def __str__(self):
        texto= '{} '
        return texto.format(self.inspeccion)
    

from apps.reclamos.models import  Reclamo, Arbol
from apps.administracion.models import Usuario
 
class Especies(models.Model):
    
        
    """
    Modelo que contiene todos los tipos de especie de arboles existentes.
    """
    
    nombre_vulgar =  models.CharField(max_length=50, verbose_name="Nombre_vulgar", default="")        
    nombre_cientifico =  models.CharField(max_length=50, verbose_name="Nombre_cientifico", default="")
    nombre_completo =  models.CharField(max_length=50, verbose_name="Nombre_completo", default="")
 
    def __str__(self):
      
        return f"{self.nombre_completo}"
    
    
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
    DisposicionChoices = (('BLANK ' , ''), ('PUNTUAL','Puntual'),('LINEAL','Lineal'))  
     
    #UrgenciaChoices = (('BLANK ' , ' '), ('BAJA','BAJA'),('MEDIA','MEDIA'),('ALTA','ALTA'))  
    no_requiere_inspeccion 	=  models.BooleanField(default=False)           
    fecha_de_inspeccion	=  models.DateField(auto_now_add=False, verbose_name="Fecha de inspeccion")
    reclamo = models.ForeignKey(Reclamo, verbose_name=("Reclamo"), on_delete=models.CASCADE)
    disposicion = models.CharField(max_length=20 ,verbose_name=("Disposicion"), default="", choices=DisposicionChoices)    
    trabajo_a_realizar	=  models.ForeignKey(Trabajos, verbose_name=("trabajos"), on_delete=models.CASCADE,null=True) 
    especie=  models.ForeignKey(Especies, verbose_name=("Especie"), on_delete=models.CASCADE)       
    especie_altura	= models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Especie_altura")
    dap = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Dap")
    cableado_cercano = models.CharField(max_length=50, verbose_name="Cableado_cercano",default="", null=True)
    construccion_cercana = models.CharField(max_length=50, verbose_name="Construccion_cercana", null=True)	
    observaciones_sitio= models.CharField(max_length=50, verbose_name="Observaciones" ,default="", null=True)	
    urgencia_trabajo = models.CharField (max_length=5, verbose_name="Urgencia", choices=Reclamo.UrgenciaChoices.choices,
                                        default=Reclamo.UrgenciaChoices.BLANK) 
    justificacion = models.CharField(max_length=50, verbose_name="Justificacion")	
    inspector = models.ForeignKey(Usuario,verbose_name=("inspector"),on_delete=models.CASCADE,default="") 	
    fecha_carga_inspeccion=	models.DateField(auto_now_add=False, verbose_name="Fecha_carga_inspeccion")
    codigo_trabajo = models.CharField(max_length=50, verbose_name="Codigo_trabajo")
    arbol = models.ForeignKey(Arbol,verbose_name=("arbol"), on_delete=models.CASCADE,null=True)
    foto = models.ImageField(upload_to='img_reclamos', null=True,
                            blank=True, verbose_name="Fotos") # img_reclamos define la ruta donde se almacenan las fotos
    eliminado=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.reclamo} {self.codigo_trabajo} {self.arbol}"

    def soft_delete(self):
        self.eliminado = True
        super().save()
     

    def restore(self):
        self.eliminado = False
        super().save()

