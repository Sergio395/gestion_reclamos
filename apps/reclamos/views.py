from datetime import datetime
# from django.conf import settings
from django.views import View
from django.views.generic import edit, ListView, UpdateView

from django.contrib import messages
# from django.core.mail import send_mail
# from django.conf import settings

from django.shortcuts import render, redirect
# from django.utils.text import get_valid_filename

from django.urls import reverse_lazy

from .models import ReclamoModel
from .forms import ReclamoForm, DenuncianteForm


# Create your views here.
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
         """
        Obtiene los datos del contexto para la vista.
        Retorna el contexto actualizado con la acción "crear" y la URL de acción.
        """
        context = super().get_context_data(**kwargs)
        context['accion'] = 'crear'
        context['action_url'] = reverse_lazy('reclamo_form')
        return context

    def get(self, request, *args, **kwargs):
        """
        Maneja la solicitud GET para la vista.
        Retorna la página de creación de reclamo con los campos de formulario vacíos.
        """
        reclamo_form = self.form_class()
        denunciante_form = self.denunciante_form_class()
        return render(request, self.template_name, {
            'reclamo_form': reclamo_form, 'denunciante_form': denunciante_form})

    def post(self, request, *args, **kwargs):
        """
        Maneja la solicitud POST para la vista.
        Valida los formularios de reclamo y denunciante.
        Si son válidos, llama a form_valid(). De lo contrario, llama a form_invalid().
        """
        reclamo_form = self.form_class(request.POST, request.FILES)
        denunciante_form = self.denunciante_form_class(request.POST)

        if reclamo_form.is_valid() and denunciante_form.is_valid():
            return self.form_valid(reclamo_form, denunciante_form)
        else:
            return self.form_invalid(reclamo_form, denunciante_form)

    def form_valid(self, reclamo_form, denunciante_form):
        """
        Guarda el reclamo y el denunciante en la base de datos.
        Muestra un mensaje de éxito y redirige a la URL de creación de reclamo con los campos vacíos.
        """
        messages.success(self.request, 'Reclamo creado con éxito')
        reclamo = reclamo_form.save(commit=False)
        denunciante = denunciante_form.save()

# AGREGAR FOTOS (EN CONSTRUCCION) -------------------------------------
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
# -----------------------------------------------------------------------
        reclamo.save()
        reclamo.denunciantes.add(denunciante)
        return redirect(self.success_url)

    def form_invalid(self, reclamo_form, denunciante_form):
        """
        Maneja el caso en que los formularios son inválidos.
        Muestra un mensaje de error y vuelve a renderizar la página de creación de reclamo.
        """
        messages.error(self.request, 'Revisa los campos del formulario')
        return render(self.request, self.template_name, {
            'reclamo_form': reclamo_form, 'denunciante_form': denunciante_form})


class ReclamoListView(ListView):
    """
    Vista para mostrar una lista de reclamos.
    Muestra una lista de reclamos que no han sido eliminados.
    Cada reclamo está asociado a su primer denunciante.
    """
    model = ReclamoModel
    template_name = 'reclamos/reclamo_list.html'
    context_object_name = 'reclamos'
    queryset = ReclamoModel.objects.filter(eliminado=False)
    ordering = ['numero']

    def get_context_data(self, **kwargs):
        """
        Obtiene los datos del contexto para la vista.
        Retorna el contexto actualizado con las relaciones reclamo-denunciante.
        """
        context = super().get_context_data(**kwargs)
        reclamos = self.get_queryset()
        relaciones = []

        for reclamo in reclamos:
            # Obtener el primer denunciante del reclamo
            denunciante = reclamo.denunciantes.first()

            # Crear la relación reclamo-denunciante
            relacion = {
                'reclamo': reclamo,
                'denunciante': denunciante,
            }
            relaciones.append(relacion)

        context['relaciones'] = relaciones
        return context


class ReclamoUpdateView(UpdateView):
    """
    Vista para editar un reclamo existente.
    Permite editar los datos de un reclamo, incluido su denunciante.
    """
    model = ReclamoModel
    form_class = ReclamoForm
    denunciante_form_class = DenuncianteForm
    template_name = 'reclamos/reclamo_form.html'
    success_url = reverse_lazy('seguimiento')

    def get_context_data(self, **kwargs):
        """
        Obtiene los datos del contexto para la vista.
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
        return context

    def post(self, request, *args, **kwargs):
        """
        Procesa el formulario enviado por POST.
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
        """
        Guarda los datos actualizados del reclamo y denunciante.
        Redirige a la página de seguimiento después de guardar los cambios y muestra un mensaje de éxito.
        """
        #! messages.success(self.request, 'Reclamo editado con éxito') # agregar en seguimiento
        reclamo = reclamo_form.save(commit=False)
        denunciante = denunciante_form.save(commit=False)
        reclamo.denunciantes.clear()
        reclamo.denunciantes.add(denunciante)
        reclamo.save()
        return redirect(self.success_url)

    def form_invalid(self, reclamo_form, denunciante_form):
        """
        Maneja el caso cuando el formulario es inválido.
        Muestra un mensaje de error y renderiza nuevamente el formulario con los datos ingresados.
        """
        messages.error(self.request, 'Revisa los campos del formulario')
        return self.render_to_response(self.get_context_data(
            reclamo_form=reclamo_form, denunciante_form=denunciante_form))


def reclamo_delete(request, id_reclamo):
    """
    Vista para la eliminación lógica de un reclamo.
    Elimina el reclamo especificado y redirige a la página de seguimiento.
    Si el reclamo no existe, se muestra una página de error 404.
    """
    reclamo = get_object_or_404(ReclamoModel, pk=id_reclamo)
    
    try:
        reclamo.soft_delete()
        messages.success(request, f'El reclamo con pk {reclamo.numero} se ha eliminado exitosamente.')
    except Exception as e:
        messages.error(request, f'Error al eliminar el reclamo {reclamo.numero}: {str(e)}')
    return redirect('seguimiento')


#             # if nuevo.correo_electronico:
#             #     mensaje = f"""
#             #         De : {nuevo.cleaned_data['nombre']} <{nuevo.cleaned_data['correo_electronico']}>
#             #         Asunto: {nuevo.cleaned_data['asunto']}
#             #         Mensaje: {nuevo.cleaned_data['mensaje']}
#             #     """
#             #     mensaje_html = f"""
#             #         <p>De: {nuevo.cleaned_data['nombre']} <a href="mailto:{nuevo.cleaned_data['correo_electronico']}">{nuevo.cleaned_data['email']}</a></p>
#             #         <p>Asunto:  {nuevo.cleaned_data['asunto']}</p>
#             #         <p>Mensaje: {nuevo.cleaned_data['mensaje']}</p>
#             #     """
#             #     asunto = "CONSULTA DESDE LA PAGINA - " + \
#             #         nuevo.cleaned_data['asunto']
#             #     send_mail(
#             #         asunto, mensaje, settings.EMAIL_HOST_USER,
#             #         [settings.RECIPIENT_ADDRESS],
#             #         fail_silently=False,
#             #         html_message=mensaje_html
#             #     )

#         # acción para mostrar los datos del formulario
#         else:
#             messages.error(
#                 request,
#                 'Revisa los errores en el formulario'
#             )

#     elif request.method == 'GET':
#         nuevo = ReclamoForm()

#     else:
#         return HttpResponseNotAllowed(
#             f"Método {request.method} no soportado"
#         )

#     context = {
#         'reclamo_form': nuevo
#     }

#     return render(request, 'reclamos/reclamo_form.html', context)

