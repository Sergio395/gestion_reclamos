from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from .forms import GestionForm, BusquedaForm
from .models import GestionModel

from django.views.generic.list import ListView
from django.views.generic import DetailView, edit
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.inspeccion.models import inspecciones
from apps.inspeccion.forms import NuevaInspeccion
from apps.reclamos.forms import DenuncianteForm, ReclamoForm

# # Create your views here.    
def gestion_index(request):
    '''
    Por ahora trae los valores de la tabla Gestion, pero deberiamos definir en grupo que datos va a mostrar 
    Muestra un formulario de busqueda para utilizar como filtro
    Trae los reclamos y los muestra en una tabla
    '''
    form_busqueda = BusquedaForm(request.POST or None)
    try:
        gestion = GestionModel.objects.filter(eliminado=False)
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
    filtro = {'eliminado':False}
    
    if criterio['criterio1_campo'] != 'none':
        filtro[criterio['criterio1_campo']] = criterio['criterio1_valor']
    if criterio['criterio2_campo'] != 'none':
        filtro[criterio['criterio2_campo']] = criterio['criterio2_valor']
    if criterio['criterio3_campo'] != 'none':
        filtro[criterio['criterio3_campo']] = criterio['criterio3_valor']
    if criterio['criterio4_campo'] != 'none':
        filtro[criterio['criterio4_campo']] = criterio['criterio4_valor'].strftime('%Y-%m-%d')
    return filtro

# Lo mismo pero con CBV
#---------------------------

class GestionListView(ListView):
    '''
    Muestra una lista de inspecciones
    '''
    model = inspecciones
    paginate_by = 10
    template_name = 'gestion/gestioncbv_lista.html'
    queryset = inspecciones.objects.filter(eliminado=False).all()
    ordering = ['id']
    
    def get_context_data(self, **kwargs):
        '''
        Agrega el formulario de busqueda al contexto
        '''
        context = super(GestionListView, self).get_context_data(**kwargs)
        context['form_busqueda'] = BusquedaForm()
        return context

    def post(self, request, *args, **kwargs):
        """Procesa el formulario enviado por POST.

        Si el formulario de busqueda es validos, se filtran las inspecciones y se devuelve a la lista.
        """
        # carga las instancias de los formularios
        # self.object = self.get_object()
        # busqueda_form = BusquedaForm(request.POST, instance=self.object)
        busqueda_form = BusquedaForm(request.POST)
        # reclamo_form = self.reclamo_form_class(request.POST, instance=self.object.inspecciones.reclamo)
        # inspeccion_form = self.reclamo_form_class(request.POST, instance=self.object.inspecciones)
        # gestion_form = self.get_form()
        # consulta si son validos
        if busqueda_form.is_valid():
            return self.form_valid(busqueda_form)
        else:
            return self.form_invalid(busqueda_form)
        
# ------------ voy x aca -----------

    def form_valid(self, busqueda_form):
        """Guarda los datos actualizados del reclamo y denunciante.

        Redirige a la página de seguimiento después de guardar los cambios y muestra un mensaje de éxito.
        """
        messages.success(self.request, 'Resultados de la busqueda')
        filtro = preparar_filtro(busqueda_form.cleaned_data)
        inspeccion = inspecciones.objects.filter(**filtro)
        # busqueda_form = denunciante_form.save(commit=False)
        # reclamo = reclamo_form.save(commit=False)
        # reclamo.denunciantes.clear()
        # reclamo.denunciantes.add(denunciante)
        # reclamo.save()
        # inspeccion = inspeccion_form.save(commit=False)
        # inspeccion.save()
        # gestion = gestion_form.save(commit=False)
        # gestion.save()
        return (inspeccion)

    def form_invalid(self, busqueda_form):
        """Maneja el caso cuando el formulario es inválido.

        Muestra un mensaje de error y renderiza nuevamente el formulario con los datos ingresados.
        """
        messages.error(self.request, 'Revisa los campos del formulario')
        return self.render_to_response(self.get_context_data(busqueda_form))

class GestionCreateView(CreateView):
    model = GestionModel
    form_class = GestionForm
    template_name = 'gestion/gestioncbv_nuevo.html'
    success_url = reverse_lazy('gestioncbv_lista')

