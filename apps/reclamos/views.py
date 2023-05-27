# import os
# import glob
from datetime import datetime
# from django.conf import settings
from django.views.generic import edit, ListView, UpdateView, DeleteView

from django.contrib import messages
# from django.core.mail import send_mail
# from django.conf import settings

from django.shortcuts import render, redirect
from django.utils.text import get_valid_filename

from django.urls import reverse_lazy

from .forms import ReclamoForm, DenuncianteForm
from .models import ReclamoModel, DenuncianteModel


# Create your views here.
class ReclamoCreateView(edit.CreateView):
    model = ReclamoModel
    reclamo_form_class = ReclamoForm
    denunciante_form_class = DenuncianteForm
    template_name = 'reclamos/reclamo_form.html'
    # URL a la que redirigir después de guardar el reclamo
    success_url = reverse_lazy('reclamo_form')

    def get(self, request, *args, **kwargs):
        reclamo_form = self.reclamo_form_class()
        denunciante_form = self.denunciante_form_class()
        return render(request, self.template_name, {
            'reclamo_form': reclamo_form, 'denunciante_form': denunciante_form})

    def post(self, request, *args, **kwargs):
        reclamo_form = self.reclamo_form_class(request.POST, request.FILES)
        denunciante_form = self.denunciante_form_class(request.POST)

        if reclamo_form.is_valid() and denunciante_form.is_valid():
            return self.form_valid(reclamo_form, denunciante_form)
        else:
            return self.form_invalid(reclamo_form, denunciante_form)

    def form_valid(self, reclamo_form, denunciante_form):
        messages.success(self.request, 'Reclamo creado con éxito')
        reclamo = reclamo_form.save(commit=False)
        denunciante = denunciante_form.save()

        # Guardar las fotos
        fotos = self.request.FILES.getlist('foto')
        current_datetime = datetime.now().strftime('%Y%m%d_%H%M%S%f')

        for i, pic in enumerate(fotos):
            # Obtener el nombre del archivo original
            original_filename = pic.name

            # Obtener el nombre del archivo original
            extension = original_filename.split('.')[-1]

            # Generar el nombre de la foto usando la fecha, hora actual y numero de foto subida
            foto_name = f"{current_datetime}-{i+1}"
            foto_filename = get_valid_filename(foto_name + '.' + extension)

            # Guardar el reclamo de la foto
            reclamo.foto.save(foto_filename, pic)

        reclamo.save()
        reclamo.denunciantes.add(denunciante)

        return redirect(self.success_url)

    def form_invalid(self, reclamo_form, denunciante_form):
        messages.error(self.request, 'Revisa los campos del formulario')
        return render(self.request, self.template_name, {
            'reclamo_form': reclamo_form, 'denunciante_form': denunciante_form})


class ReclamoListView(ListView):
    model = ReclamoModel
    template_name = 'reclamos/reclamo_list.html'
    context_object_name = 'reclamos'
# obtener fotos-------------------------------------
    # def obtener_fotos_por_nombre_base(self, nombre_base):
    #     media_root = settings.MEDIA_ROOT  # Ruta a la carpeta de medios configurada en settings.py
    #     subcarpeta = 'img_reclamos'  # Nombre de la subcarpeta donde se encuentran las imágenes

    #     # Construir la ruta completa a la carpeta de imágenes
    #     ruta_carpeta = os.path.join(media_root, subcarpeta)

    #     # Construir el patrón de búsqueda para las imágenes
    #     patron_busqueda = os.path.join(ruta_carpeta, f'{nombre_base}-*')

    #     # Buscar las imágenes que coincidan con el patrón
    #     imagenes = glob.glob(patron_busqueda)

    #     return imagenes
# fin obtener fotos------------------------------------
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reclamos = self.get_queryset()
        # images = []
        relaciones = []

        for reclamo in reclamos:
            # Obtener el nombre base de la foto
            # nombre_base = reclamo.foto

            # Obtener las imágenes asociadas al reclamo
            # reclamo_images = self.obtener_fotos_por_nombre_base(nombre_base)
            # images.extend(reclamo_images)

            # Obtener el primer denunciante del reclamo
            denunciante = reclamo.denunciantes.first()

            # Crear la relación reclamo-denunciante
            relacion = {
                'reclamo': reclamo,
                'denunciante': denunciante,
            }
            relaciones.append(relacion)

        # context['images'] = images
        context['relaciones'] = relaciones
        return context


