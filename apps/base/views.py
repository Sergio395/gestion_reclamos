from django.shortcuts import render


# Create your views here.
def index(request):
    """Vista para la página de inicio.

    Esta vista renderiza la plantilla 'base/index.html' y devuelve el resultado como respuesta HTTP. No se pasan datos adicionales al contexto de la plantilla, por lo que se pasa un diccionario vacío como argumento al método `render()`.
    """
    return render(request, 'base/index.html', {})
