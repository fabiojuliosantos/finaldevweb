from pickle import TRUE
from django.db import models
from usuarios.models import Usuario



class CursosDisponiveis(models.Model):
    nome_curso = models.CharField(max_length=150)
    professor = models.CharField(max_length=50)
    contato_professor = models.CharField(max_length=30, blank=True, null=True)
    data_curso = models.DateField()
    

    def __str__(self) -> str:
        return str(self.nome_curso)

    class Meta:
        verbose_name = 'Curso'

class CursosInscritos(models.Model):
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo')
    )
    user = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=TRUE)
    curso = models.ForeignKey(CursosDisponiveis, on_delete=models.DO_NOTHING, null=TRUE)
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True)
    comentario = models.TextField(max_length=35, null=TRUE, blank=TRUE )
    def __str__(self) -> str:
        return f"{self.user} | {self.curso} "
    