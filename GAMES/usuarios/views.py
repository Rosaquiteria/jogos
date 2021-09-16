from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']
        if not nome.strip():
            print('o campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('o campo email não pode ficar em branco')
            return redirect('cadastro')
        if not senha1.strip():
            print('o campo senha não pode ficar em branco')
            return redirect('cadastro')
        if senha1 != senha2:
            print('senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuario já cadastrado')
            return redirect('cadastro')
        usuario = User.objects.create_user(username=nome, email=email, password=senha1)
        usuario.save()
        print('usuario cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print('os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email= email).exists():
            nome = User.objects.filter(email= email).values_list('username', flat=True).get()
            usuario = auth.authenticate(request, username=nome, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                print('login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')