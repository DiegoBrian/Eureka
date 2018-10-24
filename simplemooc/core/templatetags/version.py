from django import template
from django.conf import settings
import time
import re

register = template.Library()

@register.filter
def youtube(text):
    url = text.partition('=')
    if url:
    	tag = '<center><iframe class="embed-responsive-item" src="https://www.youtube.com/embed/'+url[2]+'" allowfullscreen> </iframe></center>'
    	return tag
    else:
    	return text
