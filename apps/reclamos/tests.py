from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Denunciante, Arbol, Reclamo


class DenuncianteModelTests(TestCase):

    def test_str(self):
        denunciante = Denunciante(nombre="Juan", apellido="Pérez")
        self.assertEqual(str(denunciante), "Pérez, Juan")


class ArbolModelTests(TestCase):

    def test_str(self):
        arbol = Arbol(especie="Ficus", latitud="-34.603722", longitud="-58.381592")
        self.assertEqual(str(arbol), "Ficus [lat -34.603722, lng -58.381592]")


class ReclamoModelTests(TestCase):

    def setUp(self):
        self.denunciante = Denunciante.objects.create(
            nombre="Juan",
            apellido="Pérez",
            dni=12345678,
            correo_electronico="juanperez@example.com",
            celular=1555555555,
            telefono_fijo=1155555555
        )
        self.arbol = Arbol.objects.create(
            calle="Av. Corrientes",
            numeracion=1234,
            entre_calle_1="Larrea",
            entre_calle_2="Aguero",
            localidad="CABA",
            edificio="",
            departamento="",
            latitud="-34.603722",
            longitud="-58.381592",
            especie="Ficus",
            altura=5.0
        )

    def test_str(self):
        reclamo = Reclamo(
            numero=1,
            medio="Web",
            fuente="1",
            fecha=timezone.now(),
            reclamo="Rama caída",
            urgencia="1"
        )
        reclamo.save()
        reclamo.denunciantes.add(self.denunciante)
        reclamo.arboles.add(self.arbol)
        self.assertEqual(str(reclamo), "Reclamo #1")

    def test_crear_reclamo(self):
        # Obtener la URL de creación de reclamo
        url = reverse("reclamos:crear_reclamo")

        # Crear un diccionario con los datos del reclamo
        reclamo_data = {
            "numero": 1,
            "medio": "Web",
            "fuente": "1",
            "fecha": timezone.now(),
            "denunciantes": [self.denunciante.id],
            "arboles": [self.arbol.id],
            "reclamo": "Rama caída",
            "urgencia": "1",
        }

        # Enviar una solicitud POST a la URL de creación de reclamo
        response = self.client.post(url, reclamo_data)

        # Verificar que la solicitud haya sido exitosa
        self.assertEqual(response.status_code, 302)

        # Obtener el reclamo creado en la base de datos
        reclamo = Reclamo.objects.get(numero=1)

        # Verificar que los atributos del reclamo sean correctos
        self.assertEqual(reclamo.medio, "Web")
        self.assertEqual(reclamo.fuente, "1")
        self.assertEqual(reclamo.reclamo, "Rama caída")
        self.assertEqual(reclamo.urgencia, "1")

        # Verificar que el reclamo esté asociado con el denunciante y el árbol correctos
        self.assertEqual(list(reclamo.denunciantes.all()), [self.denunciante])
        self.assertEqual(list(reclamo.arboles.all()), [self.arbol])
