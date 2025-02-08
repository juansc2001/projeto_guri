from django.shortcuts import render, redirect
from .models import Clientes, Contato
from .forms import ClientesForm

def home(request):
    return render(request,'home.html')

def pag_afrodite(request):
    return render(request, 'suite_afrodit.html')

def cadastroC(request):
    client_list = Clientes.objects.all()
    return render(request, "cadastro.html", {'cliente': client_list})

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
