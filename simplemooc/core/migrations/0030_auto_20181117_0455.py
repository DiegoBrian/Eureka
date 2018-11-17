# Generated by Django 2.0.1 on 2018-11-17 06:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_teste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimentacao',
            name='text_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Conteúdo textual'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='Mensagem'),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Enunciado'),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='reply',
            field=ckeditor.fields.RichTextField(verbose_name='Resposta'),
        ),
        migrations.AlterField(
            model_name='usuario_pergunta',
            name='student_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Resposta'),
        ),
    ]
