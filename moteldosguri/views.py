from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def pag_afrodite(request):
    return render(request, 'suite_afrodit.html')

# Create your views here.
