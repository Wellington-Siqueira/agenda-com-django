from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/login/')
def inicio(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':eventos}
    return render(request, "agenda.html", dados)

def login_usuario(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username, password=password)
        if usuario:
            login(request, usuario)
            return redirect('/')
        
        else:
            messages.error(request, "Usuario ou senha invalidos")
    
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['eventos'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        local = request.POST.get('local')
        id_evento = request.POST.get('id_evento')
        usuario = request.user

        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.local = local
                evento.save()

            #Evento.objects.filter(id=id_evento).update(titulo=titulo, descricao=descricao, data_evento=data_evento, local=local)
        else:
            Evento.objects.create(titulo=titulo, descricao=descricao, data_evento=data_evento, usuario=usuario, local=local)

    return redirect('/')


def cadastro(request):
    return render(request, 'cadastro.html')

def cadastro_submit(request):
    if request.POST:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        conf_senha = request.POST.get('conf_senha')

        if senha != conf_senha or len(senha.strip()) == 0 or len(usuario.strip()) == 0:
            messages.error(request, "Senhas diferentes ou campos vazios")
            return redirect('/cadastro')
        
        else:
            User.objects.create_user(username=usuario, password=senha)
    return redirect('/')

@login_required(login_url='/login/')
def deletar_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)

    if usuario == evento.usuario:
        evento.delete()

    return redirect('/')