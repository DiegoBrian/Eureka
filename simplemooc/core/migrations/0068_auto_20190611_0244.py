# Generated by Django 2.0.1 on 2019-06-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_auto_20190606_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Tema'),
        ),
        migrations.AlterField(
            model_name='aula',
            name='text_content',
            field=models.TextField(verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='aula',
            name='visual_content',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='Vídeo em destaque'),
        ),
    ]
