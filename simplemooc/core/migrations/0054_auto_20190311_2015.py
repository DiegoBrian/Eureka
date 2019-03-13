# Generated by Django 2.0.1 on 2019-03-11 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_tema_turma'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='answer_e',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='e)'),
        ),
        migrations.AlterField(
            model_name='aula',
            name='visual_content',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='Link para vídeo'),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='correct_answer',
            field=models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e')], default='A', max_length=1, verbose_name='Resposta correta'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='core/images', verbose_name='Foto'),
        ),
    ]