class GestionDetailView(DetailView):
    '''
    Muestra una detalles de gestion
    '''
    model = GestionModel
    template_name = 'gestion/gestioncbv_detalle.html'
    queryset = GestionModel.objects.select_related().filter(eliminado=False)
    ordering = ['id']
    
    def get_context_data(self, **kwargs):
        '''
        Agrego informacion al contexto
        '''
        context = super(GestionDetailView, self).get_context_data(**kwargs)
        # obtengo instancia de los distintos modelos
        denunciante = self.object.inspecciones.reclamo.denunciantes.first()
        reclamo = self.object.inspecciones.reclamo
        inspeccion = self.object.inspecciones
        gestion = self.object
        # Paso instancias
        context['denunciante_form'] = DenuncianteForm(instance=denunciante)
        context['reclamo_form'] = ReclamoForm(instance=reclamo)
        context['inspeccion_form'] = NuevaInspeccion(instance=inspeccion)
        context['gestion_form'] = GestionForm(instance=gestion)
        # Paso las rutas de edición y sus id
        context['url_denunciante'] = f"'editar_reclamo' {denunciante.id}"
        context['url_reclamo'] = f"'editar_reclamo'{reclamo.id}"
        context['url_inspeccion'] = f"'inspeccion' {inspeccion.id}"
        context['url_gestion'] = f"'gestioncbv_editar' {gestion.id}"
        # el reto de variables de contexto
        context['calle0'] = reclamo.calle
        context['calle1'] = reclamo.entre_calle_1
        context['calle2'] = reclamo.entre_calle_2
        context['action_url'] = 'gestioncbv_detalle'
        context['accion'] = 'actualizar'

        return context

class GestionUpdateView(UpdateView):
    model = GestionModel
    # fields = '__all__'
    # form_class = NuevaInspeccion
    # queryset = GestionModel.objects.all().filter(eliminado=False)
    form_class = GestionForm
    denunciante_form_class = DenuncianteForm
    reclamo_form_class = ReclamoForm
    inspeccion_form_class = NuevaInspeccion
    template_name = 'gestion/gestion_form.html'
    success_url = reverse_lazy('gestioncbv_lista')

    def get_context_data(self, **kwargs):
        """Obtiene los datos del contexto para la vista.

        Retorna el contexto actualizado con la acción "crear" y la URL de acción.
        """
        context = super().get_context_data(**kwargs)
        context['accion'] = 'actualizar'
        # instancia de los distintos modelos
        denunciante = self.object.inspecciones.reclamo.denunciantes.first()
        reclamo = self.object.inspecciones.reclamo
        inspeccion = self.object.inspecciones
        gestion = self.object
        # carga instancias en formularios y pasa x contexto
        context['denunciante_form'] = DenuncianteForm(instance=denunciante)
        context['reclamo_form'] = ReclamoForm(instance=reclamo)
        context['inspeccion_form'] = NuevaInspeccion(instance=inspeccion)
        context['gestion_form'] = GestionForm(instance=gestion)
        context['action_url'] = reverse_lazy('gestioncbv_lista')
        # carga valores para plantilla
        context['calle0'] = reclamo.calle
        context['calle1'] = reclamo.entre_calle_1
        context['calle2'] = reclamo.entre_calle_2
        return context
    
    def post(self, request, *args, **kwargs):
        """Procesa el formulario enviado por POST.

        Si el formulario de reclamo y el formulario de denunciante son válidos, se guarda la información actualizada y se redirige a la página de seguimiento.
        """
        # carga las instancias de los formularios
        self.object = self.get_object()
        denunciante_form = self.denunciante_form_class(request.POST, instance=self.object.denunciantes.first())
        reclamo_form = self.reclamo_form_class(request.POST, instance=self.object.inspecciones.reclamo)
        inspeccion_form = self.reclamo_form_class(request.POST, instance=self.object.inspecciones)
        gestion_form = self.get_form()
        # consulta si son validos
        if denunciante_form.is_valid() and reclamo_form.is_valid() and inspeccion_form.is_valid() and gestion_form.is_valid():
            return self.form_valid(denunciante_form, reclamo_form, inspeccion_form, gestion_form)
        else:
            return self.form_invalid(denunciante_form, reclamo_form, inspeccion_form, gestion_form)

    def form_valid(self, denunciante_form, reclamo_form, inspeccion_form, gestion_form):
        """Guarda los datos actualizados del reclamo y denunciante.

        Redirige a la página de seguimiento después de guardar los cambios y muestra un mensaje de éxito.
        """
        messages.success(self.request, 'Información actualizado con éxito')
        denunciante = denunciante_form.save(commit=False)
        reclamo = reclamo_form.save(commit=False)
        reclamo.denunciantes.clear()
        reclamo.denunciantes.add(denunciante)
        reclamo.save()
        inspeccion = inspeccion_form.save(commit=False)
        inspeccion.save()
        gestion = gestion_form.save(commit=False)
        gestion.save()
        return redirect(self.success_url)

    def form_invalid(self, denunciante_form, reclamo_form, inspeccion_form, gestion_form):
        """Maneja el caso cuando el formulario es inválido.

        Muestra un mensaje de error y renderiza nuevamente el formulario con los datos ingresados.
        """
        messages.error(self.request, 'Revisa los campos del formulario')
        return self.render_to_response(self.get_context_data(
            reclamo_form=reclamo_form, denunciante_form=denunciante_form, inspeccion_form=inspeccion_form, gestion_form=gestion_form))

class GestionDeleteView(DeleteView):
    model = GestionModel
    success_url = reverse_lazy("gestioncbv_lista")

    def post(self, request, *args, **kwargs):
        """Procesa el formulario enviado por POST.

        Si el formulario de reclamo y el formulario de denunciante son válidos, se guarda la información actualizada y se redirige a la página de seguimiento.
        """
        # carga las instancias de los formularios
        self.object = self.get_object()
        gestion_form = self.get_form()
        # consulta si son validos
        if gestion_form.is_valid():
            return self.form_valid(gestion_form)
        else:
            return self.form_invalid(gestion_form)

    def form_valid(self, gestion_form):
        """Guarda los datos actualizados del reclamo y denunciante.

        Redirige a la página de seguimiento después de guardar los cambios y muestra un mensaje de éxito.
        """
        messages.success(self.request, 'Información actualizado con éxito')
        gestion = gestion_form.save(commit=False)
        gestion.soft_delete()
        return redirect(self.success_url)

    def form_invalid(self, gestion_form):
        """Maneja el caso cuando el formulario es inválido.

        Muestra un mensaje de error y renderiza nuevamente el formulario con los datos ingresados.
        """
        messages.error(self.request, 'Revisa los campos del formulario')
        return self.render_to_response(self.get_context_data(gestion_form=gestion_form))


#-------------------------------

# class GestionCreateView(edit.CreateView):
#     """Vista para crear un numero de gestion asociada a un reclamo(inspeccion).
#     """
# #--------------- Voy revisando por aca -----
#     model = inspecciones
#     form_class = GestionForm
#     denunciante_form_class = DenuncianteForm
#     reclamo_form_class = ReclamoForm
#     inspecciones_form_class = NuevaInspeccion # estaria bueno cambiarle el nombre
#     template_name = 'gestion/gestion_form.html'
#     success_url = reverse_lazy('gestion_form')

#     def dispatch(self, request, *args, **kwargs):
#         inspeccion_pk = self.kwargs['pk']
#         self.inspeccion = inspecciones.objects.get (pk=inspeccion_pk)
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         """Obtiene los datos del contexto para la vista.

#         Retorna el contexto actualizado con la acción "crear" y la URL de acción.
#         """
#         context = super().get_context_data(**kwargs)
#         context['accion'] = 'crear'
#         context['inspeccion'] = self.inspeccion
#         context['action_url'] = reverse_lazy('gestion_form')
#         return context

#     def get(self, request, *args, **kwargs):
#         """Maneja la solicitud GET para la vista.

#         Retorna la página de creación de reclamo con los campos de formulario vacíos.
#         """
#         gestion_form = self.form_class()
#         reclamo_form = self.reclamo_form_class()
#         denunciante_form = self.denunciante_form_class()
#         inspecciones_form = self.inspecciones_form_class()
#         return render(request, self.template_name, {
#             'gestion_form': gestion_form,'reclamo_form': reclamo_form, 'denunciante_form': denunciante_form, 'inspecciones_form': inspecciones_form})

#     def post(self, request, *args, **kwargs):
#         """Maneja la solicitud POST para la vista.

#         Valida los formularios de reclamo y denunciante. Si son válidos, llama a form_valid(). De lo contrario, llama a form_invalid().
#         """
#         gestion_form = self.form_class(request.POST)
#         reclamo_form = self.reclamo_form_class(request.POST, request.FILES)
#         denunciante_form = self.denunciante_form_class(request.POST)
#         inspecciones_form = self.inspecciones_form_class(request.POST)

#         if gestion_form.is_valid() and reclamo_form.is_valid() and denunciante_form.is_valid() and inspecciones_form.is_valid():
#             return self.form_valid(gestion_form, reclamo_form, denunciante_form, inspecciones_form)
#         else:
#             return self.form_invalid(gestion_form, reclamo_form, denunciante_form, inspecciones_form)

#     def form_valid(self, gestion_form, reclamo_form, denunciante_form, inspecciones_form):
#         """Guarda el reclamo y el denunciante en la base de datos.

#         Muestra un mensaje de éxito y redirige a la URL de creación de reclamo con los campos vacíos.
#         """
#         messages.success(self.request, 'Reclamo creado con éxito')
#         gestion = gestion_form.save(commit=False)
#         reclamo = reclamo_form.save()
#         denunciante = denunciante_form.save()
#         inspecciones = inspecciones_form.save()
#         gestion.save()
#         gestion.inspecciones.add(inspecciones[pk])
#         return redirect(self.success_url)

#     def form_invalid(self, gestion_form, reclamo_form, denunciante_form, inspecciones_form):
#         """Maneja el caso en que los formularios son inválidos.

#         Muestra un mensaje de error y vuelve a renderizar la página de creación de reclamo.
#         """
#         messages.error(self.request, 'Revisa los campos del formulario')
#         return render(self.request, self.template_name, {self, gestion_form, reclamo_form, denunciante_form, inspecciones_form})


#---------------------------
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
