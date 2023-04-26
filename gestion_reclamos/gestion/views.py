from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader
from gestion.forms import GestionForm
from datetime import datetime


# Create your views here.
def gestion_manejo_formulario (request):
    mensaje = None

    if request.method == 'POST':
        gestion_form = GestionForm(request.POST)
        mensaje = 'Hemos recibido tus datos'
    # acción para tomar los datos del formulario
    elif request.method == 'GET':
        gestion_form = GestionForm()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    context = {
        # 'cursos': listado_cursos,
        'mensaje': mensaje,
        'gestion_form': gestion_form
    }

    return render(request, 'gestion/gestion_index.html', context)
