from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^observaciones/$',ListaObservacion.as_view()
		,name='lista-observacion'),
	url(r'^observaciones/nuevo/$',NuevoObservacion.as_view(),
		name='nuevo-observacion'),
	url(r'^observaciones/(?P<pk>\d+)/editar/$',
		EditarObservacion.as_view(),name='editar-observacion'),
	url(r'^',index,name='index'),

]