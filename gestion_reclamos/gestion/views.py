from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.template import loader
from gestion.forms import GestionForm, GesContactoForm, GesInspeccion, GesGestion

lista_reclamos = [
    {
        "Reclamo": "1",
    	"Medio": "Medio1",
    	"Fuente": "Fuente1",
    	"Fechadereclamo": "Fecha reclamo 1",
    	"NombreyApellido": "Nombre y apellido 1",
    	"DNI": "DNI1",
    	"Celular": "Celular 1",
    	"Telefono": "Teléfono 1",
    	"Mail": "Mail1",
    	"Calle": "Calle1",
    	"Altura": "Altura1",
    	"Edificio": "Edificio1",
    	"Depto": "Depto1",
    	"Entrecalle1": "EC1-1",
    	"Entrecalle2": "EC1-2",
    	"Localidad": "Localidad1",
    	"ReclamoB": "ReclamoB1",
    	"Urgencia": "Urgencia1",
    	"Detalledelreclamo": "Detalle1",
    	"FechadeCarga": "Fecha Carga1",
    	"ID": "ID1",
    	"Norequiereinspeccion": "NRI1",
    	"Fechadeinspeccion": "Fecha Insp1",
    	"Trabajoarealizar": "Trabajo a ralizar1",
    	"Especie": "Especie1",
    	"Altura(m)": "Altra1",
    	"Dap(cm)": "Dap1",
    	"Cableadocercano": "Cableado1",
    	"Construccioncercana": "Construccion1",
    	"Observacionesdelsitio": "Obs1",
    	"Urgenciadetrabajo": "Urgencia1",
    	"Justificacion": "Justify1",
    	"Inspector": "Boton1",
    	"Fechadecarga de inspeccion": "Fecha carga1",
    	"Codigotrabajo": "Cod trabajo1",
    	"Lote": "Lote1",
    	"ESTADO": "Estado1",
    	"Gestion": "Gestion1",
    	"DetalledeGestion": "Detalle1",
    	"EquipodeTrabajo": "Equipo Trabajo1",
    	"FechaProgramada": "Fecha programada1",
    	"FechadeSolucion": "Fecha Solucion1",
    	"OrdendeTrabajo": "OT1",
    },
    {
    	"Reclamo": "2",
    	"Medio": "Medio2",
    	"Fuente": "Fuente2",
    	"Fechadereclamo": "Fecha reclamo 2",
    	"NombreyApellido": "Nombre y apellido 2",
    	"DNI": "DNI 2",
    	"Celular": "Celular 2",
    	"Telefono": "Teléfono 2",
    	"Mail": "Mail 2",
    	"Calle": "Calle 2",
    	"Altura": "Altura 2",
    	"Edificio": "Edificio 2",
    	"Depto": "Depto 2",
    	"Entrecalle1": "EC 2-1",
    	"Entrecalle2": "EC 2-2",
    	"Localidad": "Localidad 2",
    	"ReclamoB": "ReclamoB 2",
    	"Urgencia": "Urgencia 2",
        "Detalledelreclamo": "Detalle 2",
    	"FechadeCarga": "Fecha Carga 2",
    	"ID": "ID 2",
    	"Norequiereinspeccion": "NRI 2",
    	"Fechadeinspeccion": "Fecha Insp 2",
    	"Trabajoarealizar": "Trabajo a ralizar 2",
    	"Especie": "Especie 2",
    	"Altura(m)": "Altura 2",
    	"Dap(cm)": "Dap 2",
    	"Cableadocercano": "Cableado 2",
    	"Construccioncercana": "Construccion 2",
    	"Observacionesdelsitio": "Obs 2",
    	"Urgenciadetrabajo": "Urgencia 2",
    	"Justificacion": "Justify 2",
    	"Inspector": "Boton 2",
    	"Fechadecarga de inspeccion": "Fecha carga 2",
    	"Codigotrabajo": "Cod trabajo 2",
    	"Lote": "Lote1 2",
    	"ESTADO": "Estado 2",
    	"Gestion": "Gestion 2",
    	"DetalledeGestion": "Detalle 2",
    	"EquipodeTrabajo": "Equipo Trabajo 2",
    	"FechaProgramada": "Fecha programada 2",
    	"FechadeSolucion": "Fecha Solucion 2",
    	"OrdendeTrabajo": "OT 2",
    },
    {
    	"Reclamo": "3",
    	"Medio": "Medio 3",
    	"Fuente": "Fuente 3",
    	"Fechadereclamo": "Fecha reclamo 3",
    	"NombreyApellido": "Nombre y apellido 3",
    	"DNI": "DNI 3",
    	"Celular": "Celular 3",
    	"Telefono": "Teléfono 3",
    	"Mail": "Mail 3",
    	"Calle": "Calle 3",
    	"Altura": "Altura 3",
    	"Edificio": "Edificio 3",
    	"Depto": "Depto 3",
    	"Entrecalle1": "EC 3-1",
    	"Entrecalle2": "EC 3-2",
    	"Localidad": "Localidad 3",
    	"ReclamoB": "ReclamoB 3",
    	"Urgencia": "Urgencia 3",
    	"Detalledelreclamo": "Detalle 3",
    	"FechadeCarga": "Fecha Carga 3",
    	"ID": "ID 3",
    	"Norequiereinspeccion": "NRI 3",
    	"Fechadeinspeccion": "Fecha Insp 3",
    	"Trabajoarealizar": "Trabajo a ralizar 3",
    	"Especie": "Especie 3",
    	"Altura(m)": "Altra 3",
    	"Dap(cm)": "Dap 3",
    	"Cableadocercano": "Cableado 3",
    	"Construccioncercana": "Construccion 3",
    	"Observacionesdelsitio": "Obs 3",
    	"Urgenciadetrabajo": "Urgencia 3",
    	"Justificacion": "Justify 3",
    	"Inspector": "Boton 3",
    	"Fechadecarga de inspeccion": "Fecha carga 3",
    	"Codigotrabajo": "Cod trabajo 3",
    	"Lote": "Lote 3",
    	"ESTADO": "Estado 3",
    	"Gestion": "Gestion 3",
    	"DetalledeGestion": "Detalle 3",
    	"EquipodeTrabajo": "Equipo Trabajo 3",
    	"FechaProgramada": "Fecha programada 3",
    	"FechadeSolucion": "Fecha Solucion 3",
    	"OrdendeTrabajo": "OT 3",
    },
    {
    	"Reclamo": "4",
    	"Medio": "Medio 4",
    	"Fuente": "Fuente 4",
    	"Fechadereclamo": "Fecha reclamo 4",
    	"NombreyApellido": "Nombre y apellido 4",
    	"DNI": "DNI 4",
    	"Celular": "Celular 4",
    	"Telefono": "Teléfono 4",
    	"Mail": "Mail 4",
    	"Calle": "Calle 4",
    	"Altura": "Altura 4",
    	"Edificio": "Edificio 4",
    	"Depto": "Depto 4",
    	"Entrecalle1": "EC 4-1",
    	"Entrecalle2": "EC 4-2",
    	"Localidad": "Localidad 4",
    	"ReclamoB": "ReclamoB 4",
    	"Urgencia": "Urgencia 4",
    	"Detalledelreclamo": "Detalle 4",
    	"FechadeCarga": "Fecha Carga 4",
    	"ID": "ID 4",
    	"Norequiereinspeccion": "NRI 4",
    	"Fechadeinspeccion": "Fecha Insp 4",
    	"Trabajoarealizar": "Trabajo a ralizar 4",
    	"Especie": "Especie 4",
    	"Altura(m)": "Altura 4",
    	"Dap(cm)": "Dap 4",
    	"Cableadocercano": "Cableado 4",
    	"Construccioncercana": "Construccion 4",
    	"Observacionesdelsitio": "Obs 4",
    	"Urgenciadetrabajo": "Urgencia 4",
    	"Justificacion": "Justify 4",
    	"Inspector": "Boton 4",
    	"Fechadecargadeinspeccion": "Fecha carga 4",
    	"Codigotrabajo": "Cod trabajo 4",
    	"Lote": "Lote 4",
    	"ESTADO": "Estado 4",
    	"Gestion": "Gestion 4",
    	"DetalledeGestion": "Detalle 4",
    	"EquipodeTrabajo": "Equipo Trabajo 4",
    	"FechaProgramada": "Fecha programada 4",
    	"FechadeSolucion": "Fecha Solucion 4",
    	"OrdendeTrabajo": "OT 4",
    },
    {
    	"Reclamo": "5",
    	"Medio": "Medio 5",
    	"Fuente": "Fuente 5",
    	"Fechadereclamo": "Fecha reclamo 5",
    	"NombreyApellido": "Nombre y apellido 5",
    	"DNI": "DNI 5",
    	"Celular": "Celular 5",
    	"Telefono": "Teléfono 5",
    	"Mail": "Mail 5",
    	"Calle": "Calle 5",
    	"Altura": "Altura 5",
    	"Edificio": "Edificio 5",
    	"Depto": "Depto 5",
    	"Entrecalle1": "EC 5-1",
    	"Entrecalle2": "EC 5-2",
    	"Localidad": "Localidad 5",
    	"ReclamoB": "ReclamoB 5",
    	"Urgencia": "Urgencia 5",
    	"Detalledelreclamo": "Detalle 5",
    	"FechadeCarga": "Fecha Carga 5",
    	"ID": "ID 5",
    	"Norequiereinspeccion": "NRI 5",
    	"Fechadeinspeccion": "Fecha Insp 5",
    	"Trabajoarealizar": "Trabajo a ralizar 5",
    	"Especie": "Especie 5",
    	"Altura(m)": "Altra 5",
    	"Dap(cm)": "Dap 5",
    	"Cableadocercano": "Cableado 5",
    	"Construccioncercana": "Construccion 5",
    	"Observacionesdelsitio": "Obs 5",
    	"Urgenciadetrabajo": "Urgencia 5",
    	"Justificacion": "Justify 5",
    	"Inspector": "Boton 5",
    	"Fechadecarga de inspeccion": "Fecha carga 5",
    	"Codigotrabajo": "Cod trabajo 5",
    	"Lote": "Lote 5",
    	"ESTADO": "Estado 5",
    	"Gestion": "Gestion 5",
    	"DetalledeGestion": "Detalle 5",
    	"EquipodeTrabajo": "Equipo Trabajo 5",
    	"FechaProgramada": "Fecha programada 5",
    	"FechadeSolucion": "Fecha Solucion 5",
    	"OrdendeTrabajo": "OT 5",
    }
]



# Create your views here.
def gestion_inicio (request):
    
    mensaje = None
    context = {
		'reclamos': lista_reclamos,
        'mensaje': mensaje
    }

    return render(request, 'gestion/gestion_inicio.html', context)

# def gestion_editar_reclamo (request, nro_reclamo):
#     return render(request, 'gestion/gestion_editar_reclamo.html', {
#         'reclamo': lista_reclamos[nro_reclamo-1]
#     })

def gestion_editar_reclamo (request, nro_reclamo):
    mensaje = None
    if request.method == 'POST':
        # GesContactoForm, GesInspeccion, GesGestion
        form_contacto = GesContactoForm(request.POST)
        form_inspeccion = GesInspeccion(request.POST)
        form_gestion = GesGestion(request.POST)
        mensaje = 'Hemos recibido tus datos'
        # acción para tomar los datos del formulario
    elif request.method == 'GET':
        form_contacto = GesContactoForm()
        form_inspeccion = GesInspeccion()
        form_gestion = GesGestion()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    context = {
        'mensaje': mensaje,
        'reclamo': lista_reclamos[nro_reclamo-1],
        'form_contacto': form_contacto,
        'form_inspeccion': form_inspeccion,
        'form_gestion': form_gestion
    }

    return render(request, 'gestion/gestion_editar_reclamo.html', context)


def gestion_guardar_reclamo (request):
    mensaje = "Estoy en construcción"
    if request.method == 'POST':
        gestion_form = GestionForm(request.POST)
        mensaje = 'Hemos recibido tus datos'
    # acción para tomar los datos del formulario
    elif request.method == 'GET':
    	gestion_form = GestionForm()
    else:
        return HttpResponseNotAllowed(f"Método {request.method} no soportado")
    context = {
	    'mensaje': mensaje,
        'gestion_form': gestion_form
    }

    return render(request, 'gestion/gestion_editar_reclamo.html', context)
