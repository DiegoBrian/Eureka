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

@register.simple_tag
def load_avaliable_courses(user):
	return Aluno_Turma.objects.exclude(aluno_id=user)