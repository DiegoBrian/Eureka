# Generated by Django 2.0.1 on 2018-11-15 01:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20181111_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='text_content',
            field=ckeditor.fields.RichTextField(verbose_name='Conteúdo textual'),
        ),
    ]
