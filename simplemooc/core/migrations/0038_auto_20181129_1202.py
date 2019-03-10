# Generated by Django 2.0.1 on 2018-11-29 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20181127_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno_exercicio',
            name='corrected',
            field=models.BooleanField(default=False, verbose_name='Corrigigo'),
        ),
        migrations.AddField(
            model_name='aluno_exercicio',
            name='score',
            field=models.FloatField(blank=True, null=True, verbose_name='Nota final'),
        ),
    ]
