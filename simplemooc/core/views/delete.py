from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import *


def excluir_aula(request,pk):
	aula = Aula.objects.get(pk=pk)
	turma = aula.turma_id
	aula.delete()
	return redirect ('turma', turma.pk)


def excluir_exercicio(request,pk):
	exe = Exercicio.objects.get(pk=pk)
	aula = exe.class_id
	exe.delete()
	return redirect ('exercicios', aula.pk)


def excluir_experimentacao(request,pk):
	exp = Experimentacao.objects.get(pk=pk)
	aula = exp.class_id
	exp.delete()
	return redirect ('experimentacoes', aula.pk)


def excluir_turma(request,pk):
	turma = Turma.objects.get(pk=pk)
	turma.delete()
	return redirect ('index')

