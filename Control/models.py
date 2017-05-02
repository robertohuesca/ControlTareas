# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Catalogos.models import Alumno
from django.db import models

# Create your models here.
class Observacion(models.Model):
	fecha = models.DateField()
	observacion = models.TextField()
	alumno = models.ForeignKey(Alumno)

	def __str__(self):
		return '%s %s %s' % (self.fecha, self.observacion, self.alumno)