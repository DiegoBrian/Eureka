from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('testes/', views.testes, name='testes'),
    path('aula/<int:pk>', views.aula, name='aula'),
    path('turmas/', views.index, name='index'),
    path('turmas/<int:pk>/', views.turma, name='turma'),
    path('conta/', include('django.contrib.auth.urls')),
    path('conta/cadastrar/', views.cadastrar, name='cadastrar'),
]