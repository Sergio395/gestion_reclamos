import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from reclamos.forms import NuevoReclamo
import datetime







# Create your views here.
def index(request):
    tag="pagina_index"
    return render(request, 'index.html', {'tag': tag})



# Nuevo Reclamo---------------------------------------------------

def nuevo_reclamo(request):
    mensaje = None
    if request.method == 'POST':
        nuevo_reclamo = NuevoReclamo(request.POST)
        mensaje = 'Hemos recibido tus datos'
        # acción para tomar los datos del formulario
    elif request.method == 'GET':
        nuevo_reclamo = NuevoReclamo()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    context = {
        'mensaje': mensaje,
        'nuevo_reclamo': nuevo_reclamo
    }

    return render(request, 'reclamos/nuevo_reclamo.html', context)




# Fin Nuevo Reclamo-----------------------------------------------



lista = ['Area Geográfica', 'Norte', 30333256, 15995687, 42974589, 'pepe@nocorreo.com']
lista2 = ['Arbol caido = 1', 'Arbol enfermo = 2', 'Arbol poda = 5', 'Arbol no identificado = 2']
# lista2 = []


def seguimiento(request):
    fecha_actual = datetime.datetime.now()
    nombre = lista[0] + " " + lista[1]
    return render(request, 'reclamos/seguimiento.html', {
        'fechaActual': fecha_actual,
        'nombre': nombre,
        'lista2': lista2,
        'lista': lista
    })


def seguimiento_reclamo(request, nro_reclamo):
    return render(request, 'reclamos/ver_reclamo.html', {
        'lista2': lista2[nro_reclamo-1],
        'nro': nro_reclamo,
        'lista': lista
    })
