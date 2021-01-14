from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Lista(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    prazo = models.DateField(blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='imagens/%d/%m/%Y', blank=True, null=True)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)
    prazo = models.DateField(blank=True, null=True)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    

    



