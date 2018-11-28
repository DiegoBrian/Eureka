from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import *
from core.forms import FormularioCorrecao

@login_required
def aula(request, pk):
	aula = get_object_or_404(Aula, pk=pk)

	if not tem_acesso(request.user, aula.tema_id.turma_id.pk):
		messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
		return redirect('index')

	materiais = Material.objects.filter(aula_id = pk)
	context = {
		'aula' : aula,
		'materiais' : materiais
	}
	return render(request, 'content/aula.html', context)


@login_required
def finalizar_aula(request, pk):
	aula = Aula.objects.get(pk=pk)
	Aluno_Aula.objects.create(aluno_id = request.user, aula_id=aula)

	return redirect ('tema', aula.tema_id.pk)


@login_required
def experimentacao(request, pk):
	experimentacao = get_object_or_404(Experimentacao, pk=pk)

	if not tem_acesso(request.user, experimentacao.tema_id.turma_id.pk):
		messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
		return redirect('index')

	context = {
		'experimentacao' : experimentacao
	}
	return render(request, 'content/experimentacao.html', context)


@login_required
def exercicio(request, exercise_id):
	exercicio = get_object_or_404(Exercicio, pk=exercise_id)

	#se o usuario digita um url de uma turma que não é dono ou não está matriculado, acesso negado
	if not tem_acesso(request.user, exercicio.tema_id.turma_id.pk):
		messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
		return redirect('index')

	#se o usuario ja concluiu o exercício, verifica se ele é refazivel, se for, ok, se nao for, diz que ele ja fez
	exercicio_concluido = Aluno_Exercicio.objects.filter(aluno_id=request.user, exercicio_id=exercise_id)
	if exercicio_concluido:
		if exercicio_concluido[0].exercicio_id.multiple_times == False:
			messages.error(request, 'Você já concluiu este exercício!')
			return redirect('tema', pk = exercicio.tema_id.pk)
		else:
			Usuario_Pergunta.objects.filter(aluno_id=request.user, question_id__exercise_id=exercicio).delete()
			Aluno_Exercicio.objects.filter(aluno_id=request.user, exercicio_id=exercicio).delete()

	#verifica se o usuario ja respondeu alguma pergunta deste exercicio
	respondidos = Usuario_Pergunta.objects.filter(aluno_id=request.user, question_id__exercise_id=exercicio)
	#se ele ainda não respondeu nenhuma pergunta
	if not respondidos:
		#busca a primeira pergunta do exercicio
		pergunta = Pergunta.objects.filter(exercise_id=exercise_id, number=1)
		#coloca a primeira pergunta pra ser respondida apenas se existir alguma pergunta
		if pergunta:
			Usuario_Pergunta.objects.create(aluno_id=request.user, 
											question_id=pergunta[0],
											answered=False)

	#ve todas as perguntas que o usuario ja respondeu/esta respondendo
	respondidos = Usuario_Pergunta.objects.filter(aluno_id=request.user, question_id__exercise_id=exercicio, answered=False)

	#se tem pergunta no exercicio
	if respondidos:
		#pega a pergunta que está pra ser respondida
		pergunta = Pergunta.objects.get(exercise_id = exercise_id, number=respondidos[0].question_id.number)
		todas_perguntas = Pergunta.objects.filter(exercise_id= exercise_id)
	#se exercicio nao tem pergunta nenhuma, não manda nada
	else:
		pergunta = None
		todas_perguntas = None

	if request.method == 'POST':
		# se multipla escolha
		if pergunta.quesion_type=='FECHADA':
		# 	resposta_fechada = resposta
			resposta = request.POST.get('answer')
			Usuario_Pergunta.objects.filter(aluno_id = request.user, question_id= pergunta).update(student_answer=resposta)
			print(resposta)
		# se aberta
		else:
		# 	resposta_aberta = resposta
			resposta = request.POST.get('texto')
			Usuario_Pergunta.objects.filter(aluno_id = request.user, question_id= pergunta).update(student_text=resposta)
			print(resposta)
		# respondido = true
		Usuario_Pergunta.objects.filter(aluno_id = request.user, question_id= pergunta).update(answered=True)
		# vai na tabela exercicio_pergunta e ve se existe pergunta com numero = pergunta.numero+1
		proxima_pergunta = Pergunta.objects.filter(exercise_id=exercise_id, number=pergunta.number+1)
		# se existe
		if proxima_pergunta:
		# 	cria elemento na tabela usuario_pergunta com o numero pergunta.numero+1, respondido = false
			Usuario_Pergunta.objects.create(aluno_id=request.user, question_id=proxima_pergunta[0], answered = False)
			return redirect('exercicio', exercise_id=exercise_id)
		# senao
		else:
		# 	finalizar exercicio
			Aluno_Exercicio.objects.create(aluno_id=request.user, exercicio_id=exercicio)
			corrige_multipla_escolha(request.user,exercicio)
			return redirect('tema', pk = exercicio.tema_id.pk)

	context = {
		'exercicio' : exercicio,
		'pergunta' : pergunta,
		'perguntas' : todas_perguntas
	}
	return render(request, 'content/exercicio.html', context)


