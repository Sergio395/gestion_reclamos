from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
# Create your views here.

def index(request):
    return render(request, 'reclamos/index.html', {})

def base(request):
    return render(request, 'reclamos/base.html', {})

def principal(request):
    return render(request, 'reclamos/principal.html', {})

def carga_reclamo(request):
    return render(request, 'reclamos/carga_reclamo.html', {})

def carga_inspeccion(request):
    return render(request, 'reclamos/carga_inspecciones.html', {})

def carga_certificado(request):
    return render(request, 'reclamos/carga_certificaciones.html', {})


def seguimiento(request):
    fechaActual= datetime.datetime.now()
    nombre= "Area geográfica norte"
    lista = ['Arbol caido = 1', 'Arbol enfermo=2', 'Arbol poda=5', 'Arbol no identificado=2']
    return render(request,'reclamos/seguimiento.html',{'fechaActual': fechaActual, 'nombre': nombre, 'lista':lista})