from django.test import TestCase
from ..models import CursosDisponiveis


class CursoTeste(TestCase):
    
    def setUp(self):
        CursosDisponiveis.objects.create(
            nome_curso="Python para iniciantes",
            professor="Abner Dias",
            contato_professor="abnerdias@protonmail.ch",
            data_curso="2022-07-22"
        )
    
    def test_retorno_str(self):
        curso1 = CursosDisponiveis.objects.get(nome_curso="Python para iniciantes")
        self.assertEquals(curso1.__str__(), "Python para iniciantes")

    def test_professor_deve_ser_informado(self):
        cursoProfessor = CursosDisponiveis.objects.get(professor="Abner Dias")
        self.assertNotEquals(cursoProfessor, None)
    
    def test_contato_professor_deve_ser_informado(self):
        contatoProfessor = CursosDisponiveis.objects.get(contato_professor="abnerdias@protonmail.ch")
        self.assertNotEquals(contatoProfessor, None)
    
    def test_data_deve_ser_informada(self):
        cursoData = CursosDisponiveis.objects.get(data_curso="2022-07-22")
        self.assertNotEquals(cursoData, None)