# from datetime import datetime
# from django.contrib import messages
# from django.forms import ValidationError
from django.http import HttpResponse
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
from apps.reclamos.models import ReclamoModel 
from apps.reclamos.forms import ReclamoForm 
 


# def db_inspeccion(request):
#     inspeccionesRealizadas = Inspeccion.objects.all()
#     return render (request, 'inspeccion/inspecciones.html',{'inspecciones':inspeccionesRealizadas  })
    
 

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
    queryset = inspecciones.objects.filter(eliminado=False)
    #ordering = ['numero']

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
        reclamo = ReclamoModel.objects.get(id=pk)
    except ReclamoModel.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    #formulario = ReclamoForm(request.POST or None, request.FILES or None, instance=reclamo)
    


    return render(request, 'inspeccion/inspeccion_mostrar.html', {'form': reclamo})
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    





















   
   
   
   
   
   
   
   
 
    
    # class InspeccionesDeleteView(DeleteView):
    
        # model = inspecciones
        # template_name = 'inspeccion/inspeccion_listar.html'
        # success_url = reverse_lazy('inspeccion')

        # # se puede sobreescribir el metodo delete por defecto de la VBC, para que no se realice una baja fisica
        # def delete(self, request, *args, **kwargs):
            # self.object = self.get_object()
            # self.object.soft_delete()  # Llamada al método soft_delete() del modelo
            # return HttpResponseRedirect(self.get_success_url())

    
    
    
    
    
#------------------------------------------------------------------------------------------------------------------------------





















# def carga_inspeccion(request):
    # mensaje = None
    # if request.method == 'POST':
        # nueva_inspeccion = NuevaInspeccion(request.POST)
        # mensaje = 'Hemos recibido tus datos'
        # # acción para tomar los datos del formulario
    # elif request.method == 'GET':
        # nueva_inspeccion = NuevaInspeccion()
    # else:
        # return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    # context = {
        # # 'cursos': listado_cursos,
        # 'mensaje': mensaje,
        # 'nueva_inspeccion': nueva_inspeccion
    # }

    # return render(request, 'inspeccion/nueva_inspeccion.html', context)


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



# class InspeccionListView(ListView):
#     model = Inspeccion
#     template_name = 'inspeccion/gestion_inspecciones.html'