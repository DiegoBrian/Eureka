# Generated by Django 2.0.1 on 2019-03-14 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
