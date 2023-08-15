from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre='Laboratorio 1', ciudad='Ciudad 1', pais='Pais 1')

    def test_datos_laboratorio(self):
        laboratorio = Laboratorio.objects.get(nombre='Laboratorio 1')
        self.assertEqual(laboratorio.ciudad, 'Ciudad 1')
        self.assertEqual(laboratorio.pais, 'Pais 1')

class LaboratorioViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre='Laboratorio 1', ciudad='Ciudad 1', pais='Pais 1')

    def test_respuesta_http_200(self):
        url = reverse('listar_laboratorios')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_plantilla_correcta(self):
        url = reverse('listar_laboratorios')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'listar_laboratorios.html')


def test_contenido_html_esperado(self):
    url = reverse('listar_laboratorios')
    response = self.client.get(url)
    print(response.content)
    contenido_esperado = """
        Listado de Laboratorios
    """
    self.assertContains(response, contenido_esperado)