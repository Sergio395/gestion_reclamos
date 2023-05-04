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

### Diagrama de Clases

![Diagrama de clases]()

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
│   │   ├── forms.py
│   │   ├── models.py
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
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── __init__.py
├── diagrams
│   ├── Gestión_reclamos-DER_DB.png
│   ├── Gestión_reclamos-Flujo.png
│   ├── Gestión_reclamos-Formularios.png
│   └── Gestión_reclamos-UX-UI_Preliminar.png
├── gestion_reclamos
│   ├── __init__.py
│   ├── .env
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   └── assets
│       ├── css
│       │   └── main.css
│       ├── img
│       │   ├── favicon
│       │   └── SGR.png
│       ├── js
│       │   └── main.js
│       └── vendor
├── templates
│   ├── administracion
│   │   └── admin_index.html
│   ├── base
│   │   ├── base.html
│   │   ├── footer.html
│   │   └── index.html
│   ├── gestion
│   │   └── gestion_index.html
│   ├── inspeccion
│   │   ├── inspeccion_index.html
│   │   ├── nueva_certificacion.html
│   │   └── nueva_inspeccion.html
│   └── reclamos
│       ├── nuevo_reclamo.html
│       ├── seguimiento.html
│       └── ver_reclamo.html
├── .gitignore
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

    ```bash
    git clone https://github.com/Sergio395/PIG_django_gestion_reclamos.git
    ```

2. Acceder a la carpeta del proyecto

    ```bash
    cd ruta/gestion_reclamos
    ```

3. Crear un entorno virtual

    ```bash
    python -m venv "nombre_entorno_virtual" 
    ```

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

    ```bash
    pip install -r requirements.txt
    ```

6. Crear las tablas de la base de datos

    ```bash
    python manage.py migrate
    ````

<!-- 7. Crear un usuario administrador

    ```bash
    python manage.py createsuperuser
    ```` -->

7. Ejecutar el servidor local

    ```bash
    python manage.py runserver
    ````

8. Acceder a <http://localhost:8000/> en el navegador

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