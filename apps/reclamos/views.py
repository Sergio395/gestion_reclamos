from datetime import datetime
from django.shortcuts import render, redirect
# from django.views import View
from .forms import NuevoReclamo
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed




# PARA IMPLEMENTAR
# from django.views.generic.edit import FormView
# from .forms import NuevoReclamoForm

# class NuevoReclamoView(FormView):
#     template_name = 'reclamos/nuevo_reclamo.html'
#     form_class = NuevoReclamoForm
#     success_url = '/reclamos/gracias/'

#     def form_valid(self, form):
#         # Lógica para guardar el formulario en la base de datos
#         return super().form_valid(form)
#  fin


# class NuevoReclamoView(View):
#     template_name = 'reclamos/nuevo_reclamo.html'

#     def get(self, request, *args, **kwargs):
#         nuevo = NuevoReclamo()
#         context = {
#             'nuevo_reclamo': nuevo,
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         nuevo = NuevoReclamo(request.POST)
#         if nuevo.is_valid():
#             mensaje = 'Hemos recibido tus datos'
#             # acción para tomar los datos del formulario
#             return redirect('ruta_de_redireccion')
#         else:
#             mensaje = 'Ha ocurrido un error, por favor verifica los datos ingresados.'
#         context = {
#             'mensaje': mensaje,
#             'nuevo_reclamo': nuevo,
#         }
#         return render(request, self.template_name, context)




# Create your views here.
def nuevo_reclamo(request):
    mensaje = None
    if request.method == 'POST':
        nuevo = NuevoReclamo(request.POST)
        mensaje = 'Hemos recibido tus datos'
        # acción para tomar los datos del formulario
    elif request.method == 'GET':
        nuevo = NuevoReclamo()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    context = {
        'mensaje': mensaje,
        'nuevo_reclamo': nuevo
    }

    return render(request, 'reclamos/nuevo_reclamo.html', context)
# Fin Nuevo Reclamo-----------------------------------------------


lista = ['Area Geográfica', 'Norte', 30333256,
         15995687, 42974589, 'pepe@nocorreo.com']
lista2 = ['Arbol caido = 1', 'Arbol enfermo = 2',
          'Arbol poda = 5', 'Arbol no identificado = 2']
# lista2 = []


def seguimiento(request):
    fecha_actual = datetime.now()
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
