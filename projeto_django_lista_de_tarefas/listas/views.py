from django.shortcuts import render, redirect, get_object_or_404
from .models import Lista, Tarefa
from django.contrib.auth.models import User


def cria_lista(request):
    if request.user.is_authenticated:
        lista = Lista()
        lista.usuario = User.objects.get(pk=request.user.id)
        if request.POST['nome_lista'].isspace():
            return redirect('dashboard')
        else:
            lista.nome = request.POST['nome_lista']
        if request.POST['prazo_lista'] != '':
            lista.prazo = request.POST['prazo_lista']
        if 'desc_lista' in request.POST:
            lista.desc = request.POST['desc_lista']
        if 'imagem_lista' in request.FILES:
            lista.imagem = request.FILES['imagem_lista']
        lista.save()
        return redirect('dashboard')
    else:
        return redirect('/login')


def exibe_lista(request, lista_id):
    if request.user.is_authenticated:
        lista = Lista.objects.get(pk=lista_id)
        tarefas = Tarefa.objects.order_by('-data_criacao').filter(lista=lista_id)
        dados = {'lista': lista, 'tarefas': tarefas}
        return render(request, 'lista.html', dados)
    else:
        return redirect('/login')


def exclui_lista(request, lista_id):
    if request.user.is_authenticated:
        lista = get_object_or_404(Lista, pk=lista_id)
        if lista.usuario.id == request.user.id:
            lista.delete()
        return redirect('dashboard')
    else:
        return redirect('login')

#def index(request):
#    if request.user.is_authenticated:
#        pass
#    return redirect('usuario/login')



