from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import Http404  
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.models import *
from core.forms import FormularioResposta


class ForumView(ListView):

	paginate_by = 2
	template_name = 'forum/index.html'

	def get_context_data(self, **kwargs):
		context = super(ForumView, self).get_context_data(**kwargs)
		context['content'] = self.kwargs['content']
		if self.kwargs['content'] == 'exp':
			context['pk'] = Experimentacao.objects.get(pk = self.kwargs['pk']).name
		elif self.kwargs['content'] == 'exe':
			context['pk'] = Exercicio.objects.get(pk = self.kwargs['pk']).name
		elif self.kwargs['content'] == 'cla':
			context['pk'] = Aula.objects.get(pk = self.kwargs['pk']).name

		return context

	def get_queryset(self):
		if self.kwargs['content'] == 'exp':
			queryset = Forum.objects.filter(experimentation_id__pk = self.kwargs['pk'])
		elif self.kwargs['content'] == 'exe':
			queryset = Forum.objects.filter(exercise_id__pk = self.kwargs['pk'])
		elif self.kwargs['content'] == 'cla':
			queryset = Forum.objects.filter(class_id__pk = self.kwargs['pk'])
		else:
			raise Http404

		
		order = self.request.GET.get('order', '')
		if order == 'views':
			queryset = queryset.order_by('-views')
		elif order == 'answers':
			queryset = queryset.order_by('-answers')
		return queryset
		


@login_required
def forum_topic(request, pk):
	topic = Forum.objects.get(pk=pk)
	replies = Resposta.objects.filter(forum_id = topic)

	form = FormularioResposta(request.POST or None)
	if form.is_valid():
		reply = form.save(commit=False)
		reply.forum_id = topic
		reply.author = request.user
		reply.save()

		return redirect('forum_topic', pk=pk)

	context = {
		'topic' : topic,
		'replies' : replies,
		'form' : form
	}
	
	return render(request, "forum/topic.html", context)
