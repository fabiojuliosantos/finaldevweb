from turtle import home
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('inicio/', views.inicial, name="inicio")
]
