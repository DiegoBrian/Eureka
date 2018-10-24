from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
import re

class Usuario(AbstractBaseUser, PermissionsMixin):
	USER_OPTIONS = (
		('PROFESSOR', 'Professor'),
		('ALUNO', 'Aluno'),
	)
	GENDER_OPTIONS = (
		('MASCULINO', 'M'),
		('FEMININO', 'F'),
	)

	username = models.CharField('Nome de Usuário', max_length=30, unique=True, validators = [validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'O nome de usuário só pode conter letras, dígitos ou os seguintes caracteres @/./+/-/_', 'invalid')])
	name = models.CharField('Nome', max_length=100)
	#password = models.
	gender = user_type = models.CharField('Sexo', max_length=9, choices=GENDER_OPTIONS, default='MASCULINO')
	birth_date = models.DateField('Data de Nascimento', null=True, blank = True)
	grade = models.IntegerField('Série', validators=[MaxValueValidator(9), MinValueValidator(1)], null=True, blank = True)
	email = models.EmailField('Email', max_length=256, blank=True, unique=True)
	user_type = models.CharField('Tipo', max_length=9, choices=USER_OPTIONS, default='ALUNO')
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)
	is_active = models.BooleanField('Estpa ativo?', blank=True, default=True)
	is_staff = models.BooleanField('Admin', blank=True, default=False)
	date_joined = models.DateTimeField('Data de cadastro', auto_now_add=True)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'