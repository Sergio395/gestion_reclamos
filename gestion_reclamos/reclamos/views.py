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

lista=['Carlos','Garcia', 30333256, 15995687,42974589, 'pepe@nocorreo.com']
lista2 = ['Arbol caido = 1', 'Arbol enfermo = 2', 'Arbol poda = 5', 'Arbol no identificado = 2']
# lista2 = []

def seguimiento(request):
    fechaActual= datetime.datetime.now()
    nombre= lista[0] + " " + lista[1]
    return render(request, 'reclamos/seguimiento.html', {'fechaActual': fechaActual, 'nombre': nombre, 'lista2': lista2, 'lista':lista})


def seguimiento_reclamo(request, nro_reclamo):
    return render(request, 'reclamos/ver_reclamo.html', {'lista2': lista2[nro_reclamo-1], 'nro': nro_reclamo,'lista':lista})
