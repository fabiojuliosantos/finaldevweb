from curses.ascii import HT
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import CursosDisponiveis, CursosInscritos
from usuarios.models import Usuario
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(60)
def home(request):

    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        cursoslistados = CursosDisponiveis.objects.all()

        usuarios = Usuario.objects.all()
        print(usuarios)

        return render(request, 'cursos.html', {'cursoslistados': cursoslistados, 
                                               'usuario_logado': request.session.get('usuario'),
                                               'usuarios': usuarios})

    else:
        return redirect('/cursos/logar')
    
    


def logar(request):
    return render(request, 'cursos_logar.html')

def mostrar_inscricoes(request):
    usuario = Usuario.objects.get(id = request.session['usuario'])
    inscricoes = CursosInscritos.objects.filter(user = usuario)
    print(inscricoes)

def inscrever_curso(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        curso = request.POST.get('curso')
        avaliacao = request.POST.get('opcoes')
        comentario = request.POST.get('comentario')
        cursosinscritos = CursosInscritos(user_id = user, 
                                          curso_id = curso,
                                          avaliacao = avaliacao,
                                          comentario = comentario)
    cursosinscritos.save()

    return redirect('listagem/')

def inscricoes(request):
    usuario = Usuario.objects.get(id = request.session['usuario'])
    cursos_inscritos = CursosInscritos.objects.filter(user = usuario)
    print(cursos_inscritos)

    return render(request, 'mostra_cursos.html', {'usuario_logado': request.session['usuario'], 
                                                'cursos_inscritos':cursos_inscritos})