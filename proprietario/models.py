from django.db import models

class Proprietario(models.Model):
    class Meta:
        ordering = ("id",)
    nome = models.CharField(max_length=14)
    cpf = models.IntegerField(max_length=11)
    dono_da_loja=models.IntegerChoices()