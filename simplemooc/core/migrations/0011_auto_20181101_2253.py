# Generated by Django 2.0.1 on 2018-11-02 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20181101_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='correct_answer',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Resposta correta'),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='student_answer',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Resposta do aluno'),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='student_text',
            field=models.TextField(blank=True, null=True, verbose_name='Resposta do aluno'),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='text',
            field=models.TextField(verbose_name='Enunciado'),
        ),
    ]
