# Generated by Django 2.0.1 on 2018-12-22 03:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20181129_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='exercise_id',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='experimentation_id',
        ),
        migrations.AlterField(
            model_name='aula',
            name='visual_content',
            field=models.CharField(max_length=2048, verbose_name='Link para vídeo'),
        ),
        migrations.AlterField(
            model_name='experimentacao',
            name='visual_content',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='Link para vídeo'),
        ),
        migrations.AlterField(
            model_name='usuario_pergunta',
            name='score',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Nota'),
        ),
    ]