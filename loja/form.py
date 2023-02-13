from django import forms  
class LojaForm(forms.Form):  
    nome = forms.CharField(label="Coloque seu nome",max_length=50)  
    saldo  = forms.FloatField(label="Insira o saldo")  
    cpf = forms.IntegerField(label="Insira o CPF do dono do estabelecimento",)  
    dono_da_loja = forms.CharField(label="Insira o nome do dono do estabelecimento", max_length = 50) 

 
