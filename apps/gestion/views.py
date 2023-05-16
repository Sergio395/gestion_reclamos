from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.template import loader
from .forms import GesContacto, GesInspector, GesInspeccion, GesGestion, GesBusqueda

lista_reclamos = [
    {
		"medio": "1",
		"fuente": "1",
		"fecha": "0001-01-01",
		"nombre": "nombre 1",
		"apellido": "apellido 1",
		"dni": "1",
		"celular": "1",
		"tel_fijo": "1",
		"mail": "a@a.com",
		"calle": "calle 1",
		"altura": "altura 1",
		"edificio": "edificio 1",
		"departamento": "departamento 1",
		"entre_calle_1": "entre_calle_1 1",
		"entre_calle_2": "entre_calle_2 1",
		"localidad": "localidad 1",
		"urgencia": "2",
		"detalle": "detalle 1",
		"nombre2": "nombre 1",
		"lugar": "lugar 1",
		"reclamo": "1",
		"nota": "nota 1",
		"numero_reclamo": "1",
		"reclamo_valido": "2",
		"fecha_inspeccion": "0001-01-01",
		"trabajo": "2",
		"especie": "2",
		"altura3": "11111",
		"dap": "dap 1",
		"cableado": "cableado 1",
		"construccion": "construccion 1",
		"observaciones": "observaciones 1",
		"urgencia4": "1",
		"inspector": "2",
		"estado": "1",
		"gestion": "gestion 1",
		"detalle_gestion": "detalle_gestion 1",
		"equipo_trabajo": "equipo_trabajo 1",
		"fecha_programada": "0001-01-01",
		"fecha_solucion": "0001-01-01",
		"orden_trabajo": "1"
    },
    {
    	"medio": "2",
		"fuente": "2",
		"fecha": "0002-02-02",
		"nombre": "nombre 2",
		"apellido": "apellido 2",
		"dni": "2",
		"celular": "2",
		"tel_fijo": "2",
		"mail": "a@a.com",
		"calle": "calle 2",
		"altura": "altura 2",
		"edificio": "edificio 2",
		"departamento": "departamento 2",
		"entre_calle_1": "entre_calle_1 2",
		"entre_calle_2": "entre_calle_2 2",
		"localidad": "localidad 2",
		"urgencia": "2",
		"detalle": "detalle 2",
		"nombre2": "nombre 2",
		"lugar": "lugar 2",
		"reclamo": "2",
		"nota": "nota 2",
		"numero_reclamo": "2",
		"reclamo_valido": "2",
		"fecha_inspeccion": "0002-02-02",
		"trabajo": "2",
		"especie": "2",
		"altura3": "2222",
		"dap": "dap 2",
		"cableado": "cableado 2",
		"construccion": "construccion 2",
		"observaciones": "observaciones 2",
		"urgencia4": "1",
		"inspector": "2",
		"estado": "1",
		"gestion": "gestion 2",
		"detalle_gestion": "detalle_gestion 2",
		"equipo_trabajo": "equipo_trabajo 2",
		"fecha_programada": "0002-02-02",
		"fecha_solucion": "0002-02-02",
		"orden_trabajo": "1"
    },
    {
    	"medio": "3",
		"fuente": "3",
		"fecha": "0003-03-03",
		"nombre": "nombre 3",
		"apellido": "apellido 3",
		"dni": "33333",
		"celular": "333333",
		"tel_fijo": "33333",
		"mail": "a@a.com",
		"calle": "calle 3",
		"altura": "altura 3",
		"edificio": "edificio 3",
		"departamento": "departamento 3",
		"entre_calle_1": "entre_calle_1 3",
		"entre_calle_2": "entre_calle_2 3",
		"localidad": "localidad 3",
		"urgencia": "2",
		"detalle": "detalle 3",
		"nombre2": "nombre 3",
		"lugar": "lugar 3",
		"reclamo": "3",
		"nota": "nota 3",
		"numero_reclamo": "3",
		"reclamo_valido": "2",
		"fecha_inspeccion": "0003-03-03",
		"trabajo": "2",
		"especie": "2",
		"altura3": "3333",
		"dap": "dap 3",
		"cableado": "cableado 3",
		"construccion": "construccion 3",
		"observaciones": "observaciones 3",
		"urgencia4": "1",
		"inspector": "2",
		"estado": "1",
		"gestion": "gestion 3",
		"detalle_gestion": "detalle_gestion 3",
		"equipo_trabajo": "equipo_trabajo 3",
		"fecha_programada": "0003-03-03",
		"fecha_solucion": "0003-03-03",
		"orden_trabajo": "1"
    },
    {
    	"medio": "4",
		"fuente": "4",
		"fecha": "0004-04-04",
		"nombre": "nombre 4",
		"apellido": "apellido 4",
		"dni": "44444",
		"celular": "444444",
		"tel_fijo": "444444",
		"mail": "a@a.com",
		"calle": "calle 4",
		"altura": "altura 4",
		"edificio": "edificio 4",
		"departamento": "departamento 4",
		"entre_calle_1": "entre_calle_1 4",
		"entre_calle_2": "entre_calle_2 4",
		"localidad": "localidad 4",
		"urgencia": "2",
		"detalle": "detalle 4",
		"nombre2": "nombre 4",
		"lugar": "lugar 4",
		"reclamo": "4",
		"nota": "nota 4",
		"numero_reclamo": "4",
		"reclamo_valido": "2",
		"fecha_inspeccion": "0004-04-04",
		"trabajo": "2",
		"especie": "2",
		"altura3": "4444",
		"dap": "dap 4",
		"cableado": "cableado 4",
		"construccion": "construccion 4",
		"observaciones": "observaciones 4",
		"urgencia4": "1",
		"inspector": "2",
		"estado": "1",
		"gestion": "gestion 4",
		"detalle_gestion": "detalle_gestion 4",
		"equipo_trabajo": "equipo_trabajo 4",
		"fecha_programada": "0004-04-04",
		"fecha_solucion": "0004-04-04",
		"orden_trabajo": "1"
    },
    {
    	"medio": "5",
		"fuente": "5",
		"fecha": "0005-05-05",
		"nombre": "nombre 5",
		"apellido": "apellido 5",
		"dni": "55555",
		"celular": "5555",
		"tel_fijo": "5555",
		"mail": "a@a.com",
		"calle": "calle 5",
		"altura": "altura 5",
		"edificio": "edificio 5",
		"departamento": "departamento 5",
		"entre_calle_1": "entre_calle_1 5",
		"entre_calle_2": "entre_calle_2 5",
		"localidad": "localidad 5",
		"urgencia": "2",
		"detalle": "detalle 5",
		"nombre2": "nombre 5",
		"lugar": "lugar 5",
		"reclamo": "5",
		"nota": "nota 5",
		"numero_reclamo": "5",
		"reclamo_valido": "2",
		"fecha_inspeccion": "0005-05-05",
		"trabajo": "2",
		"especie": "2",
		"altura3": "5555",
		"dap": "dap 5",
		"cableado": "cableado 5",
		"construccion": "construccion 5",
		"observaciones": "observaciones 5",
		"urgencia4": "1",
		"inspector": "2",
		"estado": "1",
		"gestion": "gestion 5",
		"detalle_gestion": "detalle_gestion 5",
		"equipo_trabajo": "equipo_trabajo 5",
		"fecha_programada": "0005-05-05",
		"fecha_solucion": "0005-05-05",
		"orden_trabajo": "1"
    }
]

