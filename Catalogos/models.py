# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
class Escuela(models.Model):
	folio = models.CharField(max_length=50)
	nombre = models.CharField(max_length=250)
	direccion = models.CharField(max_length=250)

	def __str__(self):
		return '%s %s %s' % (self.folio, self.nombre, self.direccion)

@python_2_unicode_compatible
class NivelEducativo(models.Model):
	escuela = models.ForeignKey(Escuela)
	nivel = models.CharField(max_length=25)

	def __str__(self):
		return '%s' % ( self.nivel)


class Grado(models.Model):
	grado = models.IntegerField()

	def __str__(self):
		return '%d' % self.grado

class CicloEscolar(models.Model):
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()

	def __str__(self):
		return  '%d %d' % (self.fecha_inicio.year, self.fecha_fin.year)
@python_2_unicode_compatible
class Grupo(models.Model):
	id_grado = models.ForeignKey(Grado)
	id_escuela = models.ForeignKey(Escuela)
	id_ciclo = models.ForeignKey(CicloEscolar)
	id_nivel = models.ForeignKey(NivelEducativo)
	grupo = models.CharField(max_length=20)

	def __str__(self):
		return '%s %s %s' % (self.id_grado, self.grupo, self.id_nivel)


class Genero(models.Model):
	genero = models.CharField(max_length=15)

	def __str__(self):
		return '%s' % (self.genero)

class Persona(models.Model):
	nombre = models.CharField(max_length=55)
	paterno = models.CharField(max_length=20)
	materno = models.CharField(max_length=20)
	fecha_nacimiento = models.DateField()
	genero = models.ForeignKey(Genero)

	def __str__(self):
		return '%s %s %s' % (self.nombre, self.paterno, self.materno,
			)
	    
@python_2_unicode_compatible
class Alumno(models.Model):
	matricula = models.CharField(max_length=20)
	id_persona = models.ForeignKey(Persona)
	grupo = models.ForeignKey(Grupo)
	escuela = models.ForeignKey(Escuela)

	def __str__(self):
		return '%s %s %s %s' % (self.matricula, self.id_persona, self.grupo,
			self.escuela) 

@python_2_unicode_compatible
class Profesor(models.Model):
	id_persona= models.ForeignKey(Persona)
	grupo = models.ForeignKey(Grupo)

	def __str__(self):
		return '%s %s' % (self.id_persona, self.grupo)


