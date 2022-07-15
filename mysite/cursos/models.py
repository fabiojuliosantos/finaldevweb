from django.db import models
from usuarios.models import Usuario


class CursosDisponiveis(models.Model):
    nome_curso = models.CharField(max_length=150)
    professor = models.CharField(max_length=50)
    contato_professor = models.CharField(max_length=30, blank=True, null=True)
    data_curso = models.DateTimeField()
    

    def __str__(self) -> str:
        return str(self.nome_curso)

    class Meta:
        verbose_name = 'Curso'