def corrige_multipla_escolha(user, exercise_id):
	usuario_perguntas = Usuario_Pergunta.objects.filter(aluno_id=user, question_id__exercise_id=exercise_id)
	for pergunta in usuario_perguntas:
		questao = Pergunta.objects.get(pk = pergunta.question_id.pk)
		if questao.quesion_type == 'FECHADA':
			if questao.correct_answer == pergunta.student_answer:
				Usuario_Pergunta.objects.filter(aluno_id=user, question_id=questao).update(correction='C')
				aluno_exercicio = Aluno_Exercicio.objects.get(exercicio_id=exercise_id, aluno_id=user)
				corrects = aluno_exercicio.corrects + 1
				Aluno_Exercicio.objects.filter(exercicio_id=exercise_id, aluno_id=user).update(corrects=corrects)
			else:
				Usuario_Pergunta.objects.filter(aluno_id=user, question_id=questao).update(correction='E')
				aluno_exercicio = Aluno_Exercicio.objects.get(exercicio_id=exercise_id, aluno_id=user)
				wrongs = aluno_exercicio.wrongs + 1
				Aluno_Exercicio.objects.filter(exercicio_id=exercise_id, aluno_id=user).update(wrongs=wrongs)

@login_required
def corrige_resposta_aberta(request, turma_pk, aluno_pk):
	nao_corrigidos = Usuario_Pergunta.objects.filter(aluno_id__pk = aluno_pk , question_id__exercise_id__tema_id__turma_id__pk = turma_pk, correction= 'N')
	print(len(nao_corrigidos))
	form = FormularioCorrecao(request.POST or None, instance = nao_corrigidos[0])
	if form.is_valid():
		correction = form.save(commit = False)
		correction.correction = 'C'
		correction.save()
		print(len(nao_corrigidos))
		if len(nao_corrigidos)>1:
			return redirect('corrigir', turma_pk=turma_pk, aluno_pk=aluno_pk)
		return redirect('listar_alunos', turma_id=turma_pk)

	context = {
		'pergunta': nao_corrigidos[0],
		'form': form
	}

	return render (request, 'content/corrigir.html', context)

@login_required
def turma(request, pk):
	turma = get_object_or_404(Turma, pk = pk)

	if not tem_acesso(request.user, turma.pk):
		messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
		return redirect('index')

	if request.method == 'POST' and 'btnsearch' in request.POST:
		srch = request.POST['search']
		temas = Tema.objects.filter(turma_id = pk , name__icontains=srch)
	else:
		temas = Tema.objects.filter(turma_id = pk)

	if request.method == 'POST' and 'btnmatricula' in request.POST:
		resposta = request.POST.getlist('alunos')
		print(resposta)
		####################.getlist########################
		matriculados = []
		for aluno in resposta:
			selecionado = Usuario.objects.get(pk=aluno)
			if Aluno_Turma.objects.filter(aluno_id=selecionado, turma_id=turma).exists():
				print ("Aluno ja matriculado")
			else:
				Aluno_Turma.objects.create(aluno_id=selecionado, turma_id=turma)
				matriculados.append(selecionado)
				
		if matriculados:
			messages.success(request, "Aluno(s) matriculado(s) com sucesso!")

	
	alunos = Usuario.objects.filter(user_type= 'ALUNO')
	nao_matriculados = []
	for aluno in alunos:
		if not esta_matriculado(aluno, turma.pk):
			nao_matriculados.append(aluno)

	context = {
		'turma': turma,
		'temas' : temas,
		'alunos' : nao_matriculados
	}
	return render(request, 'content/turma.html', context)


@login_required
def tema(request, pk):
	tema = get_object_or_404(Tema, pk = pk)

	if not tem_acesso(request.user, tema.turma_id.pk):
		messages.error(request, 'Você não tem permissão para acessar este conteúdo!')
		return redirect('index')


	if request.method == 'POST':
		srch = request.POST['search']
		aulas = Aula.objects.filter(tema_id = pk , name__icontains=srch)
		exercicios = Exercicio.objects.filter(tema_id = pk , name__icontains=srch)
		experimentacoes = Experimentacao.objects.filter(tema_id = pk , name__icontains=srch)
	else:
		aulas = Aula.objects.filter(tema_id = pk)
		exercicios = Exercicio.objects.filter(tema_id = pk)
		experimentacoes = Experimentacao.objects.filter(tema_id = pk)


	context = {
		'tema': tema,
		'aulas': aulas,
		'exercicios':exercicios,
		'experimentacoes':experimentacoes
	}
	return render(request,'content/tema.html', context)

@login_required
def listar_alunos(request, turma_id):
	alunos = Usuario.objects.filter(user_type= 'ALUNO')
	matriculados = []
	for aluno in alunos:
		if esta_matriculado(aluno, turma_id):
			matriculados.append(aluno)

	turma = Turma.objects.get(pk = turma_id)
	context = {
		'turma': turma,
		'alunos' : matriculados
	}
	return render(request, 'content/listar_alunos.html', context)


@login_required
def ver_correcao(request, exercise_id):
	exercicio_concluido = Aluno_Exercicio.objects.filter(aluno_id=request.user, exercicio_id=exercise_id)
	if exercicio_concluido:

		questoes = Usuario_Pergunta.objects.filter(question_id__exercise_id = exercise_id, aluno_id=request.user)

		context = {
			'questoes': questoes
		}

		return render (request, 'content/ver_correcao.html', context)


def esta_matriculado(user, turma_pk):
	turma = Turma.objects.get(pk = turma_pk)
	matricula = Aluno_Turma.objects.filter(aluno_id = user, turma_id = turma)

	if matricula:
		return True
	else:
		return False


def eh_responsavel(user, turma_pk):
	turma = Turma.objects.get(pk = turma_pk)

	if turma.responsible == user:
		return True
	else:
		return False


def tem_acesso(user, turma):
	if (user.user_type == 'ALUNO' and esta_matriculado(user, turma)) or (user.user_type == 'PROFESSOR' and eh_responsavel(user, turma)):
		return True
	else:
		return False
