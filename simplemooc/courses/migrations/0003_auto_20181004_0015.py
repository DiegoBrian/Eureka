# Generated by Django 2.0.1 on 2018-10-04 03:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20181003_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('birth_date', models.DateField(verbose_name='Data de Nascimento')),
                ('grade', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(1)], verbose_name='Série')),
                ('email', models.EmailField(blank=True, max_length=256, verbose_name='Email')),
                ('user_type', models.CharField(choices=[('PROFESSOR', 'professor'), ('ALUNO', 'aluno')], default='ALUNO', max_length=9, verbose_name='Tipo')),
            ],
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
    ]
