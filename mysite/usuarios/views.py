from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuario.objects.filter(email=email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')
    if len(senha) < 8:
        return redirect('/auth/cadastro/?status = 2')
    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')

    try:
        
        usuario = Usuario(nome=nome, sobrenome=sobrenome,
                          email=email, senha=senha)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')

    return HttpResponse(f"{nome} {sobrenome} {senha} {email} ")


def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    
    usuario = Usuario.objects.filter(email=email).filter(senha=senha)

    usuario = Usuario.objects.filter(email = email).filter(senha = senha)
    
    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        usuarionome = usuario[0].nome
        return redirect('/cursos/listagem')

    return HttpResponse(f"{email} {senha}")

def sair(request):
    request.session.flush()
    return redirect('/auth/login/')