from django.shortcuts import render, get_object_or_404
from.models import Jogo
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):
    jogo= Jogo.objects.filter(publicado=True)
    dados= {
        'jogos': jogo
    }
    return render(request, 'index.html', dados)

def jogo(request, jogo_id):
    jogo= get_object_or_404(Jogo, pk=jogo_id)
    jogo_a_exibir={
        'jogo': jogo
    }
    return render(request, 'jogo.html', jogo_a_exibir)

def buscar(request):
    lista_jogo = Jogo.objects.filter(publicado=True)

    if 'buscar' in request.GET:
        nome_a_buscar= request.GET['buscar']
        if nome_a_buscar:
            lista_jogo= lista_jogo.filter(nome__icontains=nome_a_buscar)

    dados = {
        'jogos': lista_jogo
    }
    return render(request, 'buscar.html', dados)


def criar_jogo(request):
    return render(request, 'jogos/cria_jogo.html')

