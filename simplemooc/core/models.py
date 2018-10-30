from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth import get_user_model
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
	is_active = models.BooleanField('Esta ativo?', blank=True, default=True)
	is_staff = models.BooleanField('Admin', blank=True, default=False)
	date_joined = models.DateTimeField('Data de cadastro', auto_now_add=True)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email','name','gender','birth_date','user_type']

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'

class Turma(models.Model):
	COURSE_OPTIONS = (
		('PUBLICA', 'Pública'),
		('PRIVADA', 'Privada'),
	)
	name = models.CharField('Nome', max_length=100)
	course_type = models.CharField('Tipo', max_length=9, choices=COURSE_OPTIONS, default='PUBLICA')
	responsible = models.ForeignKey('Usuario', on_delete=models.CASCADE)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name

class Tema(models.Model):
	name = models.CharField('Nome', max_length=100)
	turma_id = models.ForeignKey('Turma', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Aula(models.Model):
	name = models.CharField('Nome', max_length=100, default='Aula X')
	tema_id = models.ForeignKey('Tema', on_delete=models.CASCADE, default=1)
	text_content = models.TextField('Conteúdo textual')
	visual_content = models.CharField('Conteúdo visual', max_length=2048)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name


class Exercicio(models.Model):
	name = models.CharField('Nome', max_length=100, default='Exercicio')
	tema_id = models.ForeignKey('Tema', on_delete=models.CASCADE, default=1)
	multiple_times = models.BooleanField('Refazível', default=False)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.topic

class Experimentacao(models.Model):
	name = models.CharField('Nome', max_length=100, default='Experimentacao')
	tema_id = models.ForeignKey('Tema', on_delete=models.CASCADE, default=1)
	text_content = models.TextField('Conteúdo textual')
	visual_content = models.CharField('Conteúdo visual', max_length=2048)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.topic

class Pergunta(models.Model):
	QUESTION_OPTIONS = (
		('FECHADA', 'Múltipla Escolha'),
		('ABERTA', 'Resposta aberta'),
	)
	exercise_id = models.ForeignKey('Exercicio', on_delete=models.CASCADE)
	text = models.TextField('Texto')
	quesion_type = models.CharField('Tipo', max_length=9, choices=QUESTION_OPTIONS, default='FECHADA')
	student_answer = models.CharField('Resposta fechada do aluno', max_length=1, null=True, blank = True)
	answer_a = models.CharField('a)', max_length=2048, null=True, blank = True)
	answer_b = models.CharField('b)', max_length=2048, null=True, blank = True)
	answer_c = models.CharField('c)', max_length=2048, null=True, blank = True)
	answer_d = models.CharField('d)', max_length=2048, null=True, blank = True)
	correct_answer = models.CharField('Resposta fechada correta', max_length=1, null=True, blank = True)
	student_text = models.TextField('Resposta aberta do aluno', null=True, blank = True)

	def __str__(self):
		return self.id

class Aluno_Turma(models.Model):
	turma_id = models.ForeignKey('Turma', related_name = 'matriculas', on_delete=models.CASCADE)
	aluno_id = models.ForeignKey(get_user_model(), verbose_name = 'Usuário', related_name = 'matriculas', on_delete=models.CASCADE, null = True)

	class Meta:
		verbose_name = 'Inscrição'
		verbose_name_plural = 'Inscrições'
		unique_together = (('aluno_id','turma_id'),)

class Aluno_Exercicio(models.Model):
	exercicio_id = models.ForeignKey('Exercicio', on_delete=models.CASCADE, default=1)
	aluno_id = models.ForeignKey('Usuario', on_delete=models.CASCADE, default=1)