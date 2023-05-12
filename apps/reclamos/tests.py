from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import date
from .models import Fuente, Denunciante, Arbol, Reclamo


# Create your tests here.
class FuenteModelTest(TestCase):

    def setUp(self):
        Fuente.objects.create(fuente='O1')

    def test_str_method(self):
        fuente = Fuente.objects.get(fuente='O1')
        self.assertEqual(str(fuente), 'O1 => Oficina 1')


class DenuncianteModelTest(TestCase):

    def setUp(self):
        Denunciante.objects.create(nombre='Juan', apellido='Pérez', dni=12345678,
                                   correo_electronico='juan.perez@mail.com', celular=1555555555,
                                   telefono_fijo=4444444)

    def test_str_method(self):
        denunciante = Denunciante.objects.get(dni=12345678)
        self.assertEqual(str(denunciante), 'Pérez, Juan')


class ArbolModelTest(TestCase):

    def setUp(self):
        Arbol.objects.create(calle='Calle Falsa', numeracion=123, entre_calle_1='Calle 1',
                              entre_calle_2='Calle 2', localidad='Ciudad', edificio='Edificio 1',
                              departamento='Departamento A', latitud=-34.603722, longitud=-58.381592,
                              especie='Eucalipto', altura=5.5)

    def test_str_method(self):
        arbol = Arbol.objects.get(especie='Eucalipto')
        self.assertEqual(str(arbol), 'Eucalipto [lat -34.603722, lng -58.381592]')


