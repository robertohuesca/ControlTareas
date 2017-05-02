# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import Observacion
from .forms import Observacion_Form

# Create your views here.
def index( request ):
    contexto = {'msj':'Este es la vista principal', 'principal':'active'}
    return render_to_response('index.html', 
    	contexto)

class ListaObservacion(ListView):
	model = Observacion

class NuevoObservacion(CreateView):
	model = Observacion
	form_class = Observacion_Form
	success_url = reverse_lazy('control:lista-observacion')

	def form_valid(self, form):
		return super(NuevoObservacion, self).form_valid(form)


class EditarObservacion(UpdateView):
	model = Observacion
   	form_class = Observacion_Form
	success_url = reverse_lazy('control:lista-observacion')