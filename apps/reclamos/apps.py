from django.apps import AppConfig


class ReclamosConfig(AppConfig):
    """Configuración de la aplicación de reclamos.

    Esta clase define la configuración específica de la aplicación de reclamos.
    Define el campo de auto-generación de claves primarias y el nombre de la aplicación.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.reclamos'

    def ready(self):
        """Método llamado cuando la aplicación está lista.

        Importa los módulos de señales de la aplicación 'reclamos' para asegurar que sean registrados y utilizados correctamente.
        """
        import apps.reclamos.utils.signals
