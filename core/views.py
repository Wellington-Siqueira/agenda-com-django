from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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