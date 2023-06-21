# from datetime import datetime
# from django.contrib import messages
# from django.forms import ValidationError
from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render,redirect
from django.http import HttpResponseNotAllowed
from .forms import ContactoForm, NuevaInspeccion
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import inspecciones, Especies,Usuario, Trabajos
from django.shortcuts import get_object_or_404
from django.contrib import messages
from apps.reclamos.models import ReclamoModel 
from apps.reclamos.forms import ReclamoForm 
from django.contrib.auth import mixins
from django.contrib.auth.decorators import login_required
from django.db.models.signals import pre_save
from django.dispatch import receiver
 

@login_required
def db_inspeccion(request):
    inspeccionesRealizadas = inspecciones.objects.all()
    return render (request, 'inspeccion/inspecciones.html',{'inspecciones':inspeccionesRealizadas  })

@login_required    
def carga_inspeccion(request):
    inspeccionesRealizadas = inspecciones.objects.all()
    return render (request, 'inspeccion/inspecciones.html',{'inspecciones':inspeccionesRealizadas  })
    
@login_required
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


class InspeccionListView(mixins.LoginRequiredMixin, ListView):
    model = inspecciones
    context_object_name = 'inspeccion'
    template_name = 'inspeccion/inspeccion_listar.html'
    queryset = inspecciones.objects.filter(eliminado=False)
    ordering = ['codigo_trabajo']
    
    def get_context_data(self, **kwargs):
        """Obtiene los datos del contexto para la vista.
        Retorna el contexto actualizado con las relaciones inspeccion-especie e inspeccion-inspector.
        """
        
        context = super().get_context_data(**kwargs)
        inspecciones = self.get_queryset()
        relaciones = []
        for inspeccion in inspecciones:

            arbol = Especies.objects.get(pk=inspeccion.especie_id).nombre_vulgar
            inspector = Usuario.objects.get(pk=inspeccion.inspector_id)
            trabajo = Trabajos.objects.get(pk=inspeccion.trabajo_a_realizar_id).codigo
            num_reclamo = ReclamoModel.objects.get(pk=inspeccion.reclamo_id).numero

            relacion = {
                'inspeccion': inspeccion,
                'arbol': arbol,
                'inspector': inspector,
                'trabajo' : trabajo,
                'num_reclamo' : num_reclamo,            
                
                }
            relaciones.append(relacion)
        context['relaciones'] = relaciones
        return context
        

class InspeccionesCreateView(mixins.LoginRequiredMixin, CreateView):
    model = inspecciones
    form_class = NuevaInspeccion
    template_name = 'inspeccion/nueva_inspeccion.html'
    success_url = reverse_lazy('inspeccion')
    
    
@receiver(pre_save, sender=inspecciones)
def actualizar_repitancia(sender, instance, **kwargs):
    
    """Actualiza el campo 'repitancia' de un reclamo antes de guardarlo. Ademas asigna el codigo_trabajo a la inspeccion

    Esta función es utilizada como receptor (signal receiver) del evento 'pre_save' del modelo 'inspecciones'. Se ejecuta antes de que un reclamo sea guardado en la base de datos.

    Parámetros:
    - sender: La clase del modelo que envía la señal (ReclamoModel en este caso).
    - instance: La instancia del reclamo que está siendo guardada.
    - kwargs: Argumentos adicionales proporcionados por la señal.

    Comportamiento:
    - incrementado en 1 la repitancia y arma el codigo de trabajo con reclamo + repitancia.
    
    """
    if not instance.pk:

        repitancia = inspecciones.objects.filter(reclamo_id=instance.reclamo_id).count() + 1
        instance.repitancia = repitancia
        numero_reclamo=ReclamoModel.objects.get(pk=instance.reclamo_id) 
        instance.codigo_trabajo= f"{numero_reclamo.numero} - {repitancia}"  
        



class InspeccionesUpdateView(mixins.LoginRequiredMixin, UpdateView):
    
    model = inspecciones
    form_class = NuevaInspeccion
    template_name = 'inspeccion/inspeccion_editar.html'
    success_url = reverse_lazy('inspecciones')
    
    #Si queremos sobrescribir la obtención del objeto
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(inspecciones, pk=pk)
        return obj
    
    def mensaje(self,request):
        messages.success(request, 'Se ha editado el proveedor correctamente')
        return redirect('inspecciones')
    
    
@login_required
def delete_inspeccion(request, pk):
    
    try:
        inspeccion = inspecciones.objects.get(pk=pk)
    except inspecciones.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    inspeccion.soft_delete()
    messages.warning(request, 'Se ha eliminado  el registro correctamente')
    return redirect('inspecciones')

#-------------------------------------------------------------------------------------------------------------------------------------------------


@login_required
def mostrar_reclamo(request, pk):
    
    try:
        reclamo = ReclamoModel.objects.get(id=pk)
    except ReclamoModel.DoesNotExist:
        
        return render(request, 'administracion/404_admin.html') 
    return render(request, 'inspeccion/inspeccion_mostrar.html', {'form': reclamo})
