# Generated by Django 2.0.1 on 2019-03-14 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20190314_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='document',
        ),
        migrations.AddField(
            model_name='document',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
