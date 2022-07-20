from django.contrib import admin
from .models import CursosDisponiveis
from .models import CursosInscritos

admin.site.register(CursosDisponiveis)
admin.site.register(CursosInscritos)

