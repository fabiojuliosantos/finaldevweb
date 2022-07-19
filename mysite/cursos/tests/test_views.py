from django.test import TestCase
from django.urls import reverse

class CursosViewTeste(TestCase):

    def test_status_code_302_listagem(self):
        response = self.client.get(reverse('listagem'))
        self.assertEquals(response.status_code, 302)

    def test_status_code_200_login(self):
        response = self.client.get(reverse('logar'))
        self.assertEquals(response.status_code, 200)