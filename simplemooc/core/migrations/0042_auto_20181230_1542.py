# Generated by Django 2.0.1 on 2018-12-30 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20181222_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='exercise_id',
        ),
        migrations.RemoveField(
            model_name='aula',
            name='experimentation_id',
        ),
        migrations.RemoveField(
            model_name='exercicio',
            name='experimentation_id',
        ),
        migrations.RemoveField(
            model_name='experimentacao',
            name='exercise_id',
        ),
    ]