class ReclamoModelTest(TestCase):

    def setUp(self):
        fuente = Fuente.objects.create(fuente='O1')
        denunciante = Denunciante.objects.create(nombre='Juan', apellido='Pérez', dni=12345678,
                                                 correo_electronico='juan.perez@mail.com', celular=1555555555,
                                                 telefono_fijo=4444444)
        arbol = Arbol.objects.create(calle='Calle Falsa', numeracion=123, entre_calle_1='Calle 1',
                                      entre_calle_2='Calle 2', localidad='Ciudad', edificio='Edificio 1',
                                      departamento='Departamento A', latitud=-34.603722, longitud=-58.381592,
                                      especie='Eucalipto', altura=5.5)
        Reclamo.objects.create(numero=1, medio='Email', fuente=fuente, fecha=date.today(),
                                reclamo='El árbol está en mal estado', urgencia='Alta',
                                detalle='Se observan ramas rotas', reclamo_valido=True).denunciantes.add(denunciante)
        Reclamo.objects.get(numero=1).arboles.add(arbol)

    def test_str_method(self):
        reclamo = Reclamo.objects.get(numero=1)
        self.assertEqual(str(reclamo), 'Reclamo 1')

    def test_numero_uniqueness(self):
        with self.assertRaises(ValidationError):
            Reclamo.objects.create(numero=1, medio='Email', fuente=Fuente.objects.create(fuente='O2'), fecha=date.today(),
                                    reclamo='El árbol está en mal estado', urgencia='Media', reclamo_valido=True)

    def test_denunciantes_related_name(self):
        reclamo = Reclamo.objects.get(numero=1)
        denunciantes = reclamo.denunciantes.all()
        self.assertEqual(len(denunciantes), 1)
        denunciante = denunciantes[0]
        self.assertEqual(str(denunciante), 'Juan Pérez')
        reclamo_2 = Reclamo.objects.create(numero=2, medio='Telefono', fuente=Fuente.objects.create(fuente='O1'),
                                            fecha=date.today(), reclamo='El árbol está demasiado grande', urgencia='Baja',
                                            detalle='No representa un peligro', reclamo_valido=True)
        reclamo_2.denunciantes.add(denunciante)
        denunciantes_2 = reclamo_2.denunciantes.all()
        self.assertEqual(len(denunciantes_2), 1)
        denunciante_2 = denunciantes_2[0]
        self.assertEqual(str(denunciante_2), 'Juan Pérez')

    def test_arboles_related_name(self):
        reclamo = Reclamo.objects.get(numero=1)
        arboles = reclamo.arboles.all()
        self.assertEqual(len(arboles), 1)
        arbol = arboles[0]
        self.assertEqual(str(arbol), 'Calle Falsa 123')
        reclamo_2 = Reclamo.objects.create(numero=2, medio='Telefono', fuente=Fuente.objects.create(fuente='O1'),
                                            fecha=date.today(), reclamo='El árbol está demasiado grande', urgencia='Baja',
                                            detalle='No representa un peligro', reclamo_valido=True)
        arbol_2 = Arbol.objects.create(calle='Otra Calle', numeracion=321, entre_calle_1='Calle 3', entre_calle_2='Calle 4',
                                        localidad='Ciudad', edificio='Edificio 2', departamento='Departamento B',
                                        latitud=-34.604048, longitud=-58.380984, especie='Pino', altura=8)
        reclamo_2.arboles.add(arbol_2)
        arboles_2 = reclamo_2.arboles.all()
        self.assertEqual(len(arboles_2), 1)
        arbol_2 = arboles_2[0]
        self.assertEqual(str(arbol_2), 'Otra Calle 321')

    def test_create_reclamo_with_denunciante(self):
        denunciante = Denunciante.objects.get(nombre='Juan')
        reclamo_2 = Reclamo.objects.create(numero=2, medio='Telefono', fuente=Fuente.objects.create(fuente='O1'),
                                            fecha=date.today(), reclamo='El árbol está demasiado grande', urgencia='Baja',
                                            detalle='No representa un peligro', reclamo_valido=True, denunciantes=[denunciante])
        denunciantes_2 = reclamo_2.denunciantes.all()
        self.assertEqual(len(denunciantes_2), 1)
        denunciante_2 = denunciantes_2[0]
        self.assertEqual(str(denunciante_2), 'Juan Pérez')

    def test_create_reclamo_with_arbol(self):
        arbol = Arbol.objects.get(calle='Calle Falsa', numeracion=123)
        reclamo_2 = Reclamo.objects.create(numero=2, medio='Telefono', fuente=Fuente.objects.create(fuente='O2'),
                                        fecha=date.today(),
        reclamo='El árbol interfiere con los cables de luz', urgencia='Media',
        detalle='Se observa contacto entre ramas y cables', reclamo_valido=True)
        reclamo_2.arboles.add(arbol)
        reclamo_2.save()
        self.assertEqual(reclamo_2.arboles.count(), 1)
        self.assertEqual(reclamo_2.arboles.first(), arbol)

    def test_create_reclamo_with_denunciante(self):
        denunciante = Denunciante.objects.create(nombre='María', apellido='García', dni=23456789,
        correo_electronico='maria.garcia@mail.com', celular=1566666666,
        telefono_fijo=5555555)
        reclamo_3 = Reclamo.objects.create(numero=3, medio='Telefono', fuente=Fuente.objects.create(fuente='O3'),
                                        fecha=date.today(), reclamo='El árbol está dañando la vereda',
                                        urgencia='Baja', detalle='Raíces levantando baldosas',
                                        reclamo_valido=True)
        reclamo_3.denunciantes.add(denunciante)
        reclamo_3.save()
        self.assertEqual(reclamo_3.denunciantes.count(), 1)
        self.assertEqual(reclamo_3.denunciantes.first(), denunciante)

    def test_create_reclamo_with_multiple_arboles(self):
        arbol_1 = Arbol.objects.create(calle='Calle Falsa', numeracion=124, entre_calle_1='Calle 1',
        entre_calle_2='Calle 2', localidad='Ciudad', edificio='Edificio 1',
        departamento='Departamento A', latitud=-34.603722, longitud=-58.381592,
        especie='Eucalipto', altura=5.5)
        arbol_2 = Arbol.objects.create(calle='Calle Falsa', numeracion=125, entre_calle_1='Calle 1',
                                    entre_calle_2='Calle 2', localidad='Ciudad', edificio='Edificio 1',
                                    departamento='Departamento A', latitud=-34.603722, longitud=-58.381592,
                                    especie='Pino', altura=4.0)
        reclamo_4 = Reclamo.objects.create(numero=4, medio='Email', fuente=Fuente.objects.create(fuente='O4'),
        fecha=date.today(), reclamo='Los árboles están obstaculizando el paso',
        urgencia='Media', detalle='Ramificaciones bajas', reclamo_valido=True)
        reclamo_4.arboles.add(arbol_1, arbol_2)
        reclamo_4.save()
        self.assertEqual(reclamo_4.arboles.count(), 2)
        self.assertIn(arbol_1, reclamo_4.arboles.all())
        self.assertIn(arbol_2, reclamo_4.arboles.all())
