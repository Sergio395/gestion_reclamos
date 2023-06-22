# from datetime import datetime
# from django.contrib import messages
# from django.forms import ValidationError
from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render,redirect
from django.http import HttpResponseNotAllowed
from .forms import ContactoForm, NuevaInspeccion, NuevaCertificacion, InspeccionForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import inspecciones, Inspeccion, Especies,Usuario, Trabajos
from django.shortcuts import get_object_or_404
from django.contrib import messages
from apps.reclamos.models import ReclamoModel 
from apps.reclamos.forms import ReclamoForm 
from django.contrib.auth import mixins
from django.contrib.auth.decorators import login_required
from apps.inspeccion.models import Inspeccion 
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import EmailMessage

@login_required
def db_inspeccion(request):
    inspeccionesRealizadas = Inspeccion.objects.all()
    return render (request, 'inspeccion/inspecciones.html',{'inspecciones':inspeccionesRealizadas  })


@login_required 
def correos(request):
    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["sertol2019@gmail.com"]
        send_mail(subject,message,email_from,recipient_list)
        return render(request,"inspeccion/gracias.html")
    return render(request, 'inspeccion/correos.html')
 
@login_required    
def carga_inspeccion(request):
    pass

    # inspeccionesRealizadas = inspecciones.objects.all()
    # return render (request, 'inspeccion/inspecciones.html',{'inspecciones':inspeccionesRealizadas  })
    

@login_required
def inspeccion(request):
    contacto_form =ContactoForm()
    if request.method == "POST":
        contacto_form =ContactoForm(data=request.POST)
        if contacto_form.is_valid():
            asunto=request.POST.get("asunto")
            denunciante=request.POST.get("denunciante")
            documento=request.POST.get("documento")
            email=request.POST.get("email")
            mensaje=request.POST.get("mensaje")
            email=EmailMessage("Municipalidad Django Gestion Reclamos",
            "Asunto: {} ,el denunciante: {} con documento: {}, su correo: {}. El mensaje es: {}".format(asunto,denunciante,documento,email,mensaje),
            '',
            ['tolser2019@gmail.com'],
            reply_to=[email])
            try:
                email.send()
                return redirect("/inspeccion/inspeccion/?valido")
            
                print("Reclamo enviado con éxito")
            except:
                return redirect("/inspeccion/inspeccion/?novalido")
                messages.warning(request, 'Reclamo no enviado: Enviar nuevamnete')
        #     infFormi = contacto_form .cleaned_data
        #     send_mail(infFormi['asunto'], infFormi['denunciante'],
        #     infFormi['direccion'],infFormi['mensaje'],
        #     infFormi.get('email',''),['tolser2019@gmail.com'],)
    #         return render(request, 'inspeccion/Gracias.html')
    # else:
    #     contacto_form =ContactoForm()
    
    return render(request, 'inspeccion/inspeccion_index.html',{'formic':contacto_form }) 
 





     
    # mensaje = None
    # if request.method == 'POST':
    #     contacto_form = ContactoForm(request.POST)
    #     mensaje = 'Tus datos están Ok'
    # # acción para tomar los datos del formulario
    # elif request.method == 'GET':
    #     contacto_form = ContactoForm()
    # else:
    #     return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    # context = {
    #     'mensaje': mensaje,
    #     'contacto_form': contacto_form
    # }

    # return render(request, 'inspeccion/inspeccion_index.html', context)




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
    #formulario = ReclamoForm(request.POST or None, request.FILES or None, instance=reclamo)
    


    return render(request, 'inspeccion/inspeccion_mostrar.html', {'form': reclamo})


@login_required 
def inspeccion_form(request):
    data = {
        'form': InspeccionForm()
    }
    
    if request.method == 'POST':
        formulario = InspeccionForm(data=request.POST, files=request.FILES)
        data['mensaje']=""
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Envío exitoso, ingrese otra inspección"
        else:
            data['form'] = formulario
            data['mensaje'] = "Envío inválido, revisar"
    
    return render(request,'inspeccion/inspeccion_form.html',data)

 
 
 
 
 
 
 
 
 
 
 
 
    





















   
   
   
   
   
   
   
   
 
    
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

@login_required
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