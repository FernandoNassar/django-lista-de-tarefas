from django.shortcuts import render, redirect
from usuarios.forms.forms import UserFormCadastro, UserFormLogin
from django.contrib.auth.models import User
from django.contrib import auth
from listas.models import Lista

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')

def cadastrar(request):
    if request.method == 'POST':
        form = UserFormCadastro(request.POST)
        if form.is_valid():
            nome = request.POST['username']
            email = request.POST['email']
            senha = request.POST['password']

            usuario = User.objects.create_user(username=nome, email=email, password=senha)
            usuario.save()
            user = auth.authenticate(request, username=nome, password=senha)
            auth.login(request, user)
            return redirect('dashboard')
        else:
            contexto = {'form': form}
            return render(request, 'form_cadastro.html', contexto)


    contexto = {'form': UserFormCadastro()}
    return render(request, 'form_cadastro.html', contexto)


def login(request):
    if request.method == 'POST':
        form = UserFormLogin(request.POST)
        if form.is_valid():
            email = request.POST['email']
            senha = request.POST['password']

            if User.objects.filter(email=email).exists():
                nome = User.objects.filter(email=email).values_list('username', flat=True).get()
                senha = request.POST['password']
                user = auth.authenticate(request, username=nome, password=senha)

                if user is not None:
                    auth.login(request, user)
                    return redirect('dashboard')
        else:
            contexto = {'form': form}
            return render(request, 'form_login.html', contexto)


    contexto = {'form': UserFormLogin()}
    return render(request, 'form_login.html', contexto)


def logout(request):
    auth.logout(request)
    return redirect('login')


def dashboard(request):
    if request.user.is_authenticated:
        usuario_id = request.user.id 
        listas = Lista.objects.order_by('-data_criacao').filter(usuario=usuario_id)
        dados = {'listas': listas}
        return render(request, 'dashboard.html', dados)
    else:
        return redirect('login')


