from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.models import *
from core.forms import *


# Create your views here.
def home(request):
	return render(request, 'home.html')


def sobre(request):
	return render(request, 'sobre.html')


def testes(request):
	form = FormularioTeste(request.POST or None)
	if form.is_valid():
		new_test = form.save()
		return redirect('testes')

	context = {
		'form' : form,
	}

	print("form: ")
	print(form)
	return render(request, 'testes.html', context)


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