# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.template import RequestContext as ctx
from django.forms.models import inlineformset_factory
# Create your views here.
class ListaEscuela(ListView):
	model = Escuela

class NuevoEscuela(CreateView):
	model = Escuela
	form_class = Cat_Escuela_Form
	success_url = reverse_lazy('catalogos:lista-escuela')

	def form_valid(self, form):
		return super(NuevoEscuela, self).form_valid(form)

class EditarEscuela(UpdateView):
    model = Escuela
    form_class = Cat_Escuela_Form
    success_url = reverse_lazy('catalogos:lista-escuela')


class ListaNivel(ListView):
	model = NivelEducativo

class NuevoNivel(CreateView):
	model = NivelEducativo
	form_class = Cat_Nivel_Educativo_Form
	success_url = reverse_lazy('catalogos:lista-nivel')

	def form_valid(self, form):
		return super(NuevoNivel, self).form_valid(form)

class EditarNivel(UpdateView):
    model = NivelEducativo
    form_class = Cat_Nivel_Educativo_Form
    success_url = reverse_lazy('catalogos:lista-nivel')




class ListaCiclo(ListView):
	model = CicloEscolar

class NuevoCiclo(CreateView):
	model = CicloEscolar
	form_class = Cat_Ciclo_Escolar_Form
	success_url = reverse_lazy('catalogos:lista-ciclo')

	def form_valid(self, form):
		return super(NuevoCiclo, self).form_valid(form)

class EditarCiclo(UpdateView):
	model = CicloEscolar
	form_class = Cat_Ciclo_Escolar_Form
	success_url = reverse_lazy('catalogos:lista-ciclo')




class ListaGrado(ListView):
	model = Grado 

class NuevoGrado(CreateView):
	model = Grado
	form_class = Cat_Grado_Form
	success_url = reverse_lazy('catalogos:lista-grado')

	def form_valid(self, form):
		return super(NuevoGrado, self).form_valid(form)

class EditarGrado(UpdateView):
	model = Grado
	form_class = Cat_Grado_Form
	success_url = reverse_lazy('catalogos:lista-grado')




class ListaGrupo(ListView):
	model = Grupo 

class NuevoGrupo(CreateView):
	model = Grupo
	form_class = Cat_Grupo_Form
	success_url = reverse_lazy('catalogos:lista-grupo')

	def form_valid(self, form):
		return super(NuevoGrupo, self).form_valid(form)

class EditarGrupo(UpdateView):
	model = Grupo
	form_class = Cat_Grupo_Form
	success_url = reverse_lazy('catalogos:lista-grupo')




class ListaProfesor(ListView):
	model = Profesor

def NuevoProfesor(request):
        if request.method == "POST":
            formpersona = Cat_Persona_Form(request.POST)
            formprof = Cat_Profesor_Form(request.POST)
            if formpersona.is_valid():
                post = formpersona.save(commit=False)
                post.save()
                persona = post.id
                
                user = Persona.objects.get(id=persona)

                if formprof.is_valid():
                	prof = formprof.save(commit=False)
                	prof.id_persona = user
                	prof.save()
                
                return redirect('catalogos:lista-profesor')
        else:
            formpersona = Cat_Persona_Form()
            formprof = Cat_Profesor_Form()
        return render(request, 'Catalogos/profesor_form.html', 
        	{'form1': formpersona,'form2': formprof})

def EditarProfesor(request, pk):
        
        formpersona = Cat_Persona_Form(request.POST)
        formprof = Cat_Profesor_Form(request.POST)
        user = Profesor.objects.get(id=pk)
        if formpersona.is_valid():
            post = formpersona.save(commit=False)
            post.id = user
            post.save()
                
            if formprof.is_valid():
             	prof = formprof.save(commit=False)
               	prof.id_persona = user
               	prof.save()
                
            return redirect('catalogos:lista-profesor')

        return render(request, 'Catalogos/profesor_form.html', 
        	{'form1': formpersona,'form2': formprof})


class ListaAlumno(ListView):
	model = Alumno


def NuevoAlumno(request):
        if request.method == "POST":
            formpersona = Cat_Persona_Form(request.POST)
            formalumno = Cat_Alumno_Form(request.POST)
            if formpersona.is_valid():
                post = formpersona.save(commit=False)
                post.save()
                persona = post.id
                
                user = Persona.objects.get(id=persona)

                if formalumno.is_valid():
                	prof = formalumno.save(commit=False)
                	prof.id_persona = user
                	prof.save()
                
                return redirect('catalogos:lista-alumno')
        else:
            formpersona = Cat_Persona_Form()
            formalumno = Cat_Alumno_Form()
        return render(request, 'Catalogos/alumno_form.html', 
        	{'form1': formpersona,'form2': formalumno})