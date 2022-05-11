from django.shortcuts import redirect, render
from core.models import Evento

# Create your views here.
def inicio(request):
    eventos = Evento.objects.all()
    dados = {'eventos':eventos}
    return render(request, "agenda.html", dados)