# Create your views here.
def gestion_inicio (request):
    mensaje = None
    if request.method == 'POST':
        form_busqueda = GesBusqueda(request.POST)
        mensaje = 'Hemos recibido tus datos'
        # acción para tomar los datos del formulario
    elif request.method == 'GET':
        form_busqueda = GesBusqueda()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    context = {
		'reclamos': lista_reclamos,
        'mensaje': mensaje,
        'form_busqueda' : GesBusqueda
    }
    return render(request, 'gestion/gestion_inicio.html', context)


def gestion_editar_reclamo(request, nro_reclamo):
    datos_reclamo = lista_reclamos[nro_reclamo-1]
    mensaje = None
    if request.method == 'POST':
        form_contacto = GesContacto(request.POST)
        form_inspector = GesInspector(request.POST)
        form_inspeccion = GesInspeccion(request.POST)
        form_gestion = GesGestion(request.POST)
        mensaje = 'Hemos recibido tus datos'
        # acción para tomar los datos del formulario
    elif request.method == 'GET':
        form_contacto = GesContacto(datos_reclamo)
        form_inspector = GesInspector(datos_reclamo)
        form_inspeccion = GesInspeccion(datos_reclamo)
        form_gestion = GesGestion(datos_reclamo)
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    context = {
        'nro_reclamo' : nro_reclamo,
        'mensaje': mensaje,
        'datos_reclamo': datos_reclamo,
        'form_contacto': form_contacto,
        'form_inspector': form_inspector,
        'form_inspeccion': form_inspeccion,
        'form_gestion': form_gestion,
    }
    return render(request, 'gestion/gestion_editar_reclamo.html', context)