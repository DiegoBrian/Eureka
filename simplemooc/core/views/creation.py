from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.forms import *
from core.models import *

@login_required
def criar_forum(request, content, pk):

	form = FormularioForum(request.POST or None, initial={'author' : request.user})
	if form.is_valid():
		newforum = form.save(commit = False)
		if content == 'cla':
			aula = Aula.objects.get(pk=pk)
			newforum.class_id = aula
		elif content == 'exe':
			exercicio = Exercicio.objects.get(pk=pk)
			newforum.exercise_id = exercicio
		elif content == 'exp':
			experimentacao = Experimentacao.objects.get(pk=pk)
			newforum.experimentation_id = experimentacao
		newforum.save()
		return redirect('forum', content = content, pk = pk)

	context = {
		'form' : form
	}

	return render (request, "creation/criar_forum.html", context)


@login_required
def criar_aula(request, tema_id):
	form = FormularioAula(request.POST or None, initial={'tema_id': tema_id})
	if form.is_valid():
		new_class = form.save(commit = False)
		content = request.POST.get('content')
		new_class.text_content = content
		new_class.save()
		return redirect('tema', pk = tema_id)

	context = {
		'form' : form
	}

	return render (request, "creation/criar_aula.html", context)


@login_required
def criar_experimentacao(request, tema_id):
	form = FormularioExperimentacao(request.POST or None, initial={'tema_id': tema_id})
	if form.is_valid():
		new_experimentation = form.save()
		return redirect('tema', pk = tema_id)

	context = {
		'form' : form
	}

	return render (request, "creation/criar_experimentacao.html", context)


@login_required
def criar_exercicio(request, tema_id):
	form = FormularioExercicio(request.POST or None, initial={'tema_id': tema_id})
	if form.is_valid():
		new_exercise = form.save()
		return redirect('criar_pergunta', exercise_id = new_exercise.pk)

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

	

