"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from moteldosguri.views import home, pag_afrodite,pag_eros,pag_intence, cadastro, pag_iris, pag_lumini, pag_luzes, pag_magic, pag_sensacao, pag_vibes, pag_contatos, pag_cardapio, check
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', intro, name='intro'),
    path("", home, name='home'),
    path("home/", home, name='home'),
    path('suite_afrodit/',pag_afrodite, name='afrodite'),
    path('suite_eros/', pag_eros, name = 'eros'),
    path('suite_intence/', pag_intence, name='intence' ),
    path('suite_iris/', pag_iris, name='iris'),
    path('suite_lumini/', pag_lumini, name='lumini'),
    path('suite_luzes/', pag_luzes, name='luzes'),
    path('suite_magic/',pag_magic, name='magic' ),
    path('suite_sensacao/',pag_sensacao, name='sensacao'),
    path('suite_vibes/', pag_vibes, name='vibes'),
    path('cadastro/', cadastro, name='cadastro'),
    path('contatos/', pag_contatos, name='contatos'),
    path('cardapio/', pag_cardapio, name='cardapio'),
    path('check/', check, name='check')
]
