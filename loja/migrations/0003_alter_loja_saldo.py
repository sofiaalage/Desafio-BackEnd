# Generated by Django 4.1.4 on 2023-02-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loja", "0002_alter_loja_cpf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loja",
            name="saldo",
            field=models.FloatField(default=0),
        ),
    ]
