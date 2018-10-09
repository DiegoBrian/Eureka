# Generated by Django 2.0.1 on 2018-10-07 04:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20181007_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='answer_a',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='a)'),
        ),
        migrations.AddField(
            model_name='pergunta',
            name='answer_b',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='b)'),
        ),
        migrations.AddField(
            model_name='pergunta',
            name='answer_c',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='c)'),
        ),
        migrations.AddField(
            model_name='pergunta',
            name='answer_d',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='d)'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='grade',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(1)], verbose_name='Série'),
        ),
    ]
