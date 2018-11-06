from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from core.models import *
from .forms import *

# Create your views here.
def home(request):
	return render(request, 'home.html')


def sobre(request):
	return render(request, 'sobre.html')


def testes(request):
	return render(request, 'testes.html')


@login_required
def index(request):
	print(request.user.user_type)
	turmas = Turma.objects.filter(responsible= request.user)
	resultado = []
	turmas_publicas = Turma.objects.filter(course_type = 'PUBLICA')
	for turma in turmas_publicas:
		if not esta_matriculado(request.user, turma.pk):
			resultado.append(turma)

	print(resultado)

	context = {
		'turmas': turmas,
		'turmas_publicas': resultado
	}
	return render(request, 'index.html', context)


@login_required
def aula(request, pk):
	aula = get_object_or_404(Aula, pk=pk)

	if not tem_acesso(request.user, aula.tema_id.turma_id.pk):
		messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
		return redirect('index')

	materiais = Material.objects.filter(aula_id = pk)
	context = {
		'aula' : aula,
		'materiais' : materiais
	}
	return render(request, 'content/aula.html', context)

@login_required
def experimentacao(request, pk):
	experimentacao = get_object_or_404(Experimentacao, pk=pk)

	if not tem_acesso(request.user, experimentacao.tema_id.turma_id.pk):
		messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
		return redirect('index')

	context = {
		'experimentacao' : experimentacao
	}
	return render(request, 'content/experimentacao.html', context)


@login_required
def exercicio(request, pk):
	exercicio = get_object_or_404(Exercicio, pk=pk)

	if not tem_acesso(request.user, exercicio.tema_id.turma_id.pk):
		messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
		return redirect('index')

	perguntas = Pergunta.objects.filter(exercise_id = pk)

	context = {
		'exercicio' : exercicio,
		'perguntas' : perguntas
	}
	return render(request, 'content/exercicio.html', context)
	

@login_required
def turma(request, pk):
	turma = get_object_or_404(Turma, pk = pk)

	if not tem_acesso(request.user, turma.pk):
		messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
		return redirect('index')

	temas = Tema.objects.filter(turma_id = pk)
	context = {
		'turma': turma,
		'temas' : temas
	}
	return render(request, 'content/turma.html', context)


@login_required
def tema(request, pk):
	tema = get_object_or_404(Tema, pk = pk)

	if not tem_acesso(request.user, tema.turma_id.pk):
		messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
		return redirect('index')

	aulas = Aula.objects.filter(tema_id = pk)
	exercicios = Exercicio.objects.filter(tema_id = pk)
	experimentacoes = Experimentacao.objects.filter(tema_id = pk)
	context = {
		'tema': tema,
		'aulas': aulas,
		'exercicios':exercicios,
		'experimentacoes':experimentacoes
	}
	return render(request,'content/tema.html', context)


@login_required
def matricula(request, pk):
	turma = get_object_or_404(Turma, pk = pk)
	matricula, created = Aluno_Turma.objects.get_or_create(aluno_id = request.user, turma_id = turma)
	if created:
		messages.success(request, 'Você foi inscrito nesta turma com sucesso')
	else:
		messages.info(request, 'Você já está inscrito nesta turma')
	return redirect('turma',pk)


@login_required
def desfazer_matricula(request, pk):
	turma = get_object_or_404(Turma, pk = pk)
	matricula = get_object_or_404(Aluno_Turma, aluno_id = request.user, turma_id = turma)
	matricula.delete()
	messages.success(request, 'Sua inscrição foi cancelada com sucesso')
	return redirect ('usuario')


def cadastrar(request):
	if request.method == 'POST':
		form = FormularioRegistro(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = FormularioRegistro()
	return render(request, 'registration/cadastrar.html', {'form': form})


@login_required
def usuario(request):
	turmas = Turma.objects.filter(responsible= request.user)
	context = {
		'turmas' : turmas
	}
	return render(request,'user/usuario.html', context)


@login_required
def editar_usuario(request):
	context = {}
	if request.method == 'POST':
		form = FormularioEditarConta(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Os dados foram alterados com sucesso')
			redirect('usuario')
	else:
		form = FormularioEditarConta(instance = request.user)
	context ['form'] = form

	return render(request,'user/editar_usuario.html', context)


@login_required
def editar_senha(request):
	context = {}
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			context['success'] = True
	else:
		form = PasswordChangeForm(user = request.user)
	context ['form'] = form

	return render(request,'user/editar_senha.html', context)


@login_required
def criar_aula(request, tema_id):
	form = FormularioAula(request.POST or None, initial={'tema_id': tema_id})
	if form.is_valid():
		form.save()
		return redirect('tema', pk = tema_id)

	context = {
		'form' : form
	}

	return render (request, "creation/criar_aula.html", context)


@login_required
def criar_experimentacao(request, tema_id):
	form = FormularioExperimentacao(request.POST or None, initial={'tema_id': tema_id})
	if form.is_valid():
		form.save()
		return redirect('tema', pk = tema_id)

	context = {
		'form' : form
	}

	return render (request, "creation/criar_experimentacao.html", context)


@login_required
def criar_exercicio(request, tema_id):
	form = FormularioExercicio(request.POST or None, initial={'tema_id': tema_id})
	if form.is_valid():
		form.save()
		return redirect('tema', pk = tema_id)

	context = {
		'form' : form
	}

	return render (request, "creation/criar_exercicio.html", context)


@login_required
def criar_tema(request, turma_id):
	turma = Turma.objects.filter(pk = turma_id)


	form = FormularioTema(request.POST or None, initial={'turma_id': turma_id})
	if form.is_valid():
		#print(form)
		form.save()
		return redirect('turma', pk = turma_id)

	context = {
		'form' : form
	}

	return render (request, "creation/criar_tema.html", context)


@login_required
def criar_turma(request, profesor_id):
	form = FormularioTurma(request.POST or None, initial={'responsible': profesor_id})
	if form.is_valid():
		form.save()
		return redirect('index')

	context = {
		'form' : form
	}

	return render (request, "creation/criar_turma.html", context)


@login_required
def criar_pergunta(request, exercise_id):
	context = {
		'exercise_id' : exercise_id
	}
	return render(request, 'creation/escolher_tipo_exercicio.html', context)



@login_required
def criar_pergunta_fechada(request, exercise_id):
	form = FormularioPerguntaFechada(request.POST or None, initial={'exercise_id': exercise_id})
	if form.is_valid():
		#print(form)
		form.save()
		return redirect('exercicio', pk = exercise_id)

	context = {
		'form' : form
	}

	return render (request, "creation/criar_pergunta.html", context)


def esta_matriculado(user, turma_pk):
	turma = Turma.objects.get(pk = turma_pk)
	matricula = Aluno_Turma.objects.filter(aluno_id = user, turma_id = turma)

	if matricula:
		return True
	else:
		return False


def eh_responsavel(user, turma_pk):
	turma = Turma.objects.get(pk = turma_pk)

	if turma.responsible == user:
		return True
	else:
		return False


def tem_acesso(user, turma):
	if (user.user_type == 'ALUNO' and esta_matriculado(user, turma)) or (user.user_type == 'PROFESSOR' and eh_responsavel(user, turma)):
		return True
	else:
		return False
