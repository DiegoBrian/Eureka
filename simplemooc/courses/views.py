from django.shortcuts import render
from .models import Course

def cursos(request):
	courses = Course.objects.all();
	context = {
		'courses': courses
	}
	return render(request, 'cards.html', context)

def turma(request):
	return render(request, 'turma.html')
