from django import template
from django.conf import settings
import time
import re

register = template.Library()

@register.filter
def youtube(text):
    url = text.partition('=')
    if url:
    	tag = '<center><iframe width="720" height="540" src="https://www.youtube.com/embed/'+url[2]+'"> </iframe></center>'
    	return tag
    else:
    	return text
