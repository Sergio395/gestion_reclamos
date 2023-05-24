from django.db import models
from django.utils.translation import gettext_lazy as _
# from ..inspeccion.models import ArbolModel

# Create your models here.
class DenuncianteModel(models.Model):
    """
    Modelo que representa a la persona que realizó un reclamo.
    Contiene información personal acerca del denunciante,
    como su nombre, apellido, DNI, número de celular,
    número de teléfono fijo y correo electrónico.
    """
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI")
    celular = models.IntegerField(verbose_name="Celular")
    telefono_fijo = models.IntegerField(verbose_name="Telefono fijo")
    correo_electronico = models.EmailField(verbose_name="Correo electrónico")

    def __str__(self):
        return f"{self.apellido}, {self.nombre} DNI: {self.dni}"


class ReclamoModel(models.Model):
    """
    Modelo que representa un reclamo realizado por un denunciante.
    Contiene información relevante acerca del reclamo,
    como su número de identificación, medio por el cual fue realizado,
    fuente del reclamo, fecha en que se realizó, datos del denunciante,
    datos del árbol afectado, tipo del reclamo, grado de urgencia,
    una foto del incidente (opcional), y un detalle del mismo.
    """

    class MedioChoices(models.TextChoices):
        """
        Clase que representa las opciones de medio de un reclamo.
        Las opciones son limitadas y predefinidas, y se utilizan para
        restringir los valores permitidos en el campo 'medio' del modelo
        Reclamo.
        """
        BLANK = "", _("")
        CALLE = "06", _("Calle")
        CAV = "00", _("CAV")
        EXP = "01", _("Expediente")
        MAIL = "07", _("Correo electrónico")
        NOTA = "05", _("Nota")
        RED = "03", _("Redes sociales")
        TEL = "04", _("Teléfono Oficina")
        VENT = "02", _("Ventanilla")
        WAP = "08", _("WAP")

    class FuenteChoices(models.TextChoices):
        """
        Clase que representa las opciones de fuente de un reclamo.
        Las opciones son limitadas y predefinidas, y se utilizan para
        restringir los valores permitidos en el campo 'fuente' del modelo
        Reclamo.
        """
        BLANK = "", _("")
        ARQ = "1", _("Arquitectura")
        CAV = "2", _("CAV")
        CERE = "3", _("Ceremonial")
        COM = "4", _("COM")
        CDEL = "5", _("Consejo Deliberante")
        CESC = "6", _("Consejo Escolar")
        CULT = "7", _("Cultura")
        DEFC = "8", _("Defensa Civil")
        D9DA = "9", _("Delegación 9 de Julio")
        DCAN = "10", _("Delegación Canning")
        DEJ = "11", _("Delegación El Jagüel")
        DLG = "12", _("Delegación Luis Guillón")
        DMAL = "13", _("Delegación Malvinas")
        DMGS = "14", _("Delegación Monte Grande Sur")
        EDES = "15", _("EDESUR S.A.")
        ECHE = "16", _("Enlace Echeverría")
        ENTI = "17", _("Entidades")
        EVER = "18", _("Espacios Verdes")
        GOB = "19", _("Gobierno")
        MAMB = "20", _("Medio Ambiente")
        MENT = "21", _("Mesa de Entrada")
        OHID = "22", _("Obras Hídricas")
        OPAR = "23", _("Obras Particulares")
        OPUB = "24", _("Obras Públicas")
        PREN = "25", _("Prensa")
        SEG = "26", _("Seguridad")
        SERV = "27", _("Servicios")
        VEC = "28", _("Vecino")

    class LocalidadChoices(models.TextChoices):
        """
        Clase que representa las opciones de localidad de un reclamo.
        Las opciones son limitadas y predefinidas, y se utilizan para
        restringir los valores permitidos en el campo 'localidad' del modelo
        Reclamo.
        """
        BLANK = "", _("")
        NDAB = "R2546787", _("9 de Abril")
        CANN = "R2546804", _("Canning")
        EJAG = "R2546834", _("El Jagüel")
        LGUI = "R2546803", _("Luis Guillón")
        MGRA = "R2546842", _("Monte Grande")

    class ReclamoChoices(models.TextChoices):
        """
        Clase que representa las opciones de tipo de reclamo.
        Las opciones son limitadas y predefinidas, y se utilizan para
        restringir los valores permitidos en el campo 'reclamo' del modelo
        Reclamo.
        """
        BLANK = "", _("")
        ACAI = "1", _("Árbol caído")
        ARCA = "2", _("Árbol con riesgo de caída")
        AELE = "3", _("Árbol electrificado")
        CDRA = "4", _("Corte de raíz")
        DCAB = "5", _("Despeje de cables")
        DLUM = "6", _("Despeje luminario")
        EXTR = "7", _("Extracción")
        INDE = "8", _("Indemnización")
        PAOA = "9", _("Panal de abejas/avispas")
        PODA = "10", _("Poda")
        PSAU = "11", _("Poda sin autorización")
        QUEJ = "12", _("Queja")
        RQUE = "13", _("Rama quebrada")
        RDPO = "14", _("Recolección de poda")
        REDA = "15", _("Revisión de estado del árbol")
        SDAR = "16", _("Solicitud de árbol")
        SDAU = "17", _("Solicitud de autorización")
        TSAU = "18", _("Tala sin autorización")

    class UrgenciaChoices(models.TextChoices):
        """
        Clase que representa las opciones de urgencia de un reclamo.
        Las opciones son limitadas y predefinidas, y se utilizan para
        restringir los valores permitidos en el campo 'urgencia' del modelo
        Reclamo.
        """
        BLANK = "", _("")
        BAJA = "1", _("Baja")
        MEDIA = "2", _("Media")
        ALTA = "3", _("Alta")

    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    medio = models.CharField(max_length=50, verbose_name="Medio",
                             choices=MedioChoices.choices,
                             default=MedioChoices.BLANK)
    numero = models.IntegerField(verbose_name="Número")
    fuente = models.CharField(max_length=50, verbose_name="Fuente",
                              choices=FuenteChoices.choices,
                              default=FuenteChoices.BLANK)
    fecha = models.DateField(verbose_name="Fecha del reclamo")
    denunciantes = models.ManyToManyField(DenuncianteModel, verbose_name="Denunciante")
    localidad = models.CharField(max_length=50, verbose_name="Localidad",
                                 choices=LocalidadChoices.choices,
                                 default=LocalidadChoices.BLANK)
    calle = models.CharField(max_length=50, verbose_name="Calle")
    altura = models.IntegerField(verbose_name="Numeración")
    edificio = models.CharField(max_length=50, verbose_name="Edificio")
    departamento = models.CharField(max_length=50, verbose_name="Departamento")
    entre_calle_1 = models.CharField(max_length=50, verbose_name="Entre calle")
    entre_calle_2 = models.CharField(max_length=50, verbose_name="y calle")
    # arboles = models.ManyToManyField(Arbol, verbose_name="Arbol")
    reclamo = models.CharField(max_length=200, verbose_name="Reclamo",
                               choices=ReclamoChoices.choices,
                               default=ReclamoChoices.BLANK)
    urgencia = models.CharField(max_length=5, verbose_name="Urgencia",
                                choices=UrgenciaChoices.choices,
                                default=UrgenciaChoices.BLANK)
    foto = models.ImageField(upload_to='img_reclamos', null=True,
                             blank=True, verbose_name="Fotos") # img_reclamos define la ruta donde se almacenan las fotos
    detalle = models.CharField(max_length=500, verbose_name="Detalles")
    eliminado = models.BooleanField(default=False)

    def __str__(self):
        return f'Reclamo {self.numero}'
