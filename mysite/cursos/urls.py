from django.urls import path
from . import views

urlpatterns = [
    path('listagem/', views.home, name='listagem'),
    path('logar/', views.logar, name='logar'),
    path('inscrever_curso', views.inscrever_curso, name='inscrever_curso'),
    path('inscricoes', views.inscricoes, name='inscricoes')
]
