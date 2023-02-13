# Generated by Django 4.1.4 on 2023-02-13 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.IntegerField()),
                ("data", models.TimeField(max_length=8)),
                ("valor", models.FloatField()),
                ("cartao", models.IntegerField()),
                ("hora", models.IntegerField()),
            ],
            options={
                "ordering": ("id",),
            },
        ),
    ]