from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader
from administracion.forms import Userform, AdminForm, Empresaform
from datetime import datetime



# Create your views here.
def admin(request):
    return render(request, 'administracion/admin_index.html', {})


def usuario(request):
    users=[("Chavodelocho",8888,"Admin",14000),("kiko",3333,"Inspector",14001),("candelaylamoto?",2222,"Gestor",14002),("chilindrina",1111,"basico",14003)]
    mensaje = None
    if request.method == 'POST':
        User_form = Userform(request.POST)
        mensaje = 'Hemos recibido tus datos'

    elif request.method == 'GET':
        User_form = Userform()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")
    
    context = {
        'users': users,
        'mensaje': mensaje,
        'Userform': User_form
    }
    return render(request, 'administracion/usuarios.html', context)




def empresa(request):
    proveedores=[("La podadora","La podadora S.A.","1456","20303406022","lapodadora@gmail.com","155202636"),
                 ("La podadora","La podadora S.A.","1456","20303406022","lapodadora@gmail.com","155202636"),
                 ("La podadora","La podadora S.A.","1456","20303406022","lapodadora@gmail.com","155202636"),
                 ("La podadora","La podadora S.A.","1456","20303406022","lapodadora@gmail.com","155202636"),
                 ("La podadora","La podadora S.A.","1456","20303406022","lapodadora@gmail.com","155202636"),
                 ("La podadora","La podadora S.A.","1456","20303406022","lapodadora@gmail.com","155202636")]
    mensaje = None
    if request.method == 'POST':
        empresa_form = Empresaform(request.POST)
        mensaje = 'Hemos recibido tus datos'

    elif request.method == 'GET':
        empresa_form = Userform()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")
    
    context = {
        'proveedores': proveedores,
        'mensaje': mensaje,
        'empresaform': empresa_form
    }
    return render(request, 'administracion/empresas.html', context)




