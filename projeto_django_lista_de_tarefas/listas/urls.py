from django.urls import path
from . import views
from django.contrib.auth.models import User 

urlpatterns = [
    path('nova_lista', views.cria_lista, name='nova_lista'),
    path('lista/<int:lista_id>', views.exibe_lista, name='lista'),
    #path('', views.index, name='index'),
    #path('cadastrar', views.cadastrar, name='cadastrar'),
    #path('login', views.login, name='login'),
    #path('dashboard', views.dashboard, name='dashboard'),
]