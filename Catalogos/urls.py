from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^escuela/$',ListaEscuela.as_view(),name='lista-escuela'),
	url(r'^escuela/nuevo/$',NuevoEscuela.as_view(),
		name='nuevo-escuela'),
	url(r'^escuela/(?P<pk>\d+)/editar/$',EditarEscuela.as_view(),
		name='editar-escuela'),
 

	url(r'^nivel_educativo/$',ListaNivel.as_view(),
		name='lista-nivel'),
	url(r'^nivel_educativo/nuevo/$',NuevoNivel.as_view(),
		name='nuevo-nivel'),
	url(r'^nivel_educativo/(?P<pk>\d+)/editar/$',
		EditarNivel.as_view(),name='editar-nivel'),


	url(r'^ciclo_escolar/$',ListaCiclo.as_view(),
		name='lista-ciclo'),
	url(r'^ciclo_escolar/nuevo/$',NuevoCiclo.as_view(),
		name='nuevo-ciclo'),
	url(r'^ciclo_escolar/(?P<pk>\d+)/editar/$',
		EditarCiclo.as_view(),name='editar-ciclo'),


	url(r'^grados/$',ListaGrado.as_view(),name='lista-grado'),
	url(r'^grados/nuevo/$',NuevoGrado.as_view(),
		name='nuevo-grado'),
	url(r'^grados/(?P<pk>\d+)/editar/$',
		EditarGrado.as_view(),name='editar-grado'),


	url(r'^grupos/$',ListaGrupo.as_view(),name='lista-grupo'),
	url(r'^grupos/nuevo/$',NuevoGrupo.as_view(),
		name='nuevo-grupo'),
	url(r'^grupos/(?P<pk>\d+)/editar/$',
		EditarGrupo.as_view(),name='editar-grupo'),

	url(r'^profesores/$',ListaProfesor.as_view(),name='lista-profesor'),
	url(r'^profesores/nuevo/$',NuevoProfesor,
		name='nuevo-profesor'),
	url(r'^profesores/(?P<pk>\d+)/editar/$',
		EditarProfesor,name='editar-profesor'),

	url(r'^alumnos/$',ListaAlumno.as_view(),name='lista-alumno'),
	url(r'^alumnos/nuevo/$',NuevoAlumno,
		name='nuevo-alumno'),
]

