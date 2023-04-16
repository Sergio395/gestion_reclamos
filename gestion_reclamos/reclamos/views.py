from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
# Create your views here.

def index(request):
    return render(request, 'reclamos/index.html', {})

def principal(request):
    return render(request, 'reclamos/base.html', {})

def nuevo_reclamo(request):
    return render(request, 'reclamos/nuevo_reclamo.html', {})


def carga_inspeccion(request):
    return render(request, 'reclamos/carga_inspecciones.html', {})


def carga_certificado(request):
    return render(request, 'reclamos/carga_certificaciones.html', {})


def seguimiento(request):
    fechaActual= datetime.datetime.now()
    nombre= "Area geográfica norte"
    lista = ['Arbol caido = 1', 'Arbol enfermo = 2', 'Arbol poda = 5', 'Arbol no identificado = 2']
    return render(request, 'reclamos/seguimiento.html', {'fechaActual': fechaActual, 'nombre': nombre, 'lista': lista})


def seguimiento_reclamo(request, nro_reclamo):
    lista = ['Arbol caido = 1', 'Arbol enfermo = 2', 'Arbol poda = 5', 'Arbol no identificado = 2']
    return render(request, 'reclamos/ver_reclamo.html', {'lista': lista[nro_reclamo-1], 'nro': nro_reclamo})
