from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from .forms import GestionForm, BusquedaForm
from .models import GestionModel

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.inspeccion.models import inspecciones

# Create your views here.    
def gestion_index(request):
    '''
    Por ahora trae los valores de la tabla Gestion, pero deberiamos definir en grupo que datos va a mostrar 
    Muestra un formulario de busqueda para utilizar como filtro
    Trae los reclamos y los muestra en una tabla
    '''
    form_busqueda = BusquedaForm(request.POST or None)
    try:
        gestion = GestionModel.objects.filter(baja=False)
    except GestionModel.DoesNotExist:
        return render(request, 'gestion/gestion_prueba.html')
    try:
        fields = GestionModel.objects.model._meta.get_fields()
    except GestionModel.DoesNotExist:
        return render(request, 'gestion/gestion_prueba.html')
    return render(request, 'gestion/gestion_prueba.html', {'gestion': gestion, 'form_busqueda': form_busqueda, 'campos': fields})

def gestion_buscar(request):
    '''
    Tomar los valores del formulario busqueda, y va a realizar la consulta a la DB, para traer y mostrar los resultados
    '''
    formulario = BusquedaForm(request.POST or None) # hay que pasarle instancia?
    if formulario.is_valid():
        try:
            filtro = preparar_filtro(formulario.cleaned_data)
            gestion = GestionModel.objects.filter(**filtro)
        except GestionModel.DoesNotExist:
            return render(request, 'gestion/gestion_prueba.html')
    else:
        messages.warning(request, 'Revisa los campos')
        return render(request, 'gestion/gestion_prueba.html')
    
    fields = GestionModel.objects.model._meta.get_fields()
    return render(request, 'gestion/gestion_prueba.html', {'gestion': gestion, 'form_busqueda': formulario, 'campos': fields})

def gestion_nuevo(request):
    # forma de resumida de instanciar un formulario basado en model con los
    # datos recibidos por POST si la petición es por POST o bien vacio(None)
    # Si la petición es por GET
    titulo_accion = 'Creación de registro'
    formulario = GestionForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Se ha creado el .... correctamente')
        return redirect('gestion_index')
    return render(request, 'gestion/gestion_nuevo.html', {'gestion_form': formulario, 'accion': titulo_accion})

def gestion_editar(request, id):
    titulo_accion = 'Edición de registro'
    try:
        gestion = GestionModel.objects.get(pk=id)
    except GestionModel.DoesNotExist:
        return render(request, 'gestion/gestion_prueba.html')
    formulario = GestionForm(request.POST or None, instance=gestion)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Se ha editado el campo correctamente')
        return redirect('gestion_index')
    return render(request, 'gestion/gestion_editar.html', {'gestion_form': formulario, 'accion':titulo_accion, 'id':id})

def gestion_eliminar(request, id_registro):
    try:
        gestion = GestionModel.objects.get(id=id_registro)
    except GestionModel.DoesNotExist:
        return render(request, 'gestion/gestion_prueba.html')
    messages.success(request, 'Se ha eliminado el curso correctamente')
    gestion.soft_delete()
    return redirect('gestion_index')

def preparar_filtro(criterio):
    '''
    Recibe los criterios y compaa si son distintos de 'none', y los agrega al diccionario que luego se pasará como filtro por los parametros **kwargs
    ejemplo:
    your_filters = {
    'field_1__exact': value_1,
    'field_2__gte': value_2,
    }

    Model.objects.filter(**your_filters)
    '''
    filtro = {'baja':False}
    
    if criterio['criterio1_campo'] != 'none':
        filtro[criterio['criterio1_campo']] = criterio['criterio1_valor']
    if criterio['criterio2_campo'] != 'none':
        filtro[criterio['criterio2_campo']] = criterio['criterio2_valor']
    if criterio['criterio3_campo'] != 'none':
        filtro[criterio['criterio3_campo']] = criterio['criterio3_valor']
    if criterio['criterio4_campo'] != 'none':
        filtro[criterio['criterio4_campo']] = criterio['criterio4_valor'].strftime('%Y-%m-%d')
    return filtro

# Lo mismo pero con VBC
#---------------------------

