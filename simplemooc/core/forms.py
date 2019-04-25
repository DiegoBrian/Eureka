from django import forms
from core.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import Textarea, HiddenInput, DateInput, NumberInput
from django.contrib.admin.widgets import AdminDateWidget


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class FormularioResposta(BaseForm):
	class Meta:
		model = Resposta
		fields = ['reply']


class FormularioForum(BaseForm):
	class Meta:
		model = Forum
		fields = ['name','body', 'author']
		widgets = {'author' : HiddenInput()}


class FormularioAula(BaseForm):
	class Meta:
		model = Aula
		fields = ['name', 'turma_id', 'summary', 'visual_content', 'text_content']
		widgets = {'turma_id' : HiddenInput(), 'summary': Textarea(attrs={'rows':4})}


class FormularioExercicio(BaseForm):
	class Meta:
		model = Exercicio
		fields = ['name', 'multiple_times', 'class_id']
		widgets = {'class_id' : HiddenInput(), 'multiple_times': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'})}


class FormularioExperimentacao(BaseForm):
	class Meta:
		model = Experimentacao
		fields = ['name', 'exp_type', 'visual_content', 'text_content', 'source', 'class_id']
		widgets = {'class_id' : HiddenInput()}


class FormularioTurma(BaseForm):
	class Meta:
		model = Turma
		fields = '__all__'
		widgets = {'responsible' : HiddenInput()}


class FormularioPergunta(BaseForm):
	class Meta:
		model = Pergunta
		fields = '__all__'
		widgets = {'exercise_id' : HiddenInput(), 'number' : HiddenInput()}


User = get_user_model()

class FormularioRegistroProfessor(BaseForm):
	
	email = forms.EmailField(label = 'Email')
	password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('As senhas não são iguais')
		return password2

	def save(self, commit=True):
		user = super(FormularioRegistroProfessor, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

	class Meta:
		model = User
		fields = ['username','email','name','gender','birth_date','image','user_type']
		widgets = {'user_type' : HiddenInput()}


class FormularioRegistroAluno(BaseForm):
	
	email = forms.EmailField(label = 'Email')
	password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('As senhas não são iguais')
		return password2

	def save(self, commit=True):
		user = super(FormularioRegistroAluno, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

	class Meta:
		model = User
		fields = ['username','email','name','gender','grade','birth_date','image','user_type']
		widgets = {'user_type' : HiddenInput()}


class FormularioEditarConta(BaseForm):

	class Meta:
		model = User
		fields = ['username','email','name','gender','birth_date','grade', 'image']

class FormularioTeste(BaseForm):

	class Meta:
		model = Teste
		fields = ['text']

class FormularioCorrecao(BaseForm):

	class Meta:
		model = Usuario_Pergunta
		fields = ['score', 'comment']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'image', 'aula_id')
        widgets = {'aula_id' : HiddenInput()}