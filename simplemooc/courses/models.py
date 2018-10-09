from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Course(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	description = models.TextField('Descrição', blank=True)
	start_date = models.DateField('Data de Início', null=True, blank = True)
	image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		ordering = ['name']
		

class Usuario(models.Model):
	USER_OPTIONS = (
		('PROFESSOR', 'Professor'),
		('ALUNO', 'Aluno'),
	)

	name = models.CharField('Nome', max_length=100)
	#password = models.
	birth_date = models.DateField('Data de Nascimento', null=True, blank = True)
	grade = models.IntegerField('Série', validators=[MaxValueValidator(9), MinValueValidator(1)], null=True, blank = True)
	email = models.EmailField('Email', max_length=256, blank=True)
	user_type = models.CharField('Tipo', max_length=9, choices=USER_OPTIONS, default='ALUNO')

	def __str__(self):
		return self.name

class Turma(models.Model):
	COURSE_OPTIONS = (
		('PÚBLICA', 'Pública'),
		('PRIVADA', 'Privada'),
	)
	name = models.CharField('Nome', max_length=100)
	course_type = models.CharField('Tipo', max_length=9, choices=COURSE_OPTIONS, default='PUBLICO')
	responsible = models.ForeignKey('Usuario', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Aula(models.Model):
	turma_id = models.ForeignKey('Turma', on_delete=models.CASCADE, default=1)
	topic = models.CharField('Tema', max_length=100)
	text_content = models.TextField('Conteúdo textual')
	visual_content = models.CharField('Conteúdo visual', max_length=2048)

	def __str__(self):
		return self.topic


class Exercicio(models.Model):
	turma_id = models.ForeignKey('Turma', on_delete=models.CASCADE, default=1)
	topic = models.CharField('Tema', max_length=100)
	multiple_times = models.BooleanField('Refazível', default=False)

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
	turma_id = models.ForeignKey('Turma', on_delete=models.CASCADE, default=1)
	aluno_id = models.ForeignKey('Usuario', on_delete=models.CASCADE, default=1)


class Aluno_Exercicio(models.Model):
	exercicio_id = models.ForeignKey('Exercicio', on_delete=models.CASCADE, default=1)
	aluno_id = models.ForeignKey('Usuario', on_delete=models.CASCADE, default=1)

