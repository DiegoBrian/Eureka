from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.conf import settings
from courses.models import *
from .forms import RegisterForm

# Create your views here.
def home(request):
	return render(request, 'home.html')

def sobre(request):
	return render(request, 'sobre.html')

def testes(request):
	return render(request, 'testes.html')


def aula(request, pk):
	aula = get_object_or_404(Aula, pk=pk)
	context = {
		'aula' : aula
	}
	return render(request, 'aula.html', context)


def index(request):
	turmas_privadas = Turma.objects.filter(course_type = 'PRIVADA');
	turmas_publicas = Turma.objects.filter(course_type = 'PUBLICA');
	context = {
		'turmas_privadas': turmas_privadas,
		'turmas_publicas': turmas_publicas
	}
	return render(request, 'index.html', context)

def turma(request, pk):
	turma = get_object_or_404(Turma, pk = pk)
	aulas = Aula.objects.filter(turma_id = pk)
	exercicios = Exercicio.objects.filter(turma_id = pk)
	experimentacoes = Experimentacao.objects.filter(turma_id = pk)
	context = {
		'turma': turma,
		'aulas' : aulas,
		'exercicios' : exercicios,
		'experimentacoes' : experimentacoes
	}
	return render(request, 'turma.html', context)


def cadastrar(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(settings.LOGIN_URL)
		else:
			form = RegisterForm()
	context = {
		'form': RegisterForm()
	}
	return render(request, 'registration/cadastrar.html', context)

def cadastrar(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/cadastrar.html', {'form': form})