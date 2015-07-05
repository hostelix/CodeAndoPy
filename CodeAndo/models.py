from django.db import models
from django.contrib.auth.models import User

import datetime


class Persona(models.Model):
    usuario = models.ForeignKey(User)
    primer_nombre = models.CharField(max_length=15)
    segundo_nombre = models.CharField(max_length=15)
    primer_apellido = models.CharField(max_length=15)
    segundo_apellido= models.CharField(max_length=15)
    cedula = models.CharField(max_length=8, unique=True)
    fecha_nacimiento = models.DateField()
    tipo = models.ForeignKey('Tipo',default=1)
    permiso = models.ForeignKey('Permiso',default=1)

    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )

    sexo = models.CharField(max_length=1, choices=SEXO)

    def __str__(self):
        return "%s"%(self.usuario.username)

    def get_nombre_completo(self):
        return "%s %s"%(self.primer_nombre.capitalize(),self.primer_apellido.capitalize())

    def get_edad(self):
        delta = datetime.date.today() - self.fecha_nacimiento
        return "%d %s"%(datetime.date.fromordinal(delta.days).year, "a\xc3o")

    def get_permiso(self):
        return "%s"%(self.permiso.descripcion)

    def get_tipo_usuario(self):
        return "%s"%(self.tipo.descripcion)

    class Meta():
        db_table = "personas"


#tabla Asignatura
class Asignatura(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=15)

    class Meta():
        db_table = "asignaturas"

    def __str__(self):
        return "%d - %s"%(self.id,self.nombre.upper())

#tabla Aulas
class Aula(models.Model):
    descripcion = models.CharField(max_length=50, unique=True, blank=False)
    limite = models.IntegerField()
    asignatura = models.ForeignKey(Asignatura)
    profesor = models.ForeignKey('Profesor')
    fecha_inicio = models.DateField(auto_now=True)
    fecha_fin = models.DateField()

    alumnos = models.ManyToManyField(Persona)

    def get_limite(self):
        return "%s"%(self.limite)

    class Meta():
        db_table = "aulas"

class Permiso(models.Model):
    tipo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)

    class Meta():
        db_table = "permisos"

    def __str__(self):
        return "%s"%(self.tipo)

class Tipo(models.Model):
    descripcion = models.CharField(max_length=15)

    class Meta():
        db_table = "tipos"

    def __str__(self):
        return "%s"%(self.descripcion)

class Comentario(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.CharField(max_length=300)
    persona = models.ForeignKey(Persona)

    def obtener_usuario(self):
        return " %s"%(self.persona.usuario.username.capitalize())


    def obtener_fecha(self):
        return  "%s"%(self.fecha.date())

    class Meta():
        db_table = "comentarios"

#tabla Profesor
class Profesor(models.Model):
    especialidad = models.CharField(max_length=30)
    persona = models.ForeignKey(Persona)

    class Meta():
        db_table = "profesores"

    def __str__(self):
        return "%d - %s"%(self.id,self.persona.get_nombre_completo().upper())

