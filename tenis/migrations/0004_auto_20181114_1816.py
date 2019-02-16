# Generated by Django 2.0.3 on 2018-11-14 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenis', '0003_remove_jogo_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='correio_eletronico',
            field=models.CharField(default='branco', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jogador',
            name='status_jogador',
            field=models.CharField(default='ATIVO', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jogador',
            name='tel_casa',
            field=models.CharField(default='tel_casa', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jogador',
            name='tel_celular',
            field=models.CharField(default='tel_celular', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jogador',
            name='tel_trabalho',
            field=models.CharField(default='tel_trabalho', max_length=20),
            preserve_default=False,
        ),
    ]
