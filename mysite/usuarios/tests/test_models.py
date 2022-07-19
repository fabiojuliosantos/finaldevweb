from django.test import TestCase
from ..models import Usuario


class UsuarioTeste(TestCase):

    def setUp(self):
        Usuario.objects.create(
            nome="Fabio Julio",
            sobrenome="dos Santos",
            email="fjss@discente.ifpe.edu.br",
            senha="fabiojulio26"
        )

    def test_retorno_str(self):
        usuario1 = Usuario.objects.get(nome="Fabio Julio")
        self.assertEquals(usuario1.__str__(), "Fabio Julio")
    
    def test_nome_deveria_ter_sido_informado(self):
        usuarioNome = Usuario.objects.get(nome="Fabio Julio")
        self.assertNotEquals(usuarioNome, None)

    def test_sobrenome_deveria_ter_sido_informado(self):
        usuarioSobreNome = Usuario.objects.get(sobrenome="dos Santos")
        self.assertNotEquals(usuarioSobreNome, None)
    
    def test_email_deveria_ter_sido_informado(self):
        usuarioEmail = Usuario.objects.get(email="fjss@discente.ifpe.edu.br")
        self.assertNotEquals(usuarioEmail, None)
    
    def test_senha_deveria_ter_sido_informada(self):
        usuarioSenha = Usuario.objects.get(senha="fabiojulio26")
        self.assertNotEquals(usuarioSenha, None)
        

    
