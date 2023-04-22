from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader

from inspeccion.forms import ContactoForm

from datetime import datetime


# Create your views here.

def inspector (request):
    mensaje = None
    if (request.method == 'POST'):
        contacto_form = ContactoForm(request.POST)
        mensaje = 'Hemos recibido tus datos'
        # acción para tomar los datos del formulario
    elif request.method == 'GET':
        contacto_form = ContactoForm()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    # listado_cursos = [
    #     {
    #         'nombre': 'Fullstack Java',
    #         'descripcion': 'Curso de Fullstack',
    #         'categoria': 'Programación',
    #     },
    #     {
    #         'nombre': 'Diseño UX/UI',
    #         'descripcion': '🖌🎨',
    #         'categoria': 'Diseño',
    #     },
    #     {
    #         'nombre': 'Big Data',
    #         'descripcion': 'test',
    #         'categoria': 'Análisis de Datos',
    #     },
    #     {
    #         'nombre': 'Big Data Avanzado',
    #         'descripcion': 'test',
    #         'categoria': 'Análisis de Datos',
    #     },
    # ]

    context = {
        # 'cursos': listado_cursos,
        'mensaje': mensaje,
        'contacto_form': contacto_form
    }
    return render(request, 'inspeccion/index.html', context)