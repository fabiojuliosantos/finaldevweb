from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cursos.api import viewsets as cursosviewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


route = routers.DefaultRouter()

route.register(r'cursos/', cursosviewsets.cursosViewSets, basename="Cursos")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('cursos/', include('cursos.urls')),
    path('auth/', include('usuarios.urls')),
    path('social-auth/', include("social_django.urls"), name='social'),
    path('api/', include(route.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())

]
