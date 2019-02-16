#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Jogador
# Create your views here.

def index(request):
    texto = "Página principal do novo site da barragem"
    context = {
        'meu_texto': texto
    }
    return render(request, 'tenis/index.html', context)

def tabela(request):
    texto = "Página da tabela do novo site barragem"
    context = {
        'meu_texto': texto
    }
    return render(request, 'tenis/tabela.html', context)

def tenista(request):
    texto = "Página da lista de tenistas"
    jogadores = Jogador.objects.all()
    context = {
        'meu_texto': texto,
        'jogadores': jogadores,
    }
    return render(request, 'tenis/tenista.html', context)
