from django.db import models


class Clientes(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    horario = models.DateTimeField()
    mensagem = models.CharField(max_length=100, null=False, blank=False)
    

    #Adicione esta fução para exibir o nome dos alunos dentro do painel administrativo#
    #Veremos isso mais a frente
    def __str__(self):
        return self.nome
    
class Contato(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
# Create your models here.
