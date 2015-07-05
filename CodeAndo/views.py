from django.shortcuts import render_to_response,HttpResponseRedirect,redirect,HttpResponse,get_object_or_404
from django.template import RequestContext
from django.http import JsonResponse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from CodeAndo.models import *
from CodeAndo.form import *
from CodeAndo.mensajes import *


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/inicio')

    return render_to_response("index/index.html",context_instance=RequestContext(request))


#Usuarios
def registro_usuario(request):
    mensajes = []
    clase  = ""
    if request.method == "POST":
        nuevo_registro = RegistroUsuarioForm(request.POST)

        if nuevo_registro.is_valid():
            nuevo_registro.save()
            formulario = RegistroUsuarioForm()
            mensajes.append(MENSAJES["REGISTRO-USUARIO"]["MSJ-USUARIO-CREADO"])
            clase = "alert alert-success"
        else:
            mensajes.append(nuevo_registro.errors)
            clase = "alert alert-danger"
            formulario = RegistroUsuarioForm(request.POST)
    else:
        formulario = RegistroUsuarioForm()

    return render_to_response("usuarios/registro_usuario.html",
                              {"formulario":formulario,"mensajes":{"mensajes":mensajes,"clase":clase}},
                              context_instance=RequestContext(request))


def inicio_sesion(request):
    mensajes = []
    if request.method == "POST":

        usuario = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=usuario,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return JsonResponse({"exito":"sesion-creada"})
            else:
                mensajes.append(MENSAJES["INICIO-SESION"]["ERROR-NO-ACTIVO"])
        else:
            mensajes.append(MENSAJES["INICIO-SESION"]["ERROR-AUTENTICAR"])

    formulario = InicioSesionForm()

    return render_to_response("usuarios/inicio_sesion.html",{"formulario":formulario, "mensajes":mensajes},context_instance=RequestContext(request))

@login_required(login_url="/")
def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect("/")


#@login_required(login_url="/")
def inicio(request):
    usuario = request.user

    try:
        datos_persona = Persona.objects.filter(usuario = usuario.id).get()
    except Persona.DoesNotExist:
        datos_persona = 0

    try:
        datos_profe = Profesor.objects.filter(persona__pk=datos_persona.id).get()

    except AttributeError:
        datos_profe = 0
    except Profesor.DoesNotExist:
        datos_profe = 0


    return render_to_response("inicio/inicio_principal.html",{
        "usuario":usuario,"datos_persona":datos_persona,
        "datos_profe":datos_profe},context_instance=RequestContext(request))



def registro_persona(request):
    mensajes = []
    clase = ""
    usuario = request.user
    if request.method == "POST":
        nuevo_registro = RegistroPersonaForm(request.POST)

        if nuevo_registro.is_valid():
            nuevo_registro.save()
            mensajes.append(MENSAJES["REGISTRO-PERSONA"]["EXITO-CREADA"])
            clase = "alert alert-success"
            formulario = RegistroPersonaForm()
            return  JsonResponse({"exito":True})
        else:
            mensajes.append(nuevo_registro.errors)
            clase = "alert alert-danger"

    formulario = RegistroPersonaForm()

    return render_to_response("personas/registro_persona.html",{"usuario":usuario,"formulario":formulario,"mensajes":mensajes,"clase":clase},context_instance=RequestContext(request))


def blog(request):

    if request.method == "POST":
        formulario = ComentarioForm(request.POST)

        if formulario.is_valid():
            formulario.save()

    formulario = ComentarioForm()
    datos_persona = Persona.objects.filter(usuario__pk=request.user.id).get()
    comentarios = Comentario.objects.all().order_by('-fecha')[:10]
    usuario = request.user

    return render_to_response("blog/inicio.html",{"datos_persona":datos_persona,"formulario":formulario, "comentarios":comentarios, "usuario":usuario},context_instance=RequestContext(request))

#Gestion de aulas
def mostrar_aulas(request):
    aulas = Aula.objects.all()

    return render_to_response("aulas/mostrar_aulas.html",{"aulas":aulas},context_instance=RequestContext(request))

def crear_aula(request):
    mensajes = []
    clase = ""
    if request.method == "POST":
        formulario = RegistroAulaForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            clase = "alert alert-success"
            mensajes.append("Se ha creado el aula con exito")
            JsonResponse({"exito":True})
        else:
            mensajes.append(formulario.errors)
            clase = "alert alert-danger"
    formulario = RegistroAulaForm()

    return render_to_response("aulas/crear_aula.html",{
        "formulario":formulario,"clase":clase,
        "mensajes":mensajes
    },context_instance=RequestContext(request))


def crear_profesor(request):
    mensajes = []
    clase = ""
    if request.method == "POST":
        formulario = RegistroProfesorForm(request.POST)

        if formulario.is_valid():
            formulario.save()

            JsonResponse({"exito":True})
            mensajes.append("Se ha creado el profesor con exito")
            clase = "alert alert-success"

        else:
            mensajes.append(formulario.errors)
            clase = "alert alert-danger"

    formulario = RegistroProfesorForm()
    datos_persona = Persona.objects.filter(usuario__pk=request.user.id).get()

    return render_to_response("profesores/crear_profesor.html",{"formulario":formulario,"datos_persona":datos_persona,"mensajes":mensajes,"clase":clase},context_instance=RequestContext(request))



def crear_asignatura(request):
    mensajes = []
    clase = ""
    if request.method == "POST":
        formulario = RegistroAsignaturaForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            mensajes.append("Se ha creado la asignatura %s con exito"%(request.POST["codigo"]))
            clase = "alert alert-success"
            JsonResponse({"exito":True})
        else:
            mensajes.append(formulario.errors)
            clase = "alert alert-danger"

    formulario = RegistroAsignaturaForm()
    datos_persona = Persona.objects.filter(usuario__pk=request.user.id).get()

    return render_to_response("asignaturas/crear_asignatura.html",{
        "formulario":formulario,"datos_persona":datos_persona,
        "mensajes":mensajes, "clase":clase},context_instance=RequestContext(request))


def aulas(request,id):
    aula=get_object_or_404(Aula,pk=id)
    datos_usuario = Persona.objects.filter(usuario__pk=request.user.id).get()
    usuario  = request.user
    print aula
    if aula:
        return render_to_response('aulas/index_aula.html',{'aula':aula, "datos_usuario":datos_usuario, "usuario":usuario},context_instance=RequestContext(request))

    return HttpResponseRedirect('/inicio')