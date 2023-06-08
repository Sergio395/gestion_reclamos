from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


class MedioChoices(TextChoices):
    """Clase que representa las opciones de medio de un reclamo.

    Las opciones son limitadas y predefinidas, y se utilizan para
    restringir los valores permitidos en el campo 'medio' del modelo
    ReclamoModel.
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


class FuenteChoices(TextChoices):
    """Clase que representa las opciones de fuente de un reclamo.

    Las opciones son limitadas y predefinidas, y se utilizan para
    restringir los valores permitidos en el campo 'fuente' del modelo
    ReclamoModel.
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


class LocalidadChoices(TextChoices):
    """Clase que representa las opciones de localidad de un reclamo.

    Las opciones son limitadas y predefinidas, y se utilizan para
    restringir los valores permitidos en el campo 'localidad' del modelo
    ReclamoModel.
    """
    BLANK = "", _("")
    NDAB = "9A", _("9 de Abril")
    CANN = "CA", _("Canning")
    EJAG = "EJ", _("El Jagüel")
    LGUI = "LG", _("Luis Guillón")
    MGRA = "MG", _("Monte Grande")


class ReclamoChoices(TextChoices):
    """Clase que representa las opciones de tipo de reclamo.

    Las opciones son limitadas y predefinidas, y se utilizan para
    restringir los valores permitidos en el campo 'reclamo' del modelo
    ReclamoModel.
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


class UrgenciaChoices(TextChoices):
    """Clase que representa las opciones de urgencia de un reclamo.

    Las opciones son limitadas y predefinidas, y se utilizan para
    restringir los valores permitidos en el campo 'urgencia' del modelo
    ReclamoModel.
    """
    BLANK = "", _("")
    BAJA = "1", _("Baja")
    MEDIA = "2", _("Media")
    ALTA = "3", _("Alta")


class TrabajoChoices(TextChoices):
    """Clase que representa las opciones de trabajos a realizar en un árbol.

    Las opciones son limitadas y predefinidas, y se utilizan para
    restringir los valores permitidos en el campo 'tipo_de_trabajo' del modelo
    TrabajoModel.
    """
    BLANK = "", _("")
    PODI = "PI", _("Poda Integral")
    PODR = "PR", _("Poda Reductiva")
    PODD = "PD", _("Poda de Despeje")
    TALA = "T", _("Tala")
    COR = "CR", _("Corte de Raíces")
    EXT = "E", _("Extracción")


class AlturaChoices(TextChoices):
    """Clase que representa las opciones altura de un árbol.

    Las opciones son limitadas y predefinidas, y se utilizan para
    restringir los valores permitidos en el campo 'altura_arbol' del modelo
    TrabajoModel.
    """
    BLANK = "", _("")
    AM4 = "1", _("Árbol < 4m")
    A4Y8 = "2", _("4m < Árbol < 8m")
    A8Y12 = "3", _("8m < Árbol < 12m")
    A12Y16 = "4", _("12m < Árbol < 16m")
    A16Y20 = "5", _("16m < Árbol < 20m")
    AM20 = "6", _("Árbol > 20m")


class DisposicionChoices(TextChoices):
    """Clase que representa las opciones de disposición de un árbol.

    Las opciones son limitadas y predefinidas, y se utilizan para
    restringir los valores permitidos en el campo 'disposición' del modelo
    TrabajoModel.
    """
    LINE = "", _("Lineal")
    POINT = "*", _("Puntual")


class RiesgoChoices(TextChoices):
    """Clase que representa las opciones de riesgo de un árbol.

    Las opciones son limitadas y predefinidas, y se utilizan para
    restringir los valores permitidos en el campo 'riesgo' del modelo
    InspeccionModel.
    """
    BLANK = "", _("")
    # ! EJEMPLO
    BAJO = "1", _("Bajo")
    MEDIO = "2", _("Medio")
    ALTO = "3", _("Alto")
