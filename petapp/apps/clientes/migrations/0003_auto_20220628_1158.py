# Generated by Django 3.2.5 on 2022-06-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20220626_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='descricao',
        ),
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Cpf'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.TextField(default=1, max_length=100, verbose_name='Endereco'),
            preserve_default=False,
        ),
    ]
