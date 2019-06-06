from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('testes/<int:aula_id>/', views.testes, name='testes'),
    path('turmas/', views.index, name='index'),
    path('buscar/', views.buscar, name='buscar'),
    path('geogebra/', views.geogebra, name='geogebra'),


    #content
    path('aula/<int:pk>', views.aula, name='aula'),
    path('finalizar_aula/<int:pk>', views.finalizar_aula, name='finalizar_aula'),
    path('finalizar_experimentacao/<int:pk>', views.finalizar_experimentacao, name='finalizar_experimentacao'),
    path('exercicio/<int:exercise_id>', views.exercicio, name='exercicio'),
    path('ver_correcao/<int:exercise_id>', views.ver_correcao, name='ver_correcao'),
    path('corrigir/<int:turma_pk>/<int:aluno_pk>/', views.corrige_resposta_aberta, name='corrigir'),
    path('experimentacao/<int:pk>', views.experimentacao, name='experimentacao'),
    path('turmas/<int:pk>/', views.turma, name='turma'),
    path('exercicios/<int:pk>', views.exercicios, name='exercicios'),
    path('experimentacoes/<int:pk>', views.experimentacoes, name='experimentacoes'),
    path('listar_alunos/<int:turma_id>/', views.listar_alunos, name='listar_alunos'),

    #registration
    path('turmas/<int:pk>/matricula', views.matricula, name='matricula'),
    path('turmas/<int:pk>/desmatricular', views.desfazer_matricula, name='desmatricular'),
	path('conta/entrar/', LoginView.as_view(template_name='registration/login.html'), name='login'),
	path('conta/sair/', LogoutView.as_view(next_page='home'), name='logout'),
    path('conta/cadastrar/<int:user_type>', views.cadastrar, name='cadastrar'),
    
    #user
    path('usuario/<int:usuario_id>', views.usuario, name='usuario'),
    path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
    path('editar_senha/', views.editar_senha, name='editar_senha'),
    
    #creation
    path('criar_aula/<int:turma_id>/', views.criar_aula, name='criar_aula'),
    path('criar_exercicio/<int:class_id>/', views.criar_exercicio, name='criar_exercicio'),
    path('criar_experimentacao/<int:class_id>/', views.criar_experimentacao, name='criar_experimentacao'),
    path('criar_turma/<int:profesor_id>/', views.criar_turma, name='criar_turma'),
    path('criar_pergunta/<int:exercise_id>/', views.criar_pergunta, name='criar_pergunta'),
    path('criar_forum/<int:pk>/', views.criar_forum, name='criar_forum'),

    #delete
    path('excluir_aula/<int:pk>', views.excluir_aula, name='excluir_aula'),
    path('excluir_exercicio/<int:pk>', views.excluir_exercicio, name='excluir_exercicio'),
    path('excluir_experimentacao/<int:pk>', views.excluir_experimentacao, name='excluir_experimentacao'),
    path('excluir_turmas/<int:pk>/', views.excluir_turma, name='excluir_turma'),
    
    #forum
    path('forum/<int:pk>/', views.ForumView.as_view(), name='forum'),
    path('topic/<int:pk>', views.forum_topic, name='forum_topic'),
]