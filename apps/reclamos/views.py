from datetime import datetime
from django.views.generic import edit, ListView, UpdateView

# from django.contrib import messages
# from django.core.mail import send_mail
# from django.conf import settings

from django.shortcuts import render, redirect
from django.utils.text import get_valid_filename

from django.urls import reverse_lazy

from .forms import ReclamoForm
from .models import ReclamoModel, DenuncianteModel


# Create your views here.
class ReclamoCreateView(edit.CreateView):
    model = ReclamoModel
    form_class = ReclamoForm
    template_name = 'reclamos/reclamo_form.html'
    # URL a la que redirigir después de guardar el reclamo
    success_url = reverse_lazy('reclamo_form')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'reclamo_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print(request.POST) #!DEBUG

        if form.is_valid():
            reclamo = form.save(commit=False)
            # Crear una instancia de DenuncianteModel y guardarla
            denunciante = DenuncianteModel(
                dni = form.cleaned_data['dni'],
                correo_electronico = form.cleaned_data['correo_electronico'],
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                celular = form.cleaned_data['celular'],
                telefono_fijo = form.cleaned_data['telefono_fijo'],
            )
            denunciante.save()

            # Guardar las fotos
            fotos = request.FILES.getlist('foto')
            current_datetime = datetime.now().strftime('%Y%m%d_%H%M%S%f')
            for i, pic in enumerate(fotos):
                # Obtener el nombre del archivo original
                original_filename = pic.name

                # Obtener la extensión del archivo original
                extension = original_filename.split('.')[-1]

                # Generar el nombre de la foto usando la fecha, hora actual y numero de foto subida
                foto_name = f"{current_datetime}-{i+1}"
                foto_filename = get_valid_filename(foto_name + '.' + extension)

                # Guardar el reclamo de la foto
                reclamo.foto.save(foto_filename, pic)


            # Asociar el denunciante con el reclamo y guardar el reclamo
            reclamo.save()
            reclamo.denunciantes.add(denunciante)

            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'reclamo_form': form})


class ReclamoListView(ListView):
    model = ReclamoModel
    template_name = 'reclamos/reclamo_list.html'
    context_object_name = 'reclamos'


class ReclamoUpdateView(UpdateView):
    model = ReclamoModel
    form_class = ReclamoForm
    template_name = 'reclamos/reclamo_form.html'
    success_url = 'seguimiento'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return self.render_to_response(self.get_context_data(reclamo_form=form))


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
