from datetime import datetime
from django.contrib import messages
# from django.core.mail import send_mail
# from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from .utils.street_names import get_street_names
from .forms import ReclamoForm


# Create your views here.
def nuevo_reclamo(request): #FormView
    """
    Vista para manejar la creación de un nuevo reclamo.
    Si la solicitud es de tipo 'POST', valida el formulario utilizando la clase
    ReclamoForm y muestra los mensajes correspondientes según el resultado de la
    validación. Si la solicitud es de tipo 'GET', crea una instancia de ReclamoForm
    vacía. Si la solicitud no es de tipo 'GET' ni 'POST', devuelve un error de método
    no permitido.
    """
    if request.method == 'POST':
        nuevo = ReclamoForm(request.POST)

        # acción para tomar los datos del formulario
        if nuevo.is_valid():
            messages.success(
                request,
                'Hemos generado el reclamo'
            )
            # if nuevo.correo_electronico:
            #     mensaje = f"""
            #         De : {nuevo.cleaned_data['nombre']} <{nuevo.cleaned_data['correo_electronico']}>
            #         Asunto: {nuevo.cleaned_data['asunto']}
            #         Mensaje: {nuevo.cleaned_data['mensaje']}
            #     """
            #     mensaje_html = f"""
            #         <p>De: {nuevo.cleaned_data['nombre']} <a href="mailto:{nuevo.cleaned_data['correo_electronico']}">{nuevo.cleaned_data['email']}</a></p>
            #         <p>Asunto:  {nuevo.cleaned_data['asunto']}</p>
            #         <p>Mensaje: {nuevo.cleaned_data['mensaje']}</p>
            #     """
            #     asunto = "CONSULTA DESDE LA PAGINA - " + \
            #         nuevo.cleaned_data['asunto']
            #     send_mail(
            #         asunto, mensaje, settings.EMAIL_HOST_USER,
            #         [settings.RECIPIENT_ADDRESS],
            #         fail_silently=False,
            #         html_message=mensaje_html
            #     )

        # acción para mostrar los datos del formulario
        else:
            messages.error(
                request,
                'Revisa los errores en el formulario'
            )

    elif request.method == 'GET':
        nuevo = ReclamoForm()

    else:
        return HttpResponseNotAllowed(
            f"Método {request.method} no soportado"
        )

    context = {
        'nuevo_reclamo': nuevo
    }

    return render(request, 'reclamos/nuevo_reclamo.html', context)



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
