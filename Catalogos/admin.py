# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import (Escuela, NivelEducativo, Grado, CicloEscolar, 
	Grupo,  Persona, Alumno, Profesor, Genero)
from django.contrib import admin

# Register your models here.
@admin.register(Escuela)
class AdminEscuela(admin.ModelAdmin):
	list_display = ('id', 'folio', 'nombre', 'direccion')


@admin.register(NivelEducativo)
class AdminNivel(admin.ModelAdmin):
	list_display = ('id', 'nivel', 'escuela')


@admin.register(Grado)
class AdminGrado(admin.ModelAdmin):
	list_display = ('id', 'grado')


@admin.register(CicloEscolar)
class AdminCiclo(admin.ModelAdmin):
	list_display = ('id', 'fecha_inicio', 'fecha_fin')


@admin.register(Grupo)
class AdminGrupo(admin.ModelAdmin):
	list_display = ('id', 'id_grado', 'id_escuela', 'id_ciclo', 
		'id_nivel','grupo')

@admin.register(Genero)
class AdminGrado(admin.ModelAdmin):
	list_display = ('id', 'genero')

@admin.register(Persona)
class AdminPersona(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'paterno', 'materno', 
		'fecha_nacimiento',  'genero')

@admin.register(Alumno)
class AdminAlumno(admin.ModelAdmin):
	list_display = ('id', 'matricula', 'id_persona', 'grupo'
		,'escuela')

@admin.register(Profesor)
class AdminProfesor(admin.ModelAdmin):
	list_display = ('id', 'id_persona', 'grupo')


