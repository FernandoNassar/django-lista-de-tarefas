from django import forms
from django.contrib.auth.models import User
from .validation import *

class UserFormCadastro(forms.ModelForm):
    password2 = forms.CharField(label="Confirmação de senha", max_length=32, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {'username': 'nome', 'email': 'Email', 'password': 'Senha'}
        widgets = {'password': forms.PasswordInput(), 'email': forms.EmailInput()}

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        lista_de_erros = {}
        
        campo_vazio(username, 'username', lista_de_erros)
        campo_vazio(email, 'email', lista_de_erros)
        campo_vazio(password, 'senha', lista_de_erros)
        campo_vazio(password2, 'senha', lista_de_erros)
        senhas_diferentes(password, password2, lista_de_erros)
        email_existente(email, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data


class UserFormLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        labels = {'email': 'Email', 'password': 'Senha'}
        widgets = {'password': forms.PasswordInput(), 'email': forms.EmailInput()}
   
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        lista_de_erros = {}

        campo_vazio(email, 'email', lista_de_erros)
        campo_vazio(password, 'senha', lista_de_erros)
        email_nao_cadastrado(email, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        
        return self.cleaned_data

        

