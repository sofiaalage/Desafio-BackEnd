# Generated by Django 4.1.4 on 2023-02-13 02:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("loja", "0003_alter_loja_saldo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="loja",
            name="transacoes",
        ),
        migrations.AlterField(
            model_name="loja",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
