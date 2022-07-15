from django.urls import path
from . import views

urlpatterns = [
    path('listagem/', views.home, name='listagem'),
    path('logar/', views.logar, name='logar')
]
