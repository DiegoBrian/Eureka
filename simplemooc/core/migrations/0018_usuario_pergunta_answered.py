# Generated by Django 2.0.1 on 2018-11-07 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20181106_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario_pergunta',
            name='answered',
            field=models.BooleanField(default=False, verbose_name='Respondido'),
        ),
    ]