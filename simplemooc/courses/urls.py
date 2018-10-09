from django.urls import path

from . import views

urlpatterns = [
    path('', views.cursos, name='cursos'),
    path('turma/', views.turma, name='turma'),
]

