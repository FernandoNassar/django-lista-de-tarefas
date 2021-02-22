from listas.models import Lista, Tarefa

def finaliza_lista(listas):
    
    for lista in listas:
        lista.finalizado = True
        tarefas = Tarefa.objects.order_by('-data_criacao').filter(lista=lista)
         
        for tarefa in tarefas:
            if not tarefa.finalizado:
                lista.finalizado = False
                lista.save() 
                break
        lista.save()

    return listas 