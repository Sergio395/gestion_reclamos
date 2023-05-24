from datetime import datetime
from django.views.generic import edit, View
from django.contrib import messages
# from django.core.mail import send_mail
# from django.conf import settings
from django.shortcuts import render
# from django.http import JsonResponse, HttpResponseNotAllowed
from django.urls import reverse_lazy
# from .utils.calle_utils import get_streets
from .utils.calles_json import CALLES_JSON
from .forms import ReclamoForm
from .models import ReclamoModel, DenuncianteModel


# Create your views here.
class ReclamoView(edit.CreateView):
    model = ReclamoModel
    form_class = ReclamoForm
    template_name = 'reclamos/nuevo_reclamo.html'
    # URL a la que redirigir después de guardar el reclamo
    success_url = reverse_lazy('nuevo_reclamo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nuevo_reclamo'] = ReclamoForm()
        return context

    # def form_valid(self, form):
    #     # Obtener los valores de los campos personalizados
    #     nombre = form.cleaned_data['nombre']
    #     apellido = form.cleaned_data['apellido']
    #     dni = form.cleaned_data['dni']
    #     celular = form.cleaned_data['celular']
    #     telefono_fijo = form.cleaned_data['telefono_fijo']
    #     correo_electronico = form.cleaned_data['correo_electronico']

    #     # Crear una instancia de DenuncianteModel y guardarla
    #     denunciante = DenuncianteModel(
    #         telefono_fijo=telefono_fijo,
    #         nombre=nombre,
    #         celular=celular,
    #         apellido=apellido,
    #         correo_electronico=correo_electronico,
    #         dni=dni
    #     )
    #     denunciante.save()

    #     # Asociar el denunciante con el reclamo y guardar el reclamo
    #     reclamo = form.save(commit=False)
    #     reclamo.denunciantes.add(denunciante)
    #     reclamo.save()

    #     return super().form_valid(form)

    # def form_invalid(self, form):
    #     messages.error(self.request, 'Revisa los errores en el formulario')

    #     return self.render_to_response(self.get_context_data(form=form))

    # def form_invalid(self, form):
    #     response = super().form_invalid(form)
    #     messages.error(self.request, 'Revisa los errores en el formulario')
    #     return response

    # def form_invalid(self, form):
    #     messages.error(self.request, 'Revisa los errores en el formulario')
    #     return self.render_to_response(self.get_context_data())



# def nuevo_reclamo(request): #FormView
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
#         'nuevo_reclamo': nuevo
#     }

#     return render(request, 'reclamos/nuevo_reclamo.html', context)


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
