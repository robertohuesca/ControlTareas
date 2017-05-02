from django.forms import ModelForm
from Catalogos.models import *
from django import forms
from django.forms import ModelForm

class Cat_Escuela_Form(forms.ModelForm):

    class Meta:
        model = Escuela
        exclude = ['']

    def clean(self):
        return self.cleaned_data


class Cat_Nivel_Educativo_Form(forms.ModelForm):

    class Meta:
        model = NivelEducativo
        exclude = ['']

    def clean(self):
        return self.cleaned_data


class Cat_Ciclo_Escolar_Form(forms.ModelForm):

    class Meta:
        model = CicloEscolar
        exclude = ['']

    def clean(self):
        return self.cleaned_data


class Cat_Grado_Form(forms.ModelForm):

    class Meta:
        model = Grado
        exclude = ['']

    def clean(self):
        return self.cleaned_data


class Cat_Grupo_Form(forms.ModelForm):

    class Meta:
        model = Grupo
        exclude = ['']

    def clean(self):
        return self.cleaned_data


class Cat_Persona_Form(forms.ModelForm):

    class Meta:
        model = Persona
        exclude = ['']

    def clean(self):
        return self.cleaned_data


class Cat_Profesor_Form(forms.ModelForm):

    class Meta:
        model = Profesor
        exclude = ['id_persona']

    def clean(self):
        return self.cleaned_data

class Cat_Alumno_Form(forms.ModelForm):

    class Meta: 
        model = Alumno 
        exclude = ['id_persona']

    def clean(self):
        return self.cleaned_data