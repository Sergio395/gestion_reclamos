from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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



