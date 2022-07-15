from rest_framework import serializers
from cursos import models

class cursosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CursosDisponiveis
        id = serializers.IntegerField(read_only=True)
        fields = '__all__'