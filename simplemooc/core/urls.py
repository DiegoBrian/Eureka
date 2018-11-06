from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('testes/', views.testes, name='testes'),
    path('turmas/', views.index, name='index'),

    #content
    path('aula/<int:pk>', views.aula, name='aula'),
    path('exercicio/<int:pk>', views.exercicio, name='exercicio'),
    path('experimentacao/<int:pk>', views.experimentacao, name='experimentacao'),
    path('turmas/<int:pk>/', views.turma, name='turma'),
    path('tema/<int:pk>/', views.tema, name='tema'),

    #registration
    path('turmas/<int:pk>/matricula', views.matricula, name='matricula'),
    path('turmas/<int:pk>/desmatricular', views.desfazer_matricula, name='desmatricular'),
	path('conta/entrar/', LoginView.as_view(template_name='registration/login.html'), name='login'),
	path('conta/sair/', LogoutView.as_view(next_page='home'), name='logout'),
    path('conta/cadastrar/<int:user_type>', views.cadastrar, name='cadastrar'),
    
    #user
    path('usuario/', views.usuario, name='usuario'),
    path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
    path('editar_senha/', views.editar_senha, name='editar_senha'),
    
    #creation
    path('criar_aula/<int:tema_id>/', views.criar_aula, name='criar_aula'),
    path('criar_exercicio/<int:tema_id>/', views.criar_exercicio, name='criar_exercicio'),
    path('criar_experimentacao/<int:tema_id>/', views.criar_experimentacao, name='criar_experimentacao'),
    path('criar_tema/<int:turma_id>/', views.criar_tema, name='criar_tema'),
    path('criar_turma/<int:profesor_id>/', views.criar_turma, name='criar_turma'),
    path('criar_pergunta/<int:exercise_id>/', views.criar_pergunta, name='criar_pergunta'),
    path('criar_pergunta_fechada/<int:exercise_id>/', views.criar_pergunta_fechada, name='criar_pergunta_fechada'),
]