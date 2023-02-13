from django.db import models

class Transacao(models.Model):
    class Meta:
        app_label  = 'transacao'
        ordering = ("id",)
    tipo = models.IntegerField()
    data = models.TimeField(max_length=8)
    hora = models.TimeField(max_length=5)
    valor = models.FloatField()
    cartao = models.IntegerField()
    hora = models.IntegerField()