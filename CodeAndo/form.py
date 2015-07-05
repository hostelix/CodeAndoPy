from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

from CodeAndo.models import *


class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username","email")

    username = forms.CharField(
        label= "Usuario", max_length=30,
        help_text="Introduce tu nombre, Sin caracteres especiales. ",
        error_messages={
            "duplicate_value": "Este usuario ya existe en la base de datos",
            'invalid': "Debe de contener menos de 30 caracteres Alfanumericos[A-Z, 0-9]. ",
            },
        widget=forms.TextInput(attrs={
            "id":"usuario",
            "class":"form-control",
            "placeholder":"Usuario",
            "onkeydown":"return sin_espacios(event)"})
    )
    email = forms.EmailField(
        label="Email",
        help_text="Introduce tu email. Ej: Pedro@email.com",
        widget=forms.TextInput(attrs={
            "id":"email","class":"form-control",
            "placeholder":"Email",
            "type":"email",
            "onkeydown":"return sin_espacios(event)"})
    )

    password1 = forms.CharField(label="Password",
        widget=forms.PasswordInput(attrs={"id":"password1","class":"form-control","placeholder":"Password"})
    )
    password2 = forms.CharField(label="Password confirmacion",
        widget=forms.PasswordInput(attrs={"id":"password2","class":"form-control","placeholder":"Repite password"}),
        help_text="Introduce el password nuevamente para la verificacion."
    )



class InicioSesionForm(AuthenticationForm):
    username = forms.CharField(
        label= "Usuario", max_length=30,
        error_messages={
            'invalid': "Debe de contener menos de 30 caracteres Alfanumericos[A-Z, 0-9]. "},
        help_text="Introduce tu nombre, Sin caracteres especiales. ",

        widget=forms.TextInput(attrs={
            "id":"usuario",
            "class":"form-control",
            "placeholder":"Usuario",
            "onkeydown":"return sin_espacios(event)"})
    )
    password = forms.CharField(label="Password",
        widget=forms.PasswordInput(attrs={"id":"password","class":"form-control","placeholder":"Password"})
    )

class RegistroPersonaForm(forms.ModelForm):

    class Meta():
        model = Persona
        fields = ("primer_nombre","usuario","primer_apellido","segundo_nombre","segundo_apellido","cedula","fecha_nacimiento","sexo")

    primer_nombre = forms.CharField(
        label= "Primer nombre", max_length=15,
        error_messages={
            'invalid': "Debe de contener menos de 15 caracteres. "},
        help_text="Introduce tu primer nombre, Sin caracteres especiales. ",

        widget=forms.TextInput(attrs={
            "id":"primer_nombre",
            "class":"form-control",
            "placeholder":"Primer nombre",
            "onkeydown":"return sin_espacios(event)"})
    )
    segundo_nombre = forms.CharField(
        label= "Segundo nombre", max_length=15,
        error_messages={
            'invalid': "Debe de contener menos de 15 caracteres. "},
        help_text="Introduce tu segundo nombre, Sin caracteres especiales. ",

        widget=forms.TextInput(attrs={
            "id":"segundo_nombre",
            "class":"form-control",
            "placeholder":"Segundo nombre",
            "onkeydown":"return sin_espacios(event)"})
    )
    primer_apellido = forms.CharField(
        label= "Primer apellido", max_length=15,
        error_messages={
            'invalid': "Debe de contener menos de 15 caracteres. "},
        help_text="Introduce tu primer apellido, Sin caracteres especiales. ",

        widget=forms.TextInput(attrs={
            "id":"primer_apellido",
            "class":"form-control",
            "placeholder":"Primer apellido",
            "onkeydown":"return sin_espacios(event)"})
    )
    segundo_apellido = forms.CharField(
        label= "Segundo apellido", max_length=15,
        error_messages={
            'invalid': "Debe de contener menos de 15 caracteres. "},
        help_text="Introduce tu segundo apellido, Sin caracteres especiales. ",

        widget=forms.TextInput(attrs={
            "id":"segundo_apellido",
            "class":"form-control",
            "placeholder":"Segundo apellido",
            "onkeydown":"return sin_espacios(event)"})
    )
    cedula = forms.CharField(
        label= "Cedula", max_length=8,
        error_messages={
            'invalid': "Debe de contener menos de 8 caracteres. "},
        help_text="Introduce tu cedula, Sin caracteres especiales. ",

        widget=forms.TextInput(attrs={
            "id":"cedula",
            "class":"form-control",
            "placeholder":"Cedula",
            "onkeydown":"return sin_espacios(event)"})
    )
    fecha_nacimiento = forms.DateField(widget=forms.TextInput(attrs={
            "type":"date",
            "id":"fecha_nacimiento",
            "class":"form-control",
            "placeholder":"Fecha de nacimiento",
        })
    )

