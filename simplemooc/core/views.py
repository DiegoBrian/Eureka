from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from core.models import *
from .forms import FormularioRegistro, FormularioEditarConta

# Create your views here.
def home(request):
	return render(request, 'home.html')

def sobre(request):
	return render(request, 'sobre.html')

def testes(request):
	return render(request, 'testes.html')

@login_required
def aula(request, pk):
	aula = get_object_or_404(Aula, pk=pk)
	context = {
		'aula' : aula
	}
	return render(request, 'aula.html', context)

@login_required
def index(request):
	print(request.user.user_type)
	turmas = Turma.objects.filter(responsible= request.user);
	turmas_publicas = Turma.objects.filter(course_type = 'PUBLICA');
	context = {
		'turmas': turmas,
		'turmas_publicas': turmas_publicas
	}
	return render(request, 'index.html', context)


@login_required
def turma(request, pk):
	turma = get_object_or_404(Turma, pk = pk)
	temas = Tema.objects.filter(turma_id = pk)
	context = {
		'turma': turma,
		'temas' : temas
	}
	return render(request, 'turma.html', context)


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
	return render(request,'usuario.html')

@login_required
def editar_usuario(request):
	context = {}
	if request.method == 'POST':
		form = FormularioEditarConta(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Os dados foram alterados com sucesso')
			redirect('editar_usuario')
	else:
		form = FormularioEditarConta(instance = request.user)
	context ['form'] = form

	return render(request,'editar_usuario.html', context)

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

	return render(request,'editar_senha.html', context)


@login_required
def tema(request, pk):
	tema = get_object_or_404(Tema, pk = pk)
	aulas = Aula.objects.filter(tema_id = pk)
	print(aulas)
	exercicios = Exercicio.objects.filter(tema_id = pk)
	experimentacoes = Experimentacao.objects.filter(tema_id = pk)
	context = {
		'tema': tema,
		'aulas': aulas,
		'exercicios':exercicios,
		'experimentacoes':experimentacoes
	}
	return render(request,'tema.html', context)


@login_required
def matricula(request, pk):
	turma = get_object_or_404(Turma, pk = pk)
	matricula, created = Aluno_Turma.objects.get_or_create(aluno_id = request.user, turma_id = turma)
	if created:
		messages.success(request, 'Você foi inscrito nesta turma com sucesso')
	else:
		messages.info(request, 'Você já está inscrito nesta turma')
	return redirect('turma',pk)