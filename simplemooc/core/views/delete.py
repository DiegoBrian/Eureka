from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import *


def excluir_aula(request,pk):
	aula = Aula.objects.get(pk=pk)
	tema = aula.tema_id
	aula.delete()
	return redirect ('tema', tema.pk)


def excluir_exercicio(request,pk):
	exe = Exercicio.objects.get(pk=pk)
	tema = exe.tema_id
	exe.delete()
	return redirect ('tema', tema.pk)


def excluir_experimentacao(request,pk):
	exp = Experimentacao.objects.get(pk=pk)
	tema = exp.tema_id
	exp.delete()
	return redirect ('tema', tema.pk)


def excluir_turma(request,pk):
	turma = Turma.objects.get(pk=pk)
	turma.delete()
	return redirect ('index')


def excluir_tema(request, pk):
	tema = Tema.objects.get(pk=pk)
	turma = tema.turma_id
	tema.delete()
	if turma:
		return redirect ('turma', turma.pk)
	else:
		return redirect ('index')