from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.db.models import Q
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
	
	turmas = Turma.objects.filter(responsible= request.user)
	resultado = []
	turmas_publicas = Turma.objects.filter(course_type = 'PUBLICA')
	for turma in turmas_publicas:
		if not esta_matriculado(request.user, turma.pk):
			resultado.append(turma)


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
def exercicio(request, exercise_id):
	exercicio = get_object_or_404(Exercicio, pk=exercise_id)

	#se o usuario digita um url de uma turma que não é dono ou não está matriculado, acesso negado
	if not tem_acesso(request.user, exercicio.tema_id.turma_id.pk):
		messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
		return redirect('index')

	exercicio_concluido = Aluno_Exercicio.objects.filter(aluno_id=request.user, exercicio_id=exercise_id)
	if exercicio_concluido:
		if exercicio_concluido[0].exercicio_id.multiple_times == False:
			messages.error(request, 'Você já concluiu este exercício!')
			return redirect('tema', pk = exercicio.tema_id.pk)
		else:
			Usuario_Pergunta.objects.filter(aluno_id=request.user, question_id__exercise_id=exercicio).delete()
			Aluno_Exercicio.objects.filter(aluno_id=request.user, exercicio_id=exercicio).delete()



	#verifica se o usuario ja respondeu alguma pergunta deste exercicio
	respondidos = Usuario_Pergunta.objects.filter(aluno_id=request.user, question_id__exercise_id=exercicio)
	#se ele ainda não respondeu nenhuma pergunta
	if not respondidos:
		#busca a primeira pergunta do exercicio
		pergunta = Pergunta.objects.filter(exercise_id=exercise_id, number=1)
		#coloca a primeira pergunta pra ser respondida apenas se existir alguma pergunta
		if pergunta:
			Usuario_Pergunta.objects.create(aluno_id=request.user, 
											question_id=pergunta[0],
											answered=False)

	#ve todas as perguntas que o usuario ja respondeu/esta respondendo
	respondidos = Usuario_Pergunta.objects.filter(aluno_id=request.user, question_id__exercise_id=exercicio, answered=False)

	#se tem pergunta no exercicio
	if respondidos:
		#pega a pergunta que está pra ser respondida
		pergunta = Pergunta.objects.get(exercise_id = exercise_id, number=respondidos[0].question_id.number)
		todas_perguntas = Pergunta.objects.filter(exercise_id= exercise_id)
	#se exercicio nao tem pergunta nenhuma, não manda nada
	else:
		pergunta = None
		todas_perguntas = None

	context = {
		'exercicio' : exercicio,
		'pergunta' : pergunta,
		'perguntas' : todas_perguntas
	}
	return render(request, 'content/exercicio.html', context)

@login_required
def proxima_pergunta(request, exercise_id, number):
	exercicio = get_object_or_404(Exercicio, pk=exercise_id)
	# ve qual foi a resposta do aluno
	# vai na tabela usuario_pergunta
	pergunta = Pergunta.objects.get(exercise_id=exercicio, number = number)
	# se multipla escolha
	# 	resposta_fechada = resposta
	# se aberta
	# 	resposta_aberta = resposta
	# respondido = true
	Usuario_Pergunta.objects.filter(aluno_id = request.user, question_id= pergunta).update(answered=True)
	# vai na tabela exercicio_pergunta e ve se existe pergunta com numero = pergunta.numero+1
	proxima_pergunta = Pergunta.objects.filter(exercise_id=exercise_id, number=number+1)
	# se existe
	if proxima_pergunta:
	# 	cria elemento na tabela usuario_pergunta com o numero pergunta.numero+1, respondido = false
		Usuario_Pergunta.objects.create(aluno_id=request.user, question_id=proxima_pergunta[0], answered = False)
		return redirect('exercicio', exercise_id=exercise_id)
	# senao
	else:
	# 	finalizar exercicio
		Aluno_Exercicio.objects.create(aluno_id=request.user, exercicio_id=exercicio)
		return redirect('tema', pk = exercicio.tema_id.pk)

	
	

@login_required
def turma(request, pk):
	turma = get_object_or_404(Turma, pk = pk)

	if not tem_acesso(request.user, turma.pk):
		messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
		return redirect('index')

	if request.method == 'POST':
		srch = request.POST['search']
		temas = Tema.objects.filter(Q(turma_id = pk) | Q(name__incontains=srch))
	else:
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


def cadastrar(request, user_type):
	if request.method == 'POST':
		if user_type == 0:
			form = FormularioRegistroAluno(request.POST)
		else:
			form = FormularioRegistroProfessor(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		if user_type == 0:
			form = FormularioRegistroAluno()
		else:
			form = FormularioRegistroProfessor()
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
		exercise = form.save()
		return redirect('criar_pergunta', exercise_id = exercise.pk)

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
	perguntas = Pergunta.objects.filter(exercise_id=exercise_id).order_by('-number')
	if perguntas:
		number = perguntas[0].number+1
	else:
		number = 1

	form = FormularioPergunta(request.POST or None, initial={'exercise_id': exercise_id, 'number' : number})
	if form.is_valid():
		#print(form)
		form.save()
		return redirect('exercicio', exercise_id = exercise_id)

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
