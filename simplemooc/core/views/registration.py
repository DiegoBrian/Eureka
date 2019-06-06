from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.forms import *
from core.models import *

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
	return redirect ('usuario', request.user.pk)


def cadastrar(request, user_type):
	if request.method == 'POST':
		if user_type == 0:
			form = FormularioRegistroAluno(request.POST, request.FILES)
		else:
			form = FormularioRegistroProfessor(request.POST, request.FILES)
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


