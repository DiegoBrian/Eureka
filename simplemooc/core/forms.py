from django import forms
from core.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import AdminDateWidget

class FormularioAula(forms.ModelForm):
	class Meta:
		model = Aula
		fields = ['name', 'tema_id', 'text_content', 'visual_content']


class FormularioTema(forms.ModelForm):
	class Meta:
		model = Tema
		fields = '__all__'


User = get_user_model()

class FormularioRegistro(forms.ModelForm):
	
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
		user = super(FormularioRegistro, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

	class Meta:
		model = User
		fields = ['username','email','name','gender','birth_date','grade','user_type']

class FormularioEditarConta(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username','email','name','gender','birth_date','grade']