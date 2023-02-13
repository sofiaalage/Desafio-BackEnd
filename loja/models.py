from django.db import models
import uuid

class Loja(models.Model):
    class Meta:
        app_label  = 'loja'
        ordering = ("id",)
    nome = models.CharField(max_length=19)
    saldo = models.FloatField()
    cpf = models.IntegerField()
    dono_da_loja=models.CharField(max_length=19)
    transacoes = models.ForeignKey("transacao.Transacao", on_delete=models.CASCADE)