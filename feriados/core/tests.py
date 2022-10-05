from django.test import TestCase 
from core.models import FeriadoModel
from datetime import datetime


class SemFeriadoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Lamento')
        self.assertContains(self.resp, 'hoje não tem feriado.')

    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')


class PossuiFeriadoTest(TestCase):
    def setUp(self):
        hoje = datetime.today()
        feriado = FeriadoModel(nome='Dia do Saci', dia=hoje.day, mes=hoje.month)
        feriado.save()
        self.resp = self.client.get('/')

    def test_dados_no_banco_fake(self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Dia do Saci')

    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')



class FeriadoModelTest(TestCase):
    def setUp(self):
        self.feriado = 'Natal'
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadoModel(
            nome=self.feriado,
            dia=self.dia,
            mes=self.mes,
        )
        self.cadastro.save()
    
    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)

    def test_nome_feriado(self):
        nome = self.cadastro.__dict__.get('nome', '')
        self.assertEqual(nome, self.feriado)