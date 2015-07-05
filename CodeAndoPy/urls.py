from django.conf.urls import patterns, include, url
from django.contrib import admin
from CodeAndo.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CodeAndoPy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index,name="index"),

    #Usuarios
    url(r'^GestionUsuario/inicio_sesion$',inicio_sesion,name="iniciar_sesion"),
    url(r'^GestionUsuario/cerrar_sesion$',cerrar_sesion,name="cerrar_sesion"),

    url(r'^GestionUsuario/registro_usuario$',registro_usuario,name="registrarse"),


    url(r'^inicio/$',inicio,name="inicio"),


    url(r'^GestionPersona/registro_persona$',registro_persona,name="registro_persona"),

    url(r'^blog/$',blog,name="blog"),

    url(r'^GestionAulas/mostrar_aulas$',mostrar_aulas,name="mostrar_aulas"),
    url(r'^GestionAulas/crear_aula$',crear_aula,name="crear_aula"),

    url(r'^GestionProfesores/crear_profesor$',crear_profesor,name="crear_profesor"),
    #url(r'^GestionProfesores/mostrar_profesores$',mostrar_prfesores,name="mostrar_profesores"),

    url(r'^GestionAsignaturas/crear_asignatura$',crear_asignatura,name="crear_asignatura"),

    url(r'^Aulas/(?P<id>\d+)$',aulas),

)
