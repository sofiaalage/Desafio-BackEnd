from django import forms  
from .models import Transacao
class TrasacaoForm(forms.ModelForm): 
    class Meta: 
        model = Transacao
        fields = ('tipo','data','hora','valor','cartao')
    

    tipo = forms.CharField(label="Insira o tipo da transação",max_length=11)  
    data = forms.CharField(label="Insira a data da transação")  
    hora = forms.CharField(label="Insira a hora da transação",max_length=9)  
    valor = forms.FloatField(label="Insira o valor da transação")  
    cartao = forms.CharField(label="Insira a hora da transação",max_length=20)