class GestionListView(ListView):
    model = inspecciones
    context_object_name = 'Inspecciones'
    template_name = 'gestion/gestion_lista.html'
    queryset = inspecciones.objects.filter(eliminado=False)
    ordering = ['arbol_id']
    
    def get_context_data(self, **kwargs):
        '''
        Agrego informacion al contexto
        '''
        context = super(GestionListView, self).get_context_data(**kwargs)
        context['form_busqueda'] = BusquedaForm()
        return context

#  mod_date = models.DateField(default=date.today)
# ---- Así funcionaba con listas ----

# def gestion_inicio (request):
#     mensaje = None
#     if request.method == 'POST':
#         form_busqueda = GesBusqueda(request.POST)
        
#         # acción para tomar los datos del formulario
#         if form_busqueda.is_valid():
#             messages.success(request, 'Hemos recibido tus datos')
#             resultado = buscar_en_lista(lista_reclamos, form_busqueda.cleaned_data)
#             reclamos = resultado
#         # acción para tomar los datos del formulario
#         else:
#             messages.error(
#                 request, 'Por favor revisa los errores en el formulario')
            
#     elif request.method == 'GET':
#         form_busqueda = GesBusqueda()
#         reclamos = lista_reclamos
#     else:
#         return HttpResponseNotAllowed(f"Método {request.method} no soportado")

#     context = {
#         'reclamos': reclamos,
#         'mensaje': mensaje,
#         'form_busqueda' : form_busqueda
#     }
#     return render(request, 'gestion/gestion_inicio.html', context)



# def gestion_editar_reclamo(request, nro_reclamo):
#     datos_reclamo = lista_reclamos[nro_reclamo-1]
#     mensaje = None
#     if request.method == 'POST':
#         form_contacto = GesContacto(request.POST)
#         form_inspector = GesInspector(request.POST)
#         form_inspeccion = GesInspeccion(request.POST)
#         form_gestion = GesGestion(request.POST)
#         mensaje = 'Hemos recibido tus datos'
#         # acción para tomar los datos del formulario
#     elif request.method == 'GET':
#         form_contacto = GesContacto(datos_reclamo)
#         form_inspector = GesInspector(datos_reclamo)
#         form_inspeccion = GesInspeccion(datos_reclamo)
#         form_gestion = GesGestion(datos_reclamo)
#     else:
#         return HttpResponseNotAllowed(f"Método {request.method} no soportado")

#     context = {
#         'nro_reclamo' : nro_reclamo,
#         'mensaje': mensaje,
#         'datos_reclamo': datos_reclamo,
#         'form_contacto': form_contacto,
#         'form_inspector': form_inspector,
#         'form_inspeccion': form_inspeccion,
#         'form_gestion': form_gestion,
#     }
#     return render(request, 'gestion/gestion_editar_reclamo.html', context)

# ---- buscar en lista, filtra una lista por hasta 4 criterios distintos ---

# def buscar_en_lista (lista, criterio):
#     arreglo_fecha = f'''{criterio['criterio4_valor']}'''
#     resultado1 = []
#     resultado2 = []
#     resultado3 = []
#     resultado4 = []
#     resultado_final = []
#     # print(criterio['criterio1_campo'])
#     if criterio['criterio1_campo'] != 'none':
#         for item in lista:
#             if item[criterio['criterio1_campo']] == criterio['criterio1_valor']:
#                 resultado1.append(item)
#     else:
#         resultado1 = lista

#     if criterio['criterio2_campo'] != 'none':
#         for item in resultado1:
#             if item[criterio['criterio2_campo']] == criterio['criterio2_valor']:
#                 resultado2.append(item)
#     else:
#         resultado2 = resultado1

#     if criterio['criterio3_campo'] != 'none':
#         for item in resultado2:
#             if item[criterio['criterio3_campo']] == criterio['criterio3_valor']:
#                 resultado3.append(item)
#     else:
#         resultado3 = resultado2
    
#     if criterio['criterio4_campo'] != 'none':
#         for item in resultado3:
#             if item[criterio['criterio4_campo']] == arreglo_fecha:
#                 resultado4.append(item)
#     else:
#         resultado4 = resultado3    
#     resultado_final = resultado4
#     return resultado_final
