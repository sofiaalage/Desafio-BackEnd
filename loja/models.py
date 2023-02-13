from django.db import models
import uuid

class Loja(models.Model):
    class Meta:
        app_label  = 'loja'
        ordering = ("id",)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    nome = models.CharField(max_length=19)
    saldo = models.FloatField(default=0)
    cpf = models.CharField(max_length=15)
    dono_da_loja=models.CharField(max_length=19)