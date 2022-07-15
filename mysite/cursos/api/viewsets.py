from rest_framework import viewsets
from cursos.api import serializers
from rest_framework.permissions import IsAuthenticated
from cursos import models

class cursosViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    serializer_class = serializers.cursosSerializers
    queryset = models.CursosDisponiveis.objects.all()