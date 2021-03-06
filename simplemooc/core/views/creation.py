from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.forms import *
from core.models import *

@login_required
def criar_forum(request, pk):

	#controle de acesso

	form = FormularioForum(request.POST or None, initial={'author' : request.user})
	if form.is_valid():
		newforum = form.save(commit = False)
		turma = Turma.objects.get(pk=pk)
		newforum.turma_id = turma
		
		newforum.save()
		return redirect('forum', pk = pk)

	context = {
		'form' : form
	}

	return render (request, "creation/criar_forum.html", context)


@login_required
def criar_aula(request, turma_id):

	#controle de acesso
	# if not (request.user.user_type == 'PROFESSOR' and eh_responsavel(request.user, tema_id)):
	# 	messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
	# 	return redirect('index')
	
	form = FormularioAula(request.POST or None, initial={'turma_id': turma_id})
	if form.is_valid():
		new_class = form.save()
		return redirect('turma', pk = turma_id)

	context = {
		'form' : form,
		'turma' : turma_id
	}

	return render (request, "creation/criar_aula.html", context)


@login_required
def criar_experimentacao(request, class_id):

	#controle de acesso
	# if not (request.user.user_type == 'PROFESSOR' and eh_responsavel(request.user, tema_id)):
	# 	messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
	# 	return redirect('index')
	
	form = FormularioExperimentacao(request.POST or None, initial={'class_id': class_id})
	if form.is_valid():
		new_experimentation = form.save()
		return redirect('experimentacoes', pk = class_id)

	context = {
		'form' : form,
		'aula': class_id
	}

	return render (request, "creation/criar_experimentacao.html", context)


@login_required
def criar_exercicio(request, class_id):

	#controle de acesso
	# if not (request.user.user_type == 'PROFESSOR' and eh_responsavel(request.user, tema_id)):
	# 	messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
	# 	return redirect('index')

	form = FormularioExercicio(request.POST or None, initial={'class_id': class_id})
	if form.is_valid():
		new_exercise = form.save()
		return redirect('criar_pergunta', exercise_id = new_exercise.pk)

	context = {
		'form' : form,
		'aula': class_id
	}

	return render (request, "creation/criar_exercicio.html", context)


@login_required
def criar_turma(request, profesor_id):

	#controle de acesso
	# if not (request.user.user_type == 'PROFESSOR'):
	# 	messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
	# 	return redirect('index')

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

	exercicio = Exercicio.objects.get(pk = exercise_id)

	#controle de acesso
	# if not (request.user.user_type == 'PROFESSOR' and eh_responsavel(request.user, exercicio.class_id.tema_id.pk)):
	# 	messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
	# 	return redirect('index')

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

