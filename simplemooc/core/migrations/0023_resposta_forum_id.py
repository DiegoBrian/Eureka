# Generated by Django 2.0.1 on 2018-11-08 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20181108_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='resposta',
            name='forum_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Forum', verbose_name='Tópico'),
        ),
    ]