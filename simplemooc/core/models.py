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
	gender = user_type = models.CharField('Sexo', max_length=9, choices=GENDER_OPTIONS, default='MASCULINO')
	birth_date = models.DateField('Data de Nascimento', null=True, blank = True)
	grade = models.IntegerField('Série', validators=[MaxValueValidator(9), MinValueValidator(1)], null=True, blank = True)
	email = models.EmailField('Email', max_length=256, blank=True, unique=True)
	image = models.FileField(null = True, blank = True)
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
	responsible = models.ForeignKey('Usuario', verbose_name='Responsável', on_delete=models.CASCADE)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name


class Aula(models.Model):
	name = models.CharField('Nome', max_length=100, default='Aula X')
	turma_id = models.ForeignKey('Turma', on_delete=models.CASCADE, blank=True, null=True)
	text_content = models.TextField('Conteúdo textual')
	summary = models.TextField('Resumo', default="")
	visual_content = models.CharField('Link para vídeo', max_length=2048, blank=True, null=True)
	file = models.FileField('Arquivo',null = True, blank = True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name

class Material(models.Model):
	name = models.CharField('Nome', max_length=100)
	file = models.FileField(upload_to='core/materials', blank=True, null=True)

	aula_id = models.ForeignKey('Aula', verbose_name='Aula', on_delete=models.CASCADE, default=1, related_name='materials')

	def __str__(self):
		return self.name

class Exercicio(models.Model):
	name = models.CharField('Nome', max_length=100, default='Exercicio')
	multiple_times = models.BooleanField('Pode ser feito mais de uma vez', default=False)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)
	class_id = models.ForeignKey('Aula', verbose_name='Aula', on_delete=models.CASCADE, blank=True, null=True)
	

	def __str__(self):
		return self.name

