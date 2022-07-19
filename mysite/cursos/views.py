from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import CursosDisponiveis
from usuarios.models import Usuario
from django.views.decorators.cache import cache_page

# Create your views here.

@cache_page(60)
def home(request):

    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        cursoslistados = CursosDisponiveis.objects.all()

        return render(request, 'cursos.html', {'cursoslistados': cursoslistados, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/cursos/logar')


def logar(request):
    return render(request, 'cursos_logar.html')
