# Generated by Django 4.1.4 on 2023-02-13 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loja", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loja",
            name="cpf",
            field=models.CharField(max_length=15),
        ),
    ]
