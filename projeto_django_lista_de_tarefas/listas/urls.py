from django.urls import path
from . import views
from django.contrib.auth.models import User 

urlpatterns = [
    path('nova_lista', views.criar_lista, name='nova_lista'),
    path('lista/<int:lista_id>', views.exibir_lista, name='lista'),
    path('remover_lista/<int:lista_id>', views.excluir_lista, name='remover_lista'),
    path('editar_lista', views.editar_lista, name='editar_lista'),
    path('editar_lista_dashboard/<int:lista_id>', views.editar_lista_dashboard, name='editar_lista_dashboard'),
    path('atualizar_lista', views.atualizar_lista_dashboard, name='atualizar_lista'),
    path('nova_tarefa', views.criar_tarefa, name='nova_tarefa'),
    path('remover_tarefa/<int:tarefa_id>', views.excluir_tarefa, name='remover_tarefa'),
    path('finalizar_tarefa/<int:tarefa_id>', views.finalizar_tarefa, name='finalizar_tarefa'),
    path('buscar_lista', views.buscar_lista, name='buscar_lista'),
    path('editar_tarefa/<int:tarefa_id>', views.form_editar_tarefa, name='editar_tarefa'),
    path('atualizar_tarefa', views.atualizar_tarefa, name='atualizar_tarefa'),

    #path('', views.index, name='index'),
    #path('cadastrar', views.cadastrar, name='cadastrar'),
    #path('login', views.login, name='login'),
    #path('dashboard', views.dashboard, name='dashboard'),
]