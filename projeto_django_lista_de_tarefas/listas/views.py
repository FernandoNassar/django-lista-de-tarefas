from django.shortcuts import render, redirect, get_object_or_404
from .models import Lista, Tarefa
from django.contrib.auth.models import User
from .funcs.funcs import validacao_editar_tarefa, validacao_criar_lista, validacao_atualizar_lista, validacao_criar_tarefa
from django.core.paginator import Paginator

def criar_lista(request):
    if request.user.is_authenticated:
        lista = Lista()
        lista.usuario = User.objects.get(pk=request.user.id)

        try:
            lista = validacao_criar_lista(request, lista)
        
        except ValueError:
            return redirect('dashboard')
        
        else:
            lista.save()
            return redirect('dashboard')

    return redirect('/login')


def exibir_lista(request, lista_id):
    if request.user.is_authenticated:
        lista = Lista.objects.get(pk=lista_id)
        tarefas = Tarefa.objects.order_by('-data_criacao').filter(lista=lista_id)
        dados = {'lista': lista, 'tarefas': tarefas}
        
        return render(request, 'lista.html', dados)
    return redirect('/login')


def excluir_lista(request, lista_id):
    if request.user.is_authenticated:
        lista = get_object_or_404(Lista, pk=lista_id)
        
        if lista.usuario.id == request.user.id:
            lista.delete()

        return redirect('dashboard')
    return redirect('login')


def editar_lista(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            lista = get_object_or_404(Lista, pk=request.POST['lista_id'])
            
            if lista.usuario.id == request.user.id:
                try:
                    lista = validacao_atualizar_lista(request, lista)
                except ValueError:
                    return redirect('lista', request.POST['lista_id'])
                else:
                    lista.save()
                    return redirect('lista', request.POST['lista_id'])
                
        return redirect('dashboard')
    return redirect('login')


def editar_lista_dashboard(request, lista_id):
    if request.user.is_authenticated:
        lista = get_object_or_404(Lista, pk=lista_id)

        if lista.usuario.id == request.user.id: 
            return render(request, 'form_editar_lista.html', {'lista': lista})
        
        return redirect('dashboard')
    return redirect('login')


def atualizar_lista_dashboard(request):
    if request.user.is_authenticated:
        lista = get_object_or_404(Lista, pk=request.POST['lista_id'])

        if lista.usuario.id == request.user.id:
            try: 
                lista = validacao_atualizar_lista(request, lista)
            except ValueError:
                return redirect('editar_lista_dashboard', request.POST['lista_id'])
            else:
                lista.save()
                
        return redirect('dashboard')  
    return redirect('login')


def criar_tarefa(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            tarefa = Tarefa()
            try:
                tarefa = validacao_criar_tarefa(request, tarefa)
            except ValueError:
                return redirect('lista', request.POST['lista_id'])
            else:
                tarefa.save()
                return redirect('lista', request.POST['lista_id'])
        
        return redirect('dashboard')
    return redirect('login')


def excluir_tarefa(request, tarefa_id):
    if request.user.is_authenticated:
        tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
        
        if tarefa.lista.usuario.id == request.user.id:
            tarefa.delete()
        
        return redirect('lista', tarefa.lista.id)
    return redirect('login')


def finalizar_tarefa(request, tarefa_id):
    if request.user.is_authenticated:
        tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
        lista_id = tarefa.lista.id 
        
        if tarefa.lista.usuario.id == request.user.id:
            tarefa.finalizado = True
            tarefa.save()
            return redirect('lista', lista_id)
        
        return redirect('lista', lista_id)
    return redirect('login')


def buscar_lista(request):
    if request.user.is_authenticated:
        if 'buscar' in request.GET:
            listas = Lista.objects.order_by('-prazo').filter(usuario=User.objects.get(pk=request.user.id))
            listas = listas.filter(nome__icontains=request.GET['buscar'])
            dados = {'listas': listas}
            
            return render(request, 'buscar_lista.html', dados)
        
        return redirect('dashboard')
    return redirect('login')


def form_editar_tarefa(request, tarefa_id):
    if request.user.is_authenticated:
        tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
        
        if tarefa.lista.usuario.id == request.user.id:
            return render(request, 'form_editar_tarefa.html', {'tarefa': tarefa})
        
        return redirect('dashboard')
    return redirect('login')



def atualizar_tarefa(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            tarefa = get_object_or_404(Tarefa, pk=request.POST['tarefa_id'])
            try:
                tarefa = validacao_editar_tarefa(request, tarefa)

            except ValueError:
                return redirect('lista', tarefa.lista.id)
            
            else:
                tarefa.save()
                return redirect('lista', tarefa.lista.id)

        return redirect('dashboard')
    return redirect('login')

