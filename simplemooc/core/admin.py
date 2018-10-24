from django.contrib import admin

from .models import *


admin.site.register(Usuario)
admin.site.register(Turma)
admin.site.register(Aula)
admin.site.register(Exercicio)
admin.site.register(Pergunta)
admin.site.register(Tema)