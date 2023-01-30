from django.db import models

class Transacao(models.Model):
    class Meta:
        ordering = ("id",)
    tipo = models.IntegerField(max_length=1)
    data = models.TimeField(max_length=8)
    valor = models.IntegerField(max_length=10)
    cartao = models.IntegerField(max_length=12)
    hora = models.IntegerField(max_length=6)
    loja = models.IntegerField(max_length=11)