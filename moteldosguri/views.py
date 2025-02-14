from django.shortcuts import render, redirect
from .models import Clientes
from .forms import ClientesForm

def home(request):
    bulle = 0
    return render(request,'home.html', {'boleano': bulle })

def pag_contatos(request):
    return render(request, 'contatos.html')

def pag_cardapio(request):
    if request == True:
        bulle = 0
    else:
        bulle = 1
    
    buttton = 'mudar'


    return render(request, 'cardapio.html', {'boleano': bulle, 'botao':buttton })


def pag_afrodite(request):
    if request == True:
        bulle = 0
    else:
        bulle = 1
    
    
    return render(request, 'suite_afrodit.html', {'boleano': bulle})

def pag_eros(request):
    if request == True:
        bulle = 0
    else:
        bulle = 1

    return render(request, 'suite_eros.html', {'boleano': bulle})

def pag_intence(request):
    if request == True:
        bulle = 0
    else:
        bulle = 1
    return render(request, 'suite_intence.html', {'boleano':bulle })

def pag_iris(request):
    if request == True:
        bulle = 0
    else:
        bulle = 1
    return render(request, 'suite_iris.html', {'boleano':bulle })

def pag_lumini(request):
    if request == True:
        bulle = 0
    else:
        bulle = 1
    return render(request, 'suite_lumini.html', {'boleano':bulle })

def pag_luzes(request):
    if request == True:
        bulle = 0
    else:
        bulle = 1
    return render(request, 'suite_luzes.html', {'boleano':bulle})

def pag_magic(request):
    if request == True:
        bulle = 0
    else:
        bulle = 1
    return render(request, 'suite_magic.html', {'boleano':bulle })

def pag_sensacao(request):
    if request == True:
        bulle = 0
    else:
        bulle = 1
    return render(request, 'suite_sensacao.html', {'boleano':bulle })

def pag_vibes(request):
    if request == True:
        bulle = 0
    else:
        bulle = 1
    return render(request, 'suite_vibes.html', {'boleano':bulle })


def check(request):
    client_list = Clientes.objects.all()
    return render(request, "check.html", {'cliente': client_list})

def cadastro(request):

    if request == True:
        bulle = 0
    else:
        bulle = 1
    
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            horario = form.cleaned_data['horario']
            if Clientes.objects.filter(data=data, horario=horario).exists():
                form.add_error(None, "Este horário já está reservado.")
            else:
                form.save()
                return redirect('home')
    else:
        form = ClientesForm()
    
    return render(request, 'cadastro.html', {'form': form, 'boleano':bulle})


# Create your views here.
