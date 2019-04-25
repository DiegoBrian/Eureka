# Generated by Django 2.0.1 on 2019-04-24 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_auto_20190421_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercicio',
            name='turma_id',
        ),
        migrations.RemoveField(
            model_name='experimentacao',
            name='turma_id',
        ),
        migrations.AddField(
            model_name='experimentacao',
            name='exp_type',
            field=models.CharField(choices=[('CIÊNCIA', 'Ciência'), ('JOGO', 'Jogo'), ('NOTICIA', 'Notícia'), ('MÚSICA', 'Música'), ('VÍDEO', 'Vídeo')], default='CIENCIA', max_length=9, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='experimentacao',
            name='name',
            field=models.CharField(blank=True, default='Experimentacao', max_length=100, null=True, verbose_name='Título'),
        ),
    ]
