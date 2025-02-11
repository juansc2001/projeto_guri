from django import forms
from .models import Clientes

class ClientesForm(forms.ModelForm):
    class Meta:
        #informa o modelo
        model = Clientes

        #Informa os campos
        fields = ['nome', 'data', 'horario', 'mensagem',]

        #Define como as labes apareceram no formulário
        labels ={
            'nome': 'Informe seu nome:',
            'data': 'informe o dia',
            'horario': 'Informe o horario desejado',
            'mensagem': 'Algum pedido especial? UwU',
            
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),            
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Algum pedido especial? UwU', 'id':'exampleFormControlTextarea1'}),
            'data': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'horario': forms.TimeInput(attrs={'type':'time', 'class':'form-control '}),
            

        }