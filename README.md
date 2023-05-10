# Sistema de Gestión de Reclamos

## Grupo 8

### Integrantes

- *Emiliano Salvadeo* - [emilianoSalva](https://github.com/emilianoSalva)
- *Ezequiel Mazzini* - [ezequielmazzini](https://github.com/ezequielmazzini)
- *Humberto Sbertoli* - [Elmerex](https://github.com/Elmerex)
- *Sergio Tolaba* - [Sergio395](https://github.com/Sergio395)
- *Cristian Lahoz* - [m415x](https://github.com/m415x)

## Descripción

El Sistema de Gestión de Reclamos de arbolado público es una aplicación web que permite la gestión de los reclamos de la ciudadanía sobre el arbolado público. La aplicación cuenta con cuatro roles de usuario, cada uno con distintas funcionalidades:

-*Operador*

- Carga de reclamos
- Seguimiento de reclamos
- Búsqueda de reclamos

-*Inspector*

- Búsqueda de reclamos
- Generación de planilla de inspección
- Carga de reclamo por árbol
- Carga de trabajo terminado
- Edición de reclamos

-*Gestor*

- Búsqueda de reclamos
- Asignación de reclamos a contratistas
- Confirmación de pagos
- Edición de reclamos

-*Administrador*

- Alta de usuarios
- Asignación de roles
- Alta de contratistas

### Flujo de funcionamiento del sistema

![Flujo de funcionamiento](diagrams/Gestión_reclamos-Flujo.png)

### UX-UI (preliminar)

![Imagen de UX-UI preliminar](diagrams/Gestión_reclamos-UX-UI_Preliminar.png)

### Formularios de reclamos

![Formularios de reclamos](diagrams/Gestión_reclamos-Formularios.png)

### Diagrama de Clases (BETA)

```mermaid
classDiagram
    class Reclamo{
        +numero: integer
        +medio: string
        +fuente: string
        +fecha: date
        +nombre: string
        +apellido: string
        +dni: integer
        +celular: integer
        +telefono_fijo: integer
        +correo_electronico: string
        +calle: string
        +altura: integer
        +edificio: string
        +departamento: string
        +entre_calle_1: string
        +entre_calle_2: string
        +localidad: string
        +reclamo: string
        +urgencia: string
        +foto: file
        +detalle: string
    }

    class Operador{
        +username: string
        +email: string
        +password: string
        +cargarReclamo()
    }

    class Inspector{
        +username: string
        +email: string
        +password: string
        +manejarReclamo()
        +cargarReclamo()
    }

    class Gestor{
        +username: string
        +email: string
        +password: string
        +manejarReclamo()
    }

    class Administrador{
        +username: string
        +email: string
        +password: string
        +manejarReclamo()
    }

    Operador "1" -- "N" Reclamo : carga
    Inspector "1" -- "N" Reclamo : maneja
    Inspector "1" -- "N" Reclamo : carga
    Gestor "1" -- "N" Reclamo : maneja
    Administrador "1" -- "N" Reclamo : maneja
```

### Diagrama Entidad-Relación (DER)

![DER](diagrams/Gestión_reclamos-DER_DB.png)

### Estructura del proyecto

```text
gestion_reclamos
├── apps
│   ├── administracion
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── base
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── gestion
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── datos_reclamos.json
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── pruebas.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── inspeccion
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── reclamos
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── __init__.py
├── diagrams
├── gestion_reclamos
│   ├── __init__.py
│   ├── .env
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   ├── administracion
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       ├── datatables-simple-demo.js
│   │       └── scripts.js
│   └── assets
│       ├── css
│       │   └── main.css
│       ├── img
│       │   ├── favicon
│       │   └── SGR.png
│       ├── js
│       │   ├── inspeccion_index.js
│       │   └── main.js
│       └── vendor
│           ├── aos
│           ├── bootstrap
│           ├── bootstrap-icons
│           ├── glightbox
│           ├── isotope-layout
│           ├── php-email-form
│           ├── purecounter
│           └── swiper
├── templates
│   ├── administracion
│   │   ├── admin_index.html
│   │   ├── edit_empresa.html
│   │   ├── edit_usuario.html
│   │   ├── empresas.html
│   │   ├── nueva_empresa.html
│   │   ├── nuevo_usuario.html
│   │   └── usuarios.html
│   ├── base
│   │   ├── base_admin.html
│   │   ├── base.html
│   │   ├── footer.html
│   │   └── index.html
│   ├── gestion
│   │   ├── gestion_editar_reclamo.html
│   │   ├── gestion_index.html
│   │   ├── gestion_inicio.html
│   │   └── gestion_prueba.html
│   ├── inspeccion
│   │   ├── inspeccion_index.html
│   │   ├── nueva_certificacion.html
│   │   └── nueva_inspeccion.html
│   └── reclamos
│       ├── nuevo_reclamo.html
│       ├── seguimiento.html
│       └── ver_reclamo.html
├── .gitignore
├── bbdd_calles.json
├── bbdd_campos.json
├── manage.py
├── README.md
└── requirements.txt
```

## Requisitos del sistema

- [Python 3.9 o superior](https://www.python.org/downloads/)
- [PostgreSQL 14 o superior](https://www.postgresql.org/download/)
- [GIT 2.40 o superior](https://git-scm.com/downloads)

## Instalación

1. Clonar el repositorio desde git bash

    >```bash
    >git clone https://github.com/Sergio395/gestion_reclamos.git
    >```

2. Acceder a la carpeta del proyecto

    >```bash
    >cd ruta/gestion_reclamos
    >```

3. Crear un entorno virtual

    >```bash
    >python -m venv "nombre_entorno_virtual" 
    >```

4. Activar el entorno virtual

    >*Linux / macOS*
    >
    >```bash
    >ruta_al_entorno_virtual/nombre_entorno_virtual/bin/activate
    >```
    >
    >*Windows*
    >
    >```bash
    >ruta_al_entorno_virtual\nombre_entorno_virtual\Scripts\activate
    >```

5. Instalar las dependencias

    >```bash
    >pip install -r requirements.txt
    >```

6. Crear las tablas de la base de datos

    >```bash
    >python manage.py migrate
    >````

<!-- 7. Crear un usuario administrador

    >```bash
    >python manage.py createsuperuser
    >```` -->
7. Crea un archivo '.env' dentro de la carpeta 'gestion_reclamos' con los siguientes parámetros

    >```text
    >SECRET_KEY =
    >DEBUG = True
    >DATABASE_NAME =
    >DATABASE_HOST = 'localhost'
    >DATABASE_PORT = '5432' # puerto por defecto
    >DATABASE_USER = 'postgres' # usuario por defecto
    >DATABASE_PASSWORD =
    >````

8. Ejecutar el servidor local

    >```bash
    >python manage.py runserver
    >````

9.  Acceder a <http://localhost:8000/> en el navegador

<!-- ## Ejecutando las pruebas

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue

_Agrega notas adicionales sobre como hacer deploy_ -->

## Construido con

- [Django 3.2](https://docs.djangoproject.com/en/4.1/releases/3.2/) - El framework web utilizado
- [Bootstrap 5.2](https://getbootstrap.com/docs/5.2/getting-started/introduction/) - El framework css implementado

<!-- ## Contribuyendo

Este proyecto está abierto a contribuciones de la comunidad. Si desea contribuir, por favor lea [CONTRIBUTING.md](CONTRIBUTING.md) para obtener más información. -->

<!-- ## Versionado

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags). -->

<!-- ## Autores

- *Emiliano Salvadeo* - [emilianoSalva](https://github.com/emilianoSalva)
- *Ezequiel Mazzini* - [ezequielmazzini](https://github.com/ezequielmazzini)
- *Humberto Sbertoli* - [Elmerex](https://github.com/Elmerex)
- *Sergio Tolaba* - [Sergio395](https://github.com/Sergio395)
- *Cristian Lahoz* - [m415x](https://github.com/m415x) -->

<!-- ## Licencia

Este proyecto está disponible bajo la Licencia MIT. Consulte [LICENSE.md](LICENSE.md) para obtener más información. -->
