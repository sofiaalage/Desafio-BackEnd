from django import forms  
from .models import Loja
class LojaForm(forms.ModelForm): 
    class Meta:
        model = Loja 
        fields = ('nome','cpf','dono_da_loja')

    nome = forms.CharField(label="Coloque seu nome",max_length=50)  
    cpf = forms.CharField(label="Insira o CPF do dono do estabelecimento",max_length=15)  
    dono_da_loja = forms.CharField(label="Insira o nome do dono do estabelecimento", max_length = 50) 

 
