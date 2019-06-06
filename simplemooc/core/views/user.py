from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import *
from core.forms import *

@login_required
def usuario(request, usuario_id):
	usuario = Usuario.objects.get(pk=usuario_id)
	turmas = Turma.objects.filter(responsible= usuario)
	aluno_exercicios = Aluno_Exercicio.objects.filter(aluno_id=usuario)
	#print(aluno_exercicios)
	context = {
		'turmas' : turmas,
		'aluno_exercicios' : aluno_exercicios,
		'usuario' : usuario
	}
	return render(request,'user/usuario.html', context)


@login_required
def editar_usuario(request):
	context = {}
	if request.method == 'POST':
		form = FormularioEditarConta(request.POST, request.FILES, instance = request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Os dados foram alterados com sucesso')
			redirect('usuario',1)
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

