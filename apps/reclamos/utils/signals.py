from django.db.models.signals import pre_save
from django.dispatch import receiver
from ..models import ReclamoModel


@receiver(pre_save, sender=ReclamoModel)
def actualizar_repitancia(sender, instance, **kwargs):
    """Actualiza el campo 'repitancia' de un reclamo antes de guardarlo.

    Esta función es utilizada como receptor (signal receiver) del evento 'pre_save' del modelo 'ReclamoModel'. Se ejecuta antes de que un reclamo sea guardado en la base de datos.

    Parámetros:
    - sender: La clase del modelo que envía la señal (ReclamoModel en este caso).
    - instance: La instancia del reclamo que está siendo guardada.
    - kwargs: Argumentos adicionales proporcionados por la señal.

    Comportamiento:
    - Si el reclamo es nuevo (no tiene una clave primaria asignada), actualiza el campo 'repitancia' basado en la cantidad de reclamos existentes con el mismo valor (en el ejemplo, el campo 'numero') incrementado en 1.
    - Si el reclamo es existente (tiene una clave primaria asignada), verifica si el valor del campo 'numero' ha cambiado. Si ha cambiado, actualiza la 'repitancia' basado en la cantidad de reclamos existentes con el nuevo valor de 'numero' incrementado en 1.
    """
    if not instance.pk:
        # Es un nuevo reclamo, actualiza la repitancia
        repitancia = ReclamoModel.objects.filter(numero=instance.numero).count() + 1
        instance.repitancia = repitancia
    else:
        # Es un reclamo existente, verifica si el número ha cambiado
        if instance.numero != ReclamoModel.objects.get(pk=instance.pk).numero:
            # El número ha cambiado, actualiza la repitancia
            repitancia = ReclamoModel.objects.filter(numero=instance.numero).count() + 1
            instance.repitancia = repitancia
