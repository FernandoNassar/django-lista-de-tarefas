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


def editar_lista(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            lista = get_object_or_404(Lista, pk=request.POST['lista_id'])
            if lista.usuario.id == request.user.id:
                lista.desc = request.POST['lista_desc']
                if not request.POST['lista_nome'].isspace():
                    lista.nome = request.POST['lista_nome']
                if request.POST['lista_prazo'] != '':
                    lista.prazo = request.POST['lista_prazo']
                else:
                    lista.prazo = None
                if 'lista_imagem' in request.FILES:
                    lista.imagem = request.FILES['lista_imagem']
                lista.save()
                return redirect('lista', request.POST['lista_id'])
            else:
                return redirect('dashboard')
        else:
            return redirect('dashboard')
    else:
        return redirect('login')


def editar_lista_dashboard(request, lista_id):
    if request.user.is_authenticated:
        lista = get_object_or_404(Lista, pk=lista_id)
        if lista.usuario.id == request.user.id: 
            return render(request, 'form_editar_lista.html', {'lista': lista})
        return redirect('dashboard')
    else:
        return redirect('login')


def atualizar_lista_dashboard(request):
    if request.user.is_authenticated:
        lista = get_object_or_404(Lista, pk=request.POST['lista_id'])
        lista.desc = request.POST['lista_desc']
        if not request.POST['lista_nome'].isspace():
            lista.nome = request.POST['lista_nome']
            if request.POST['lista_prazo'] != '':
                lista.prazo = request.POST['lista_prazo']
            else:
                lista.prazo = None
            if 'lista_imagem' in request.FILES:
                lista.imagem = request.FILES['lista_imagem']

            lista.save()
            return redirect('dashboard')
        else:
            return redirect('editar_lista_dashboard', request.POST['lista_id'])
    else:
        return redirect('login')


def cria_tarefa(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            tarefa = Tarefa()
            if request.POST['tarefa_nome'].isspace():
                return redirect('lista', request.POST['lista_id'])
            else:
                tarefa.lista = Lista.objects.get(pk=request.POST['lista_id'])
                tarefa.nome = request.POST['tarefa_nome']
                if 'tarefa_desc' in request.POST:
                    tarefa.desc = request.POST['tarefa_desc']
                if request.POST['tarefa_prazo'] != '':
                    tarefa.prazo = request.POST['tarefa_prazo']
                tarefa.save()
                return redirect('lista', request.POST['lista_id'])
        else:
            return redirect('dashboard')
    else:
        return redirect('login')






# def index(request):
#    if request.user.is_authenticated:
#        pass
#    return redirect('usuario/login')



