# Generated by Django 2.0.1 on 2018-11-15 02:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20181115_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='text_content',
            field=ckeditor.fields.RichTextField(verbose_name='Conteúdo textual'),
        ),
    ]
