from listas.models import Lista, Tarefa
#from django.contrib.auth.models import User

def validacao_editar_tarefa(request, tarefa):
    if request.POST['tarefa_nome'].isspace():
        raise ValueError('Nome Vazio')
    else:
        tarefa.nome = request.POST['tarefa_nome']

    if request.POST['tarefa_prazo'] != '':
        tarefa.prazo = request.POST['tarefa_prazo']
    else:
        tarefa.prazo = None
    
    tarefa.desc = request.POST['tarefa_desc']
    
    return tarefa


def validacao_criar_lista(request, lista):
    if request.POST['nome_lista'].isspace():
        raise ValueError('Nome Vazio')
    else:
        lista.nome = request.POST['nome_lista']
    
    if request.POST['prazo_lista'] != '':
        lista.prazo = request.POST['prazo_lista']
    
    if 'desc_lista' in request.POST:
        lista.desc = request.POST['desc_lista']

    if 'imagem_lista' in request.FILES:
        lista.imagem = request.FILES['imagem_lista']
    
    return lista


def validacao_atualizar_lista(request, lista):
    lista.desc = request.POST['lista_desc']
    
    if request.POST['lista_nome'].isspace():
        raise ValueError('Nome Vazio')
    else: 
        lista.nome = request.POST['lista_nome']
    
    if request.POST['lista_prazo'] != '':
        lista.prazo = request.POST['lista_prazo']
    else:
        lista.prazo = None
        
    if 'lista_imagem' in request.FILES:
        lista.imagem = request.FILES['lista_imagem']

    return lista


def validacao_criar_tarefa(request, tarefa):
    if request.POST['tarefa_nome'].isspace():
        raise ValueError('Nome Vazio')
    else:
        tarefa.lista = Lista.objects.get(pk=request.POST['lista_id'])
        tarefa.nome = request.POST['tarefa_nome']
        
        if 'tarefa_desc' in request.POST:
            tarefa.desc = request.POST['tarefa_desc']
        
        if request.POST['tarefa_prazo'] != '':
            tarefa.prazo = request.POST['tarefa_prazo']
        
        return tarefa 
