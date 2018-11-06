# Generated by Django 2.0.1 on 2018-11-02 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20181102_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='correct_answer',
            field=models.CharField(choices=[('A', 'a'), ('b', 'b'), ('C', 'c'), ('D', 'd')], default='A', max_length=1, verbose_name='Resposta correta'),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='student_answer',
            field=models.CharField(choices=[('A', 'a'), ('b', 'b'), ('C', 'c'), ('D', 'd')], default='A', max_length=1, verbose_name='Resposta do aluno'),
        ),
    ]
