from django.urls import include, path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('testes/', views.testes, name='testes'),
    path('aula/<int:pk>', views.aula, name='aula'),
    path('turmas/', views.index, name='index'),
    path('turmas/<int:pk>/', views.turma, name='turma'),
	path('conta/entrar/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('conta/cadastrar/', views.cadastrar, name='cadastrar'),
]