from django import forms  
class TrasacaoForm(forms.Form):  
    tipo = forms.CharField(label="Insira o tipo da transação",max_length=50)  
    data = forms.IntegerField(label="Insira a data da transação")  
    hora = forms.IntegerField(label="Insira a hora da transação")  
    valor = forms.FloatField(label="Insira o valor da transação")  
    cartao = forms.IntegerField(label="Insira a hora da transação")  
    loja = forms.CharField(label="Insira o nome da loja ", max_length = 10)  
