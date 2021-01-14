from django.contrib.auth.models import User

def campo_vazio(campo, nome_campo, lista_de_erros):
    '''Verifica se o campo está vazio'''
    if campo == '':
        lista_de_erros[nome_campo] = f'O campo {nome_campo} deve ser preenchido'

def senhas_diferentes(senha1, senha2, lista_de_erros):
    if senha1 != senha2:
        lista_de_erros['password'] = 'As senhas são diferentes'

def email_existente(email, lista_de_erros):
    if User.objects.filter(email=email).exists():
        lista_de_erros['email'] = 'Email já cadastrado'

def email_nao_cadastrado(email, lista_de_erros):
    if not User.objects.filter(email=email).exists():
        lista_de_erros['email'] = 'O endereço de email não esta cadastrado'

