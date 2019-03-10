from django import template
from django.conf import settings
from core.models import *
import time
import re

register = template.Library()

@register.filter
def youtube(text):
    url = text.split('=',1)
    if url[0] == text:
    	url = text.split('/',3)

    code = url[1][:11]

    if url:
    	tag = '<center><iframe class="embed-responsive-item" src="https://www.youtube.com/embed/'+code+'" allowfullscreen> </iframe></center>'
    	return tag
    else:
    	return text

@register.simple_tag
def load_my_courses(user):
	return Aluno_Turma.objects.filter(aluno_id=user)

@register.filter
def aula_concluida(user, pk):
    aula = Aula.objects.get(pk=pk)
    concluida = Aluno_Aula.objects.filter(aluno_id = user, aula_id=aula)
    if concluida:
        return True
    else:
        return False

@register.filter
def exercicio_concluido(user, pk):
    exercicio = Exercicio.objects.get(pk=pk)
    concluido = Aluno_Exercicio.objects.filter(aluno_id = user, exercicio_id=exercicio)
    if concluido:
        return True
    else:
        return False

@register.filter
def corrigir(user, pk):
    nao_corrigidos = Usuario_Pergunta.objects.filter(aluno_id = user, question_id__exercise_id__tema_id__turma_id__pk = pk, correction= 'N')

    if nao_corrigidos:
        return True
    else: 
        return False