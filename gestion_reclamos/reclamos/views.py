import datetime
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def nuevo_reclamo(request):
    return render(request, 'reclamos/nuevo_reclamo.html', {})


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
