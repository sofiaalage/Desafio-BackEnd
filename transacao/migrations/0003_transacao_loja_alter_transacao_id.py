# Generated by Django 4.1.4 on 2023-02-13 02:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("loja", "0004_remove_loja_transacoes_alter_loja_id"),
        ("transacao", "0002_alter_transacao_cartao_alter_transacao_data_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="transacao",
            name="loja",
            field=models.ForeignKey(
                default="", on_delete=django.db.models.deletion.CASCADE, to="loja.loja"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="transacao",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