class ComentarioForm(forms.ModelForm):
    class Meta():
        model = Comentario
        fields = ("comentario","persona")


    comentario = forms.CharField(
        label= "Comentario", max_length=250,
        error_messages={
            'invalid': "Debe de contener menos de 250 caracteres. "},
        help_text="Haz tu comentario ",

        widget=forms.Textarea(attrs={
            "id":"comentario",
            "class":"form-control",
            "placeholder":"Comentar algo..",
            "rows":"3"
            })
    )


class RegistroAulaForm(forms.ModelForm):
    class Meta():
        model = Aula
        fields = ("descripcion","limite","asignatura","profesor", "fecha_fin")


    descripcion = forms.CharField(
        label= "Descripcion", max_length=50,
        error_messages={
            'invalid': "Debe de contener menos de 50 caracteres. "},
        help_text="Descripcion de el aula",

        widget=forms.Textarea(attrs={
            "id":"descripcion",
            "class":"form-control",
            "placeholder":"Descripcion del aula",
            "rows":"4"
            })
    )

    limite = forms.CharField(
        label= "Limite",
        error_messages={
            'invalid': " Error"},
        help_text="Numero maximo de personas en aula",

        widget=forms.TextInput(attrs={
            "id":"limite",
            "class":"form-control",
            "placeholder":"Limite de personas",
            })
    )

    fecha_fin = forms.DateField(
        label="Fecha fin de aula",
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"date"
        })
    )

    ASIGNATURAS = Asignatura.objects.all()
    PROFESORES = Profesor.objects.all()

    asignatura = forms.ModelChoiceField(
        ASIGNATURAS,
        empty_label="",
        label="Asignatura",
        initial=1,
        widget=forms.Select(attrs={
            "class":"form-control"
        }))

    profesor = forms.ModelChoiceField(
        PROFESORES,
        empty_label="",
        label="Profesor",
        initial=1,
        widget=forms.Select(attrs={
            "class":"form-control"
        }))


class RegistroProfesorForm(forms.ModelForm):
    class Meta():
        model = Profesor
        fields = ("especialidad","persona")

    especialidad = forms.CharField(
        label= "Especialidad", max_length=30,
        error_messages={
            'invalid': "Debe de contener menos de 30 caracteres. "},
        help_text="Especialidad del profesor",

        widget=forms.TextInput(attrs={
            "id":"especialidad",
            "class":"form-control",
            "placeholder":"Especialidad",
            })
    )

class RegistroAsignaturaForm(forms.ModelForm):
    class Meta():
        model = Asignatura
        fields = ("codigo","nombre")

    codigo = forms.CharField(
        label= "Codigo ", max_length=10,
        error_messages={
            'invalid': "Debe de contener menos de 10 caracteres. "},
        help_text="Introduce el codigo sin caracteres especiales",

        widget=forms.TextInput(attrs={
            "id":"codigo",
            "class":"form-control",
            "placeholder":"Codigo de la asignatura",
            })
    )

    nombre = forms.CharField(
        label= "Nombre", max_length=15,
        error_messages={
            'invalid': "Debe de contener menos de 15 caracteres. "},
        help_text="Introduce el nombre de la asignatura sin caracteres especiales",

        widget=forms.TextInput(attrs={
            "id":"nombre",
            "class":"form-control",
            "placeholder":"Nombre de la asignatura",
            })
    )




