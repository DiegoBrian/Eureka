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
		fields = ['name', 'tema_id', 'text_content', 'visual_content', 'exercise_id', 'experimentation_id']
		widgets = {'tema_id' : HiddenInput()}

	def __init__(self, tema, *args, **kwargs):
		super(FormularioAula, self).__init__(*args, **kwargs)
		self.fields['exercise_id'].queryset = Exercicio.objects.filter(tema_id=tema)
		self.fields['experimentation_id'].queryset = Experimentacao.objects.filter(tema_id=tema)


class FormularioExercicio(BaseForm):
	class Meta:
		model = Exercicio
		fields = ['name', 'tema_id', 'multiple_times', 'class_id', 'experimentation_id']
		widgets = {'tema_id' : HiddenInput(), 'multiple_times': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'})}

	def __init__(self, tema, *args, **kwargs):
	    super(FormularioExercicio, self).__init__(*args, **kwargs)
	    self.fields['class_id'].queryset = Aula.objects.filter(tema_id=tema)
	    self.fields['experimentation_id'].queryset = Experimentacao.objects.filter(tema_id=tema)

class FormularioExperimentacao(BaseForm):
	class Meta:
		model = Experimentacao
		fields = ['name', 'tema_id', 'text_content', 'visual_content', 'source', 'class_id', 'exercise_id']
		widgets = {'tema_id' : HiddenInput()}

	def __init__(self, tema, *args, **kwargs):
	    super(FormularioExperimentacao, self).__init__(*args, **kwargs)
	    self.fields['exercise_id'].queryset = Exercicio.objects.filter(tema_id=tema)
	    self.fields['class_id'].queryset = Aula.objects.filter(tema_id=tema)


class FormularioTema(BaseForm):
	class Meta:
		model = Tema
		fields = ['name', 'turma_id']
		widgets = {'turma_id' : HiddenInput()}

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
		fields = ['username','email','name','gender','birth_date','user_type']
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
		fields = ['username','email','name','gender','grade','birth_date','user_type']
		widgets = {'user_type' : HiddenInput()}


class FormularioEditarConta(BaseForm):

	class Meta:
		model = User
		fields = ['username','email','name','gender','birth_date','grade']

class FormularioTeste(BaseForm):

	class Meta:
		model = Teste
		fields = ['text']

class FormularioCorrecao(BaseForm):

	class Meta:
		model = Usuario_Pergunta
		fields = ['score', 'comment']