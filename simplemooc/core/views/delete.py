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
	aula = exp.tema_id
	exp.delete()
	return redirect ('exercicios', aula.pk)


def excluir_turma(request,pk):
	turma = Turma.objects.get(pk=pk)
	turma.delete()
	return redirect ('index')


# def excluir_tema(request, pk):
# 	tema = Tema.objects.get(pk=pk)
# 	turma = tema.turma_id
# 	tema.delete()
# 	if turma:
# 		return redirect ('turma', turma.pk)
# 	else:
# 		return redirect ('index')


# def desvincular_tema(request, tema_id, turma_id):
# 	vinculo = Tema_Turma.objects.get(tema_id=tema_id, turma_id=turma_id)
# 	vinculo.delete()
# 	return redirect ('turma', turma_id)