class ReclamoUpdateView(UpdateView):
    model = ReclamoModel
    form_class = ReclamoForm
    denunciante_form_class = DenuncianteForm
    template_name = 'reclamos/reclamo_form.html'
    success_url = reverse_lazy('seguimiento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reclamo = self.get_object()
        context['reclamo_form'] = self.form_class(instance=self.object)
        context['denunciante_form'] = self.denunciante_form_class(
            instance=self.object.denunciantes.first())
        context['accion'] = 'actualizar'
        context['numero_reclamo'] = reclamo.numero
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        reclamo_form = self.get_form()
        denunciante_form = self.denunciante_form_class(
            request.POST, instance=self.object.denunciantes.first())
        if reclamo_form.is_valid() and denunciante_form.is_valid():
            return self.form_valid(reclamo_form, denunciante_form)
        else:
            return self.form_invalid(reclamo_form, denunciante_form)

    def form_valid(self, reclamo_form, denunciante_form):
        messages.success(self.request, 'Reclamo editado con éxito')
        reclamo = reclamo_form.save(commit=False)
        denunciante = denunciante_form.save(commit=False)
        reclamo.denunciantes.clear()
        # reclamo.denunciantes.remove(self.object.denunciantes.first())
        reclamo.denunciantes.add(denunciante)
        reclamo.save()
        return redirect(self.success_url)

    def form_invalid(self, reclamo_form, denunciante_form):
        messages.error(self.request, 'Revisa los campos del formulario')
        return self.render_to_response(self.get_context_data(
            reclamo_form=reclamo_form, denunciante_form=denunciante_form))


class ReclamoDeleteView(DeleteView):
    model = ReclamoModel
    form_class = ReclamoForm
    denunciante_form_class = DenuncianteForm
    template_name = 'reclamos/reclamo_confirm_delete.html' #!NO ES LA IDEA
    success_url = reverse_lazy('seguimiento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'eliminar'
        return context



# def reclamo_form(request): #FormView
#     """
#     Vista para manejar la creación de un nuevo reclamo.
#     Si la solicitud es de tipo 'POST', valida el formulario utilizando la clase
#     ReclamoForm y muestra los mensajes correspondientes según el resultado de la
#     validación. Si la solicitud es de tipo 'GET', crea una instancia de ReclamoForm
#     vacía. Si la solicitud no es de tipo 'GET' ni 'POST', devuelve un error de método
#     no permitido.
#     """
#     if request.method == 'POST':
#         nuevo = ReclamoForm(request.POST)

#         # acción para tomar los datos del formulario
#         if nuevo.is_valid():
#             messages.success(
#                 request,
#                 'Hemos generado el reclamo'
#             )
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


# class ObtenerCallesView(View):
#     def get(self, request):
#         relation_id = request.GET.get('localidad')

#         # Llamar a la función obtener_calles del módulo calle_utils
#         calles = get_streets(relation_id)

#         # Devolver la lista de calles como una respuesta JSON
#         return JsonResponse(calles, safe=False)


lista = ['Area Geográfica', 'Norte', 30333256,
         15995687, 42974589, 'pepe@nocorreo.com']
lista2 = ['Arbol caido = 1', 'Arbol enfermo = 2',
          'Arbol poda = 5', 'Arbol no identificado = 2']
# lista2 = []


def seguimiento(request): #ListView
    fecha_actual = datetime.now()
    nombre = lista[0] + " " + lista[1]
    return render(request, 'reclamos/seguimiento.html', {
        'fechaActual': fecha_actual,
        'nombre': nombre,
        'lista2': lista2,
        'lista': lista
    })


def seguimiento_reclamo(request, nro_reclamo): #DetailView
    return render(request, 'reclamos/ver_reclamo.html', {
        'lista2': lista2[nro_reclamo-1],
        'nro': nro_reclamo,
        'lista': lista
    })
