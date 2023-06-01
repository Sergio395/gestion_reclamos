# from datetime import datetime
# from django.contrib import messages
# from django.forms import ValidationError
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render,redirect
from django.http import HttpResponseNotAllowed
from .forms import ContactoForm, NuevaInspeccion, NuevaCertificacion
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import inspecciones
from django.shortcuts import get_object_or_404
from django.contrib import messages
from apps.reclamos.models import Reclamo 
from apps.reclamos.forms import NuevoReclamo 




def inspeccion(request):
    mensaje = None
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        mensaje = 'Tus datos están Ok'
    # acción para tomar los datos del formulario
    elif request.method == 'GET':
        contacto_form = ContactoForm()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    context = {
        'mensaje': mensaje,
        'contacto_form': contacto_form
    }

    return render(request, 'inspeccion/inspeccion_index.html', context)



#-------------------------------------------CRUD inspecciones---------------------------------------------------------------
 
class InspeccionListView(ListView):
    model = inspecciones
    context_object_name = 'inspeccion'
    template_name = 'inspeccion/inspeccion_listar.html'
    queryset = inspecciones.objects.filter(eliminado=False).order_by('reclamo') # cuando cargo la inspeccion ya cuento con numero de reclamo. No necesito filtar ni ordenar

class InspeccionesCreateView(CreateView):
    model = inspecciones
    form_class = NuevaInspeccion
    template_name = 'inspeccion/nueva_inspeccion.html'
    success_url = reverse_lazy('inspeccion')
    
class InspeccionesUpdateView(UpdateView):
    model = inspecciones
    #fields = '__all__'    
    #exclude=['eliminado']
    
    form_class = NuevaInspeccion
    template_name = 'inspeccion/inspeccion_editar.html'
    success_url = reverse_lazy('inspeccion')
    #Si queremos sobrescribir la obtención del objeto
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(inspecciones, pk=pk)
        return obj
           
        
def delete_inspeccion(request, pk):
    try:
        inspeccion = inspecciones.objects.get(pk=pk)
    except inspecciones.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    inspeccion.soft_delete()
    messages.warning(request, 'Se ha eliminado  el registro correctamente')
    return redirect('inspeccion')


def mostrar_reclamo(request, pk):
    
    try:
        reclamo = Reclamo.objects.get(id=pk)
    except Reclamo.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    return render(request, 'inspeccion/inspeccion_mostrar.html', {'form': reclamo})


def grabar_numero(request, pk):
    # busco los codigos de trabajo que existan en la bbdd que coinciden con el numero de raclamo quee estoy cargando
    lista_codigos = list(inspecciones.objects.filter(reclamo_id=pk))
    valor = lista_codigos
    
   
    #reclamo=lista_codigos.numeros
        
    #obtengo el codigo de trabajo con ams alta repitancia en la lista codigo de trabajos y le sumo uno.
    # for codigo in lista_codigos:    
        # valor=codigo[1]
        # for i in valor:
            # reclamo = i
    return render(request, 'inspeccion/ver.html', {'valor': valor})
                    
        
    

#------------------------------------------------------------------------------------------------------------------------------





#-------------------------------------------CRUD certificacion---------------------------------------------------------------

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
        'nueva_certificacion': nueva_certificacion
    }

    return render(request, 'inspeccion/nueva_certificacion.html', context)

#------------------------------------------------------------------------------------------------------------------------------