# Generated by Django 5.0.3 on 2024-03-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuprimeiroapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessobancodedados',
            name='idade',
            field=models.IntegerField(blank=True, null=True, verbose_name='Minha idade'),
        ),
    ]
