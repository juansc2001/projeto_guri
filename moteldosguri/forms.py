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
            'nome': forms.TextInput(attrs={'class': 'form-control','style':'margin-bottom: 25px;', 'placeholder': 'Digite seu nome'}),            
            'mensagem': forms.Textarea(attrs={'class': 'form-control ','style':'margin-bottom: 25px;', 'rows': 5, 'placeholder': 'Algum pedido especial? UwU', 'id':'exampleFormControlTextarea1'}),
            'data': forms.DateInput(attrs={'type':'date', 'style':'margin-bottom: 25px; ', 'class':'form-control'}),
            'horario': forms.TimeInput(attrs={'type':'time', 'class':'form-control ', 'style':'margin-bottom: 25px; @import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");'}),
            

        }