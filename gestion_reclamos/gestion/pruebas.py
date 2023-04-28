import json

j_data = '''
          [{
              "0":{
                  "Name": "Nick",
                  "Age": "22"
              },
              "1":{
                  "Name": "Hemank",
                  "Age": "21"
              },
              "2":{
                  "Name": "Sam",
                  "Age":"25"
              }
          }
          ]
    '''

datos_JSON = '''
    {
    "1": 
        {
        "tabla_reclamos":
            {
            "Reclamo": "1",
            "Medio": "Medio1",
            "Fuente": "Fuente1",
            "Fecha de reclamo": "Fecha reclamo 1",
            "Nombre y Apellido": "Nombre y apellido 1",
            "DNI": "DNI1",
            "Celular": "Celular 1",
            "Telefono": "Teléfono 1",
            "Mail": "Mail1",
            "Calle": "Calle1",
            "Altura": "Altura1",
            "Edificio": "Edificio1",
            "Depto": "Depto1",
            "Entre calle 1": "EC1-1",
            "Entre calle 2": "EC1-2",
            "Localidad": "Localidad1",
            "ReclamoB": "ReclamoB1",
            "Urgencia": "Urgencia1",
            "Detalle del reclamo": "Detalle1",
            "Fecha de Carga": "Fecha Carga1",
            "ID": "ID1"
            },
        "tabla_inspecciones":
            {
            "No requiere inspeccion": "NRI1",
            "Fecha de inspeccion": "Fecha Insp1",
            "Trabajo a realizar": "Trabajo a ralizar1",
            "Especie": "Especie1",
            "Altura (m)": "Altra1",
            "Dap (cm)": "Dap1",
            "Cableado cercano": "Cableado1",
            "Construccion cercana": "Construccion1",
            "Observaciones del sitio": "Obs1",
            "Urgencia de trabajo": "Urgencia1",
            "Justificacion": "Justify1",
            "Inspector": "Boton1",
            "Fecha de carga de inspeccion": "Fecha carga1",
            "Codigo trabajo": "Cod trabajo1",
            "Lote": "Lote1"
        },
        "tabla_gestion":
            {
            "ESTADO": "Estado1",
            "Gestion": "Gestion1",
            "Detalle de Gestion": "Detalle1",
            "Equipo de Trabajo": "Equipo Trabajo1",
            "Fecha Programada": "Fecha programada1",
            "Fecha de Solucion":"Fecha Solucion1",
            "Orden de Trabajo": "OT1" 
            }   
        },
    "2":
        {
        "tabla_reclamos":
            {
            "Reclamo": "2",
            "Medio": "Medio2",
            "Fuente": "Fuente2",
            "Fecha de reclamo": "Fecha reclamo 2",
            "Nombre y Apellido": "Nombre y apellido 2",
            "DNI": "DNI 2",
            "Celular": "Celular 2",
            "Telefono": "Teléfono 2",
            "Mail": "Mail 2",
            "Calle": "Calle 2",
            "Altura": "Altura 2",
            "Edificio": "Edificio 2",
            "Depto": "Depto 2",
            "Entre calle 1": "EC 2-1",
            "Entre calle 2": "EC 2-2",
            "Localidad": "Localidad 2",
            "ReclamoB": "ReclamoB 2",
            "Urgencia": "Urgencia 2",
            "Detalle del reclamo": "Detalle 2",
            "Fecha de Carga": "Fecha Carga 2",
            "ID": "ID 2"
            },
        "tabla_inspecciones":    
            {
            "No requiere inspeccion": "NRI 2",
            "Fecha de inspeccion": "Fecha Insp 2",
            "Trabajo a realizar": "Trabajo a ralizar 2",
            "Especie": "Especie 2",
            "Altura (m)": "Altura 2",
            "Dap (cm)": "Dap 2",
            "Cableado cercano": "Cableado 2",
            "Construccion cercana": "Construccion 2",
            "Observaciones del sitio": "Obs 2",
            "Urgencia de trabajo": "Urgencia 2",
            "Justificacion": "Justify 2",
            "Inspector": "Boton 2",
            "Fecha de carga de inspeccion": "Fecha carga 2",
            "Codigo trabajo": "Cod trabajo 2",
            "Lote": "Lote1 2"
            },
        "tabla_gestion":
            {
            "ESTADO": "Estado 2",
            "Gestion": "Gestion 2",
            "Detalle de Gestion": "Detalle 2",
            "Equipo de Trabajo": "Equipo Trabajo 2",
            "Fecha Programada": "Fecha programada 2",
            "Fecha de Solucion": "Fecha Solucion 2",
            "Orden de Trabajo": "OT 2" 
            }
        },
    "3":
        {
        "tabla_reclamos":
            {
            "Reclamo": "3",
            "Medio": "Medio 3",
            "Fuente": "Fuente 3",
            "Fecha de reclamo": "Fecha reclamo 3",
            "Nombre y Apellido": "Nombre y apellido 3",
            "DNI": "DNI 3",
            "Celular": "Celular 3",
            "Telefono": "Teléfono 3",
            "Mail": "Mail 3",
            "Calle": "Calle 3",
            "Altura": "Altura 3",
            "Edificio": "Edificio 3",
            "Depto": "Depto 3",
            "Entre calle 1": "EC 3-1",
            "Entre calle 2": "EC 3-2",
            "Localidad": "Localidad 3",
            "ReclamoB": "ReclamoB 3",
            "Urgencia": "Urgencia 3",
            "Detalle del reclamo": "Detalle 3",
            "Fecha de Carga": "Fecha Carga 3",
            "ID": "ID 3"
            },
        "tabla_inspecciones":
            {
            "No requiere inspeccion": "NRI 3",
            "Fecha de inspeccion": "Fecha Insp 3",
            "Trabajo a realizar": "Trabajo a ralizar 3",
            "Especie": "Especie 3",
            "Altura (m)": "Altra 3",
            "Dap (cm)": "Dap 3",
            "Cableado cercano": "Cableado 3",
            "Construccion cercana": "Construccion 3",
            "Observaciones del sitio": "Obs 3",
            "Urgencia de trabajo": "Urgencia 3",
            "Justificacion": "Justify 3",
            "Inspector": "Boton 3",
            "Fecha de carga de inspeccion": "Fecha carga 3",
            "Codigo trabajo": "Cod trabajo 3",
            "Lote": "Lote 3"
            },
        "tabla_gestion":    
            {
            "ESTADO": "Estado 3",
            "Gestion": "Gestion 3",
            "Detalle de Gestion": "Detalle 3",
            "Equipo de Trabajo": "Equipo Trabajo 3",
            "Fecha Programada": "Fecha programada 3",
            "Fecha de Solucion": "Fecha Solucion 3",
            "Orden de Trabajo": "OT 3" 
            }   
        },
    "4":
        {
        "tabla_reclamos":
            {
            "Reclamo": "4",
            "Medio": "Medio 4",
            "Fuente": "Fuente 4",
            "Fecha de reclamo": "Fecha reclamo 4",
            "Nombre y Apellido": "Nombre y apellido 4",
            "DNI": "DNI 4",
            "Celular": "Celular 4",
            "Telefono": "Teléfono 4",
            "Mail": "Mail 4",
            "Calle": "Calle 4",
            "Altura": "Altura 4",
            "Edificio": "Edificio 4",
            "Depto": "Depto 4",
            "Entre calle 1": "EC 4-1",
            "Entre calle 2": "EC 4-2",
            "Localidad": "Localidad 4",
            "ReclamoB": "ReclamoB 4",
            "Urgencia": "Urgencia 4",
            "Detalle del reclamo": "Detalle 4",
            "Fecha de Carga": "Fecha Carga 4",
            "ID": "ID 4"
            },
        "tabla_inspecciones":
            {
            "No requiere inspeccion": "NRI 4",
            "Fecha de inspeccion": "Fecha Insp 4",
            "Trabajo a realizar": "Trabajo a ralizar 4",
            "Especie": "Especie 4",
            "Altura (m)": "Altura 4",
            "Dap (cm)": "Dap 4",
            "Cableado cercano": "Cableado 4",
            "Construccion cercana": "Construccion 4",
            "Observaciones del sitio": "Obs 4",
            "Urgencia de trabajo": "Urgencia 4",
            "Justificacion": "Justify 4",
            "Inspector": "Boton 4",
            "Fecha de carga de inspeccion": "Fecha carga 4",
            "Codigo trabajo": "Cod trabajo 4",
            "Lote": "Lote 4"
            },
        "tabla_gestion":
            {
            "ESTADO": "Estado 4",
            "Gestion": "Gestion 4",
            "Detalle de Gestion": "Detalle 4",
            "Equipo de Trabajo": "Equipo Trabajo 4",
            "Fecha Programada": "Fecha programada 4",
            "Fecha de Solucion":"Fecha Solucion 4",
            "Orden de Trabajo":"OT 4" 
            }
        },
    "5":
        {
        "tabla_reclamos":
            {
            "Reclamo": "5",
            "Medio": "Medio 5",
            "Fuente": "Fuente 5",
            "Fecha de reclamo": "Fecha reclamo 5",
            "Nombre y Apellido": "Nombre y apellido 5",
            "DNI": "DNI 5",
            "Celular": "Celular 5",
            "Telefono": "Teléfono 5",
            "Mail": "Mail 5",
            "Calle": "Calle 5",
            "Altura": "Altura 5",
            "Edificio": "Edificio 5",
            "Depto": "Depto 5",
            "Entre calle 1": "EC 5-1",
            "Entre calle 2": "EC 5-2",
            "Localidad": "Localidad 5",
            "ReclamoB": "ReclamoB 5",
            "Urgencia": "Urgencia 5",
            "Detalle del reclamo": "Detalle 5",
            "Fecha de Carga": "Fecha Carga 5",
            "ID": "ID 5"
            },
        "tabla_inspecciones":
            {
            "No requiere inspeccion": "NRI 5",
            "Fecha de inspeccion": "Fecha Insp 5",
            "Trabajo a realizar": "Trabajo a ralizar 5",
            "Especie": "Especie 5",
            "Altura (m)": "Altra 5",
            "Dap (cm)": "Dap 5",
            "Cableado cercano": "Cableado 5",
            "Construccion cercana": "Construccion 5",
            "Observaciones del sitio": "Obs 5",
            "Urgencia de trabajo": "Urgencia 5",
            "Justificacion": "Justify 5",
            "Inspector": "Boton 5",
            "Fecha de carga de inspeccion": "Fecha carga 5",
            "Codigo trabajo": "Cod trabajo 5",
            "Lote": "Lote 5"
            },
        "tabla_gestion": 
            {
            "ESTADO": "Estado 5",
            "Gestion": "Gestion 5",
            "Detalle de Gestion": "Detalle 5",
            "Equipo de Trabajo": "Equipo Trabajo 5",
            "Fecha Programada": "Fecha programada 5",
            "Fecha de Solucion":"Fecha Solucion 5",
            "Orden de Trabajo": "OT 5" 
            }
        }
    }
'''

d = json.loads(j_data)
dj = json.loads(datos_JSON)

archivo = open("datos_reclamos.json", 'r')
datos = json.loads( archivo.read())

print(d[0])
print(dj["1"]["tabla_inspecciones"]["No requiere inspeccion"])
print(datos["2"]["tabla_inspecciones"]["No requiere inspeccion"])