from django.db import models

class Loja(models.Model):
    class Meta:
        ordering = ("id",)
    nome = models.CharField(max_length=19)
    saldo = models.IntegerField(max_length=233)
    cpf = models.IntegerField(max_length=11)
    dono_da_loja=models.IntegerChoices() 
    transacao = models.ForeignKey(
        "transacoess.Transacao", on_delete=models.CASCADE, related_name="transacoes"
    )