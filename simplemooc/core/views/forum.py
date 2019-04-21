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
		
		context['pk'] = Turma.objects.get(pk = self.kwargs['pk'])

		return context

	def get_queryset(self):
		
		queryset = Forum.objects.filter(turma_id__pk = self.kwargs['pk'])
				
		order = self.request.GET.get('order', '')
		if order == 'answers':
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

def post_save_reply(created, instance, **kwargs):
	instance.forum_id.answers = instance.forum_id.replies.count()
	instance.forum_id.save()

def post_delete_reply(instance, **kwargs):
	instance.forum_id.answers = instance.forum_id.replies.count()
	instance.forum_id.save()

models.signals.post_save.connect(
	post_save_reply, sender=Resposta, dispatch_uid='post_save_reply'
)

models.signals.post_delete.connect(
	post_delete_reply, sender=Resposta, dispatch_uid='post_delete_reply'
)