# Generated by Django 2.0.1 on 2018-10-07 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20181007_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicio',
            name='multiple_times',
            field=models.BooleanField(default=False, verbose_name='Refazível'),
        ),
    ]
