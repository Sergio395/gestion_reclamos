from django.db import models

# Create your models here.
class Inspeccion(models.Model):
    
    
    reclamo = models.CharField(max_length=100, verbose_name="Reclamo")
    inspector = models.CharField(max_length=25, verbose_name="Apellido")
    nota = models.CharField(max_length=300, verbose_name="nota")
    foto = models.ImageField(upload_to='img_reclamos', null=True, blank=True, verbose_name="Fotos")
    
    def __str__(self):
        return f'Reclamo {self.numero}'