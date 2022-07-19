from django.test import TestCase
from django.urls import reverse


class UsuarioViewTeste(TestCase):

    def test_status_code_200_login(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    def test_status_code_200_cadastro(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEquals(response.status_code, 200)

    