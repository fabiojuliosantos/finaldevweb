from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=45)
    email = models.EmailField(max_length=30)
    senha = models.CharField(max_length=64, null=False)

    def __str__(self) -> str:
        return self.nome 