# Generated by Django 2.0.1 on 2019-04-24 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_auto_20190424_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimentacao',
            name='name',
            field=models.CharField(default='Experimentacao', max_length=100, verbose_name='Título'),
        ),
    ]
