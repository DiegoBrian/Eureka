# Generated by Django 2.0.1 on 2018-11-02 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20181101_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='correct_answer',
            field=models.CharField(blank=True, choices=[('A', 'a'), ('b', 'b'), ('C', 'c'), ('D', 'd')], default='A', max_length=1, null=True, verbose_name='Resposta correta'),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='student_answer',
            field=models.CharField(blank=True, choices=[('A', 'a'), ('b', 'b'), ('C', 'c'), ('D', 'd')], default='A', max_length=1, null=True, verbose_name='Resposta do aluno'),
        ),
    ]
