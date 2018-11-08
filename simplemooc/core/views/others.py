from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.models import *


# Create your views here.
def home(request):
	return render(request, 'home.html')


def sobre(request):
	return render(request, 'sobre.html')


def testes(request):
	return render(request, 'testes.html')


@login_required
def index(request):
	
	if request.method == 'POST':
		srch = request.POST['search']
		turmas = Turma.objects.filter(responsible= request.user, name__icontains=srch)
		matriculas = Aluno_Turma.objects.filter(aluno_id=request.user, turma_id__name__icontains=srch)
		resultado = []
		turmas_publicas = Turma.objects.filter(course_type = 'PUBLICA', name__icontains=srch)
		for turma in turmas_publicas:
			if not esta_matriculado(request.user, turma.pk):
				resultado.append(turma)
	else:
		turmas = Turma.objects.filter(responsible= request.user)
		matriculas = Aluno_Turma.objects.filter(aluno_id=request.user)
		resultado = []
		turmas_publicas = Turma.objects.filter(course_type = 'PUBLICA')
		for turma in turmas_publicas:
			if not esta_matriculado(request.user, turma.pk):
				resultado.append(turma)


	context = {
		'turmas': turmas,
		'turmas_publicas': resultado,
		'matriculas' : matriculas
	}
	return render(request, 'index.html', context)

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