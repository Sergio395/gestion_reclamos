from django.db import models
from .choices import lugares, reclamo, trabajos, inspectores,especies,urgencias
#import datetime
#from django.utils import timezone
# Create your models here.
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
    
