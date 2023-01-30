from django.db import models

class Loja(models.Model):
    class Meta:
        ordering = ("id",)
    nome = models.CharField(max_length=19)
    saldo = models.IntegerField(max_length=233) 