
# '======[Importaciones]============================'
from django import forms
from django.contrib.auth import get_user_model
from .models import Curso
from Apps.gestorCursos.models import Alumno


from django.core import validators
# '================================================='

# °==============================°
#    °Formulario -> gestorCursos
# °==============================°

Usuario = get_user_model()

class RegisterCursoForm(forms.Form):
    codigo = forms.FloatField(validators=[
        validators.MinValueValidator(0)
    ])
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    descripcion = forms.CharField(validators=[
        validators.MinLengthValidator(0),
        validators.MaxLengthValidator(300)
    ])

    codigo.label = 'Codigo'
    nombre.label = 'Nombre'
    descripcion.label = 'Descripcion'

    codigo.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['class'] = 'form-control'

class RegisterCursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo', 'nombre', 'descripcion']
    

    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    descripcion = forms.CharField(validators=[
        validators.MinLengthValidator(0),
        validators.MaxLengthValidator(300)
    ])

    codigo = forms.IntegerField()




class RegisterAlumnoForm(forms.Form):

    rut = forms.IntegerField()
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    apellido = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    
    rut.label = 'Rut'
    nombre.label = 'Nombre'
    apellido.label = 'Apellido'

    rut.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'


class RegisterAlumnoForm(forms.ModelForm):
    class Meta:
       
        model = Alumno
        fields = ['rut', 'nombre', 'apellido', 'fecha_nacimiento','cursos_tomado']
    

    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    apellido = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])

    rut = forms.IntegerField()









# from django import forms
# from .models import  Alumno

# from django.core import validators


# class RegisterAlumnoForm(forms.Form):

#     rut = forms.IntegerField()
#     nombre = forms.CharField(validators=[
#         validators.MinLengthValidator(3),
#         validators.MaxLengthValidator(25)
#     ])
#     apellido = forms.CharField(validators=[
#         validators.MinLengthValidator(3),
#         validators.MaxLengthValidator(25)
#     ])
    

#     rut.label = 'Rut'
#     nombre.label = 'Nombre'
#     apellido.label = 'Apellido'

#     rut.widget.attrs['class'] = 'form-control'
#     nombre.widget.attrs['class'] = 'form-control'
#     apellido.widget.attrs['class'] = 'form-control'


      
# class RegisterAlumnoForm(forms.ModelForm):
#     class Meta:
#         model = Alumno
#         fields = '__all__'
    
# # Definicion de campos del fourmulario + validaciones simples
#     nombre = forms.CharField(validators=[
#         validators.MinLengthValidator(3),
#         validators.MaxLengthValidator(25)
#     ])
#     apellido = forms.CharField(validators=[
#         validators.MinLengthValidator(3),
#         validators.MaxLengthValidator(25)])

#     rut = forms.IntegerField()
