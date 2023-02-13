from django.db import models
import uuid
class Transacao(models.Model):
    class Meta:
        app_label  = 'transacao'
        ordering = ("id",)

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    tipo = models.CharField(max_length=15)
    data = models.CharField(max_length=15)
    hora = models.CharField(max_length=15)
    valor = models.FloatField()
    cartao = models.CharField(max_length=20)
    loja = models.ForeignKey("loja.Loja", blank=True, null=True, on_delete=models.CASCADE)