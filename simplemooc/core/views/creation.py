from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.forms import *
from core.models import *

@login_required
def criar_forum(request, pk):

	form = FormularioForum(request.POST or None, initial={'author' : request.user})
	if form.is_valid():
		newforum = form.save(commit = False)
		tema = Tema.objects.get(pk=pk)
		newforum.tema_id = tema
		
		newforum.save()
		return redirect('forum', pk = pk)

	context = {
		'form' : form
	}

	return render (request, "creation/criar_forum.html", context)


@login_required
def criar_aula(request, tema_id):
	
	form = FormularioAula(request.POST or None, initial={'tema_id': tema_id})
	if form.is_valid():
		new_class = form.save()
		return redirect('tema', pk = tema_id)

	context = {
		'form' : form
	}

	return render (request, "creation/criar_aula.html", context)


@login_required
def criar_experimentacao(request, tema_id, class_id):
	
	form = FormularioExperimentacao(request.POST or None, initial={'tema_id': tema_id, 'class_id': class_id})
	if form.is_valid():
		new_experimentation = form.save()
		return redirect('tema', pk = tema_id)

	context = {
		'form' : form
	}

	return render (request, "creation/criar_experimentacao.html", context)


@login_required
def criar_exercicio(request, tema_id, class_id):

	form = FormularioExercicio(request.POST or None, initial={'tema_id': tema_id, 'class_id': class_id})
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


	form = FormularioTema(request.POST or None, initial={'turma_id': turma_id, 'responsible': request.user})

	if form.is_valid():
		#print(form)
		novo_tema = form.save()
		if turma:
			Tema_Turma.objects.create(turma_id = turma[0], tema_id=novo_tema)
		return redirect('tema', pk = novo_tema.pk)

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

	
@login_required
def vincular (request, turma_id, tema_id):
	turma = Turma.objects.get(pk = turma_id)
	tema = Tema.objects.get(pk = tema_id)

	Tema_Turma.objects.create(turma_id = turma, tema_id=tema)

	return redirect ('turma', pk = turma.pk)