from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404  

from core.models import Forum

class ForumView(ListView):

    paginate_by = 2
    template_name = 'forum/index.html'

    def get_queryset(self):
        queryset = Forum.objects.all()
        order = self.request.GET.get('order', '')
        if order == 'views':
            queryset = queryset.order_by('-views')
        elif order == 'answers':
            queryset = queryset.order_by('-answers')
        return queryset

def forum_topic(request, content, pk):
	if content == 'id':
		topic = Forum.objects.get(pk=pk)
	elif content == 'exp':
		topic = Forum.objects.get(experimentation_id__pk = pk)
	elif content == 'exe':
		topic = Forum.objects.get(exercise_id__pk = pk)
	elif content == 'cla':
		topic = Forum.objects.get(class_id__pk = pk)
	else:
		raise Http404

	context = {
		'topic' : topic,
		'content' : content
	}
	
	return render(request, "forum/topic.html", context)
