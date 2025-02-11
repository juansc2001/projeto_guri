from django.shortcuts import render, redirect
from .models import Clientes, Contato
from .forms import ClientesForm

def home(request):
    bulle = 0
    return render(request,'home.html', {'boleano': bulle })


def intro(request):
    return render(request, 'intro.html')

def pag_afrodite(request):
    if request == True:
        bulle = 0
    else:
        bulle = 1
    return render(request, 'suite_afrodit.html', {'boleano': bulle })

def pag_eros(request):
    if request == True:
        bulle = 0
    else:
        bulle = 1
    return render(request, 'suite_eros.html', {'boleano': bulle })

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


def cadastroC(request):
    client_list = Clientes.objects.all()
    return render(request, "reserva.html", {'cliente': client_list})

def cadastro(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        formulario = ClientesForm()
        return render(request, 'cadastro.html', {'form': formulario})

    
# Create your views here.
