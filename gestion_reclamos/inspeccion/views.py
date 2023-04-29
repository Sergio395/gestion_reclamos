from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader
from inspeccion.forms import ContactoForm, NuevaInspeccion,  NuevaCertificacion
from datetime import datetime
from django.contrib import messages

def inspeccion (request):
    #mensaje = None
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        #mensaje = 'Hemos recibido tus datos'
        if contacto_form.is_valid():
            messages.success(request, "Tus datos son válidos")
           
        else:
            messages.error(request, "Completar el formulario nuevamente, hay errores")
      
    # acción para tomar los datos del formulario
    elif request.method == 'GET':
        contacto_form = ContactoForm()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    context = {
        'messages': messages,
        'contacto_form': contacto_form
    }

    return render(request, 'inspeccion/inspeccion_index.html', context)


def carga_inspeccion(request):
    mensaje = None
    if request.method == 'POST':
        nueva_inspeccion = NuevaInspeccion(request.POST)
        mensaje = 'Hemos recibido tus datos'
        # acción para tomar los datos del formulario
    elif request.method == 'GET':
        nueva_inspeccion = NuevaInspeccion()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    context = {
        # 'cursos': listado_cursos,
        'mensaje': mensaje,
        'nueva_inspeccion': nueva_inspeccion
    }

    return render(request, 'inspeccion/nueva_inspeccion.html', context)


def carga_certificacion(request):
    
    mensaje = None
    if request.method == 'POST':
        nueva_certificacion = NuevaCertificacion(request.POST)
        mensaje = 'Hemos recibido tus datos'
        # acción para tomar los datos del formulario
    elif request.method == 'GET':
        nueva_certificacion = NuevaCertificacion()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    context = {
        # 'cursos': listado_cursos,
        'mensaje': mensaje,
        'nueva_certificacion':nueva_certificacion
    }

    return render(request, 'inspeccion/nueva_certificacion.html', context)
