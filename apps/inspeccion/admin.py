from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Inspeccion)
class InspeccionAdmin(admin.ModelAdmin):
    list_display = ('reclamo','inspector',
                    'lugar','fecha_inspeccion','trabajo')


@admin.register(Arbol)
class ArbolAdmin(admin.ModelAdmin):
    list_display = ('inspeccion','urgencia')
    