class Experimentacao(models.Model):
	name = models.CharField('Título', max_length=100, default='Experimentacao')
	text_content = models.TextField('Conteúdo textual',null=True, blank = True)
	visual_content = models.CharField('Link para vídeo', max_length=2048, null=True, blank = True)
	source = models.CharField('Fonte', max_length=2048, default='http://')
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)
	class_id = models.ForeignKey('Aula', verbose_name='Aula', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.name

class Pergunta(models.Model):
	QUESTION_OPTIONS = (
		('FECHADA', 'Múltipla Escolha'),
		('ABERTA', 'Resposta aberta'),
	)
	CORRECT_ANSWER = (
		('a', 'a'),
		('b', 'b'),
		('c', 'c'),
		('d', 'd'),
		('e', 'e'),
	)
	exercise_id = models.ForeignKey('Exercicio', verbose_name='Exercício', on_delete=models.CASCADE)
	number = models.IntegerField('Número', default=1)
	text = models.TextField('Enunciado')
	quesion_type = models.CharField('Tipo', max_length=9, choices=QUESTION_OPTIONS, default='FECHADA')
	answer_a = models.CharField('a)', max_length=2048, null=True, blank = True)
	answer_b = models.CharField('b)', max_length=2048, null=True, blank = True)
	answer_c = models.CharField('c)', max_length=2048, null=True, blank = True)
	answer_d = models.CharField('d)', max_length=2048, null=True, blank = True)
	answer_e = models.CharField('e)', max_length=2048, null=True, blank = True)
	correct_answer = models.CharField('Resposta correta', max_length=1, choices=CORRECT_ANSWER, default='A')

	def __str__(self):
		return self.text

class Usuario_Pergunta(models.Model):
	CORRECTION_OPTIONS = (
		('C', 'Certo'),
		('E', 'Errado'),
		('N', 'Não corrigido'),
	)
	aluno_id = models.ForeignKey(get_user_model(), verbose_name = 'Usuário', on_delete=models.CASCADE, null = True)
	question_id = models.ForeignKey('Pergunta', verbose_name = 'Pergunta', related_name = 'respostas', on_delete=models.CASCADE, null = True)
	student_answer = models.CharField('Resposta', max_length=1, default='a')
	student_text = models.TextField('Resposta', null=True, blank = True)
	answered = models.BooleanField('Respondido', default= False)
	correction = models.CharField('Correção', max_length=9, choices=CORRECTION_OPTIONS, default='N')
	score = models.FloatField('Nota', validators=[MaxValueValidator(10), MinValueValidator(1)], null=True, blank = True)
	comment = models.TextField('Comentário', null=True, blank = True)


	def __str__(self):
		if self.answered:
			return '('+self.correction+')'+self.aluno_id.name+" respondeu a pergunta "+self.question_id.text
		else:
			return '('+self.correction+')'+self.aluno_id.name+" está respondendo a pergunta "+self.question_id.text

class Aluno_Turma(models.Model):
	turma_id = models.ForeignKey('Turma', related_name = 'matriculas', on_delete=models.CASCADE)
	aluno_id = models.ForeignKey(get_user_model(), verbose_name = 'Usuário', related_name = 'matriculas', on_delete=models.CASCADE, null = True)

	class Meta:
		verbose_name = 'Inscrição'
		verbose_name_plural = 'Inscrições'
		unique_together = (('aluno_id','turma_id'),)

class Aluno_Exercicio(models.Model):
	exercicio_id = models.ForeignKey('Exercicio', verbose_name='Exercício', on_delete=models.CASCADE, default=1)
	aluno_id = models.ForeignKey('Usuario', on_delete=models.CASCADE, default=1)
	corrects = models.IntegerField('Certos', default=0)
	wrongs = models.IntegerField('Errados', default=0)
	score = models.FloatField('Nota final', blank=True, null=True)
	score_2 = models.FloatField('Nota da prática', blank=True, null=True)

	def __str__(self):
		return self.aluno_id.name+" concluiu o exercício "+self.exercicio_id.name

class Forum (models.Model):
	name = models.CharField('Título', max_length=100)
	author = models.ForeignKey(get_user_model(), verbose_name = 'Autor', related_name='threads', on_delete=models.CASCADE)
	body =  models.TextField('Mensagem')
	views = models.IntegerField('Vizualizações', blank=True, default=0)
	answers = models.IntegerField('Respostas', blank=True, default=0)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)
	turma_id = models.ForeignKey('Turma', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.name

class Resposta (models.Model):
	forum_id = models.ForeignKey('Forum', verbose_name="Tópico", related_name='replies', on_delete=models.CASCADE, default=0)
	reply = models.TextField('Resposta')
	author = models.ForeignKey(get_user_model(), verbose_name = 'Autor', on_delete=models.CASCADE)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.reply[:100]

class Teste (models.Model):

	text = models.TextField("Texto")

class Aluno_Aula(models.Model):
	aula_id = models.ForeignKey('Aula', verbose_name='Aula', on_delete=models.CASCADE, default=1)
	aluno_id = models.ForeignKey('Usuario', on_delete=models.CASCADE, default=1)
	
	def __str__(self):
		return self.aluno_id.name+" concluiu a aula "+self.aula_id.name

class Aluno_Experimentacao(models.Model):
	experimentacao_id = models.ForeignKey('Experimentacao', verbose_name='Experimentacao', on_delete=models.CASCADE, default=1)
	aluno_id = models.ForeignKey('Usuario', on_delete=models.CASCADE, default=1)
	
	def __str__(self):
		return self.aluno_id.name+" concluiu a experimentacao "+self.experimentacao_id.name


class Document(models.Model):
	description = models.CharField('Nome', max_length=255, blank=True)
	image = models.FileField('Arquivo', null = True, blank = True)
	uploaded_at = models.DateTimeField(auto_now_add=True)

	aula_id = models.ForeignKey('Aula', verbose_name='Aula', on_delete=models.CASCADE)

	def __str__(self):
		return self.description