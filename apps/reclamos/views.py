# from datetime import datetime
from django.views.generic import edit, ListView, UpdateView
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.html import format_html
from django.core.mail import send_mail
from django.urls import reverse

from decouple import config
from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404
# from django.utils.text import get_valid_filename

from .models import ReclamoModel
from .forms import ReclamoForm, DenuncianteForm
from .utils.log_filters import ReclamoFilter
from ..base.utils.decorators import group_required


AUTORIZED_GROUPS = 'operador', 'inspector', 'gestor', 'administrador'


# * ==================== RECLAMO CREATE VIEW ====================

@method_decorator([login_required, group_required(*AUTORIZED_GROUPS)], name='dispatch')
class ReclamoCreateView(edit.CreateView):
    """
    Vista para crear un reclamo.
    """
    model = ReclamoModel
    form_class = ReclamoForm
    denunciante_form_class = DenuncianteForm
    template_name = 'reclamos/reclamo_form.html'
    success_url = reverse_lazy('reclamo_form')

    def get_context_data(self, **kwargs):
        """Obtiene los datos del contexto para la vista.

        Retorna el contexto actualizado con la acción "crear" y la URL de acción.
        """
        context = super().get_context_data(**kwargs)
        context['accion'] = 'crear'
        context['action_url'] = reverse_lazy('reclamo_form')
        return context

    def get(self, request, *args, **kwargs):
        """Maneja la solicitud GET para la vista.

        Retorna la página de creación de reclamo con los campos de formulario vacíos.
        """
        reclamo_form = self.form_class()
        denunciante_form = self.denunciante_form_class()
        return render(request, self.template_name, {
            'reclamo_form': reclamo_form, 'denunciante_form': denunciante_form})

    def post(self, request, *args, **kwargs):
        """Maneja la solicitud POST para la vista.

        Valida los formularios de reclamo y denunciante. Si son válidos, llama a form_valid(). De lo contrario, llama a form_invalid().
        """
        reclamo_form = self.form_class(request.POST, request.FILES)
        denunciante_form = self.denunciante_form_class(request.POST)

        if reclamo_form.is_valid() and denunciante_form.is_valid():
            return self.form_valid(reclamo_form, denunciante_form)
        else:
            return self.form_invalid(reclamo_form, denunciante_form)

    def form_valid(self, reclamo_form, denunciante_form):
        """Guarda el reclamo y el denunciante en la base de datos.

        Muestra un mensaje de éxito, envía un correo electrónico al denunciante con información sobre el reclamo y redirige a la URL de creación de reclamo con los campos vacíos.
        """
        messages.success(self.request, 'Reclamo creado con éxito')
        reclamo = reclamo_form.save(commit=False)
        denunciante = denunciante_form.save()

# ? AGREGAR FOTOS (EN CONSTRUCCION) -------------------------------------
        # # Guardar las fotos
        # fotos = self.request.FILES.getlist('foto')
        # current_datetime = datetime.now().strftime('%Y%m%d_%H%M%S%f')

        # for i, pic in enumerate(fotos):
        #     # Obtener el nombre del archivo original
        #     original_filename = pic.name

        #     # Obtener el nombre del archivo original
        #     extension = original_filename.split('.')[-1]

        #     # Generar el nombre de la foto usando la fecha, hora actual y numero de foto subida
        #     foto_name = f"{current_datetime}-{i+1}"
        #     foto_filename = get_valid_filename(foto_name + '.' + extension)

        #     # Guardar el reclamo de la foto
        #     reclamo.foto.save(foto_filename, pic)
# ? -----------------------------------------------------------------------
        reclamo.save()
        reclamo.denunciantes.add(denunciante)

        email = denunciante_form.cleaned_data['correo_electronico']

        if email:
            # Envío de correo electrónico con texto plano.
            subject = f"{denunciante_form.cleaned_data['nombre']} hemos registrado su reclamo"
            message = f'''
                Su número de reclamo es {reclamo_form.cleaned_data['numero']}.
                Para realizar el seguimiento del mismo, por favor comunicarse con el municipio.
            '''
            from_email = config("EMAIL_HOST_USER")
            to_email = email
            send_mail(subject, message, from_email, [to_email])

# ? EMAIL CON TEMPLATE PRESONALIZADO (EN COSNTRUCCIÓN)---------------------
            # # Envío de correo electrónico con template personalizado
            # subject = 'Su reclamo ha sido registrado con éxito'
            # from_email = config("EMAIL_HOST_USER")
            # to_email = email

            # # Renderizar el contenido del template con los datos relevantes
            # context = {'reclamo': reclamo, 'denunciante': denunciante}
            # message = render_to_string('reclamos/email_template.html', context)

            # # Enviar el correo electrónico
            # send_mail(subject, message, from_email, [to_email], html_message=message)
# ? --------------------------------------------------------------------------
        return redirect(self.success_url)

    def form_invalid(self, reclamo_form, denunciante_form):
        """Maneja el caso en que los formularios son inválidos.

        Muestra un mensaje de error y vuelve a renderizar la página de creación de reclamo.
        """
        messages.error(self.request, 'Revisa los campos del formulario')
        return render(self.request, self.template_name, {
            'reclamo_form': reclamo_form, 'denunciante_form': denunciante_form})


# * ==================== RECLAMO LIST VIEW ====================

@method_decorator([login_required, group_required(*AUTORIZED_GROUPS)], name='dispatch')
class ReclamoListView(ListView):
    """Vista para mostrar una lista de reclamos.

    Muestra una lista de reclamos que no han sido eliminados.
    Cada reclamo está asociado a su primer denunciante.
    """
    model = ReclamoModel
    template_name = 'reclamos/reclamo_list.html'
    context_object_name = 'relaciones'
    queryset = ReclamoModel.objects.filter(eliminado=False)
    paginate_by = 6
    ordering = ['numero', '-repitancia']

    def get_queryset(self):
        """Obtiene el conjunto de consultas (queryset) para la vista.

        Filtra los reclamos según los parámetros proporcionados en el formulario, incluyendo la fecha de inicio y fecha de fin, si están presentes y retorna un queryset filtrado de reclamos.
        """
        queryset = super().get_queryset()
        reclamo_filter = ReclamoFilter(self.request.GET, queryset=queryset)

        # Obtener los valores de fecha_inicio y fecha_fin del formulario
        fecha_inicio = self.request.GET.get('fecha_inicio')
        fecha_fin = self.request.GET.get('fecha_fin')

        # Obtener los valores de repitancia_operador y repitancia del formulario
        repitancia_operador = reclamo_filter.form.data.get('repitancia_operador')
        repitancia = reclamo_filter.form.data.get('repitancia')

        # Obtener los valores del resto de filtros
        medio = reclamo_filter.form.data.get('medio')
        fuente = reclamo_filter.form.data.get('fuente')
        localidad = reclamo_filter.form.data.get('localidad')
        calle = reclamo_filter.form.data.get('calle')
        altura = reclamo_filter.form.data.get('altura')
        reclamo = reclamo_filter.form.data.get('reclamo')
        urgencia = reclamo_filter.form.data.get('urgencia')

        if fecha_inicio:
            queryset = queryset.filter(fecha__gte=fecha_inicio)

        if fecha_fin:
            queryset = queryset.filter(fecha__lte=fecha_fin)

        if repitancia and repitancia_operador:
            queryset = reclamo_filter.filters['repitancia'].filter(queryset, repitancia)

        if medio:
            queryset = queryset.filter(medio=medio)

        if fuente:
            queryset = queryset.filter(fuente=fuente)

        if localidad:
            queryset = queryset.filter(localidad=localidad)

        if calle:
            queryset = queryset.filter(calle=calle)

        if altura:
            queryset = queryset.filter(altura=altura)

        if reclamo:
            queryset = queryset.filter(reclamo=reclamo)

        if urgencia:
            queryset = queryset.filter(urgencia=urgencia)

        return queryset

    def get_context_data(self, **kwargs):
        """Obtiene los datos del contexto para la vista.

        Retorna el contexto actualizado con las relaciones reclamo-denunciante.
        """
        context = super().get_context_data(**kwargs)
        reclamos = self.get_queryset()
        reclamo_filter = ReclamoFilter(self.request.GET, queryset=reclamos)
        paginator = Paginator(reclamo_filter.qs, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        relaciones = []

        for reclamo in page_obj:
            # Obtener el primer denunciante del reclamo
            denunciante = reclamo.denunciantes.first()

            # Crear la relación reclamo-denunciante
            relacion = {
                'reclamo': reclamo,
                'denunciante': denunciante,
            }
            relaciones.append(relacion)

        context['relaciones'] = relaciones
        context['reclamo_filter'] = ReclamoFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get(self, request, *args, **kwargs):
        """Maneja la solicitud GET para la vista.

        Si se proporciona el parámetro 'reset_filters' en la URL, redirecciona a la URL de la vista sin los parámetros de filtro.
        De lo contrario, retorna la página de creación de reclamo con los campos de formulario vacíos.
        """
        if 'reset_filters' in request.GET:
            # Redireccionar a la URL de la vista sin los parámetros de filtro
            return HttpResponseRedirect(reverse('seguimiento'))
        return super().get(request, *args, **kwargs)


# * ==================== RECLAMO UPDATE VIEW ====================

@method_decorator([login_required, group_required(*AUTORIZED_GROUPS)], name='dispatch')
class ReclamoUpdateView(UpdateView):
    """Vista para editar un reclamo existente.

    Permite editar los datos de un reclamo, incluido su denunciante.
    """
    model = ReclamoModel
    form_class = ReclamoForm
    denunciante_form_class = DenuncianteForm
    template_name = 'reclamos/reclamo_form.html'
    success_url = reverse_lazy('seguimiento')

    def get_context_data(self, **kwargs):
        """Obtiene los datos del contexto para la vista.

        Retorna el contexto actualizado con los formularios de reclamo y denunciante, así como los detalles adicionales para la vista de edición.
        """
        context = super().get_context_data(**kwargs)
        reclamo = self.get_object()
        context['reclamo_form'] = self.form_class(instance=self.object)
        context['denunciante_form'] = self.denunciante_form_class(
            instance=self.object.denunciantes.first())
        context['accion'] = 'actualizar'
        context['action_url'] = reverse_lazy('editar_reclamo', kwargs={'pk': reclamo.pk})
        context['numero_reclamo'] = reclamo.numero
        context['calle0'] = reclamo.calle
        context['calle1'] = reclamo.entre_calle_1
        context['calle2'] = reclamo.entre_calle_2
        return context

    def post(self, request, *args, **kwargs):
        """Procesa el formulario enviado por POST.

        Si el formulario de reclamo y el formulario de denunciante son válidos, se guarda la información actualizada y se redirige a la página de seguimiento.
        """
        self.object = self.get_object()
        reclamo_form = self.get_form()
        denunciante_form = self.denunciante_form_class(
            request.POST, instance=self.object.denunciantes.first())
        if reclamo_form.is_valid() and denunciante_form.is_valid():
            return self.form_valid(reclamo_form, denunciante_form)
        else:
            return self.form_invalid(reclamo_form, denunciante_form)

    def form_valid(self, reclamo_form, denunciante_form):
        """Guarda los datos actualizados del reclamo y denunciante.

        Redirige a la página de seguimiento después de guardar los cambios y muestra un mensaje de éxito.
        """
        messages.success(self.request, 'Reclamo actualizado con éxito')
        reclamo = reclamo_form.save(commit=False)
        denunciante = denunciante_form.save(commit=False)
        reclamo.denunciantes.clear()
        reclamo.denunciantes.add(denunciante)
        reclamo.save()
        return redirect(self.success_url)

    def form_invalid(self, reclamo_form, denunciante_form):
        """Maneja el caso cuando el formulario es inválido.

        Muestra un mensaje de error y renderiza nuevamente el formulario con los datos ingresados.
        """
        messages.error(self.request, 'Revisa los campos del formulario')
        return self.render_to_response(self.get_context_data(
            reclamo_form=reclamo_form, denunciante_form=denunciante_form))


# * ==================== RECLAMO DELETE ====================

@login_required
@group_required(*AUTORIZED_GROUPS)
def reclamo_delete(request, id_reclamo):
    """Vista para la eliminación lógica de un reclamo.

    Elimina el reclamo especificado y redirige a la página de seguimiento.
    Si el reclamo no existe, se muestra una página de error 404.
    """
    reclamo = get_object_or_404(ReclamoModel, pk=id_reclamo)

    try:
        reclamo.soft_delete()
        mensaje_exito = format_html('El reclamo <strong>{}</strong> se ha eliminado exitosamente.', reclamo.numero)
        messages.success(request, mensaje_exito)
    except Exception as e:
        mensaje_error = format_html('Error al eliminar el reclamo <strong>{}</strong>: {}', reclamo.numero, str(e))
        messages.error(request, mensaje_error)
    return redirect('seguimiento')
