
# '======[Importaciones]============================'
from django import forms
from django.contrib.auth import get_user_model
from Apps.gestorCursos.models import Alumno, Curso

from django.core import validators
# '================================================='

# °==============================°
#    °Formulario -> gestorCursos
# °==============================°

Usuario = get_user_model()

class RegisterCursoForm(forms.Form):
    # Definicion + validacion + style + label de campos
    codigo = forms.CharField(validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(60)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. CC-JV-203'}),
        label='Código del curso'
    )

    nombre = forms.CharField(validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(80)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. Matemáticas'}),
        label='Nombre del curso'
    )

    descripcion = forms.CharField(validators=[
            validators.MinLengthValidator(0),
            validators.MaxLengthValidator(300)],
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Ej. Este curso trata sobre..'}),
        label='Descripción del curso'
    )

class RegisterCursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo', 'nombre', 'descripcion']
    
    # Definicion + validacion + style + label de campos
    codigo = forms.CharField(validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(60)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. CC-JV-203'}),
        label='Código del curso'
    )

    nombre = forms.CharField(validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(80)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. Matemáticas'}),
        label='Nombre del curso'
    )

    descripcion = forms.CharField(validators=[
            validators.MinLengthValidator(0),
            validators.MaxLengthValidator(300)],
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Ej. Este curso trata sobre..'}),
        label='Descripción del curso'
    )



class RegisterAlumnoForm(forms.Form):

    # Definicion + validacion + style + label de campos
    rut = forms.CharField(validators=[
            validators.MinLengthValidator(9),
            validators.MaxLengthValidator(10)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. 12345678-7'}),
        label='RUT del estudiante'
    )

    nombre = forms.CharField(validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(50)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. Pancho'}),
        label='Nombre'
    )

    apellido = forms.CharField(validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(50)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. Megidez'}),
        label='Apellido'
    )

    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'}),
        label='Fecha de nacimiento'
    )

    #  se encarga de traer todo los objetos ordenarlos  (cursos)  ↓↓
    cursos_tomado = forms.ModelMultipleChoiceField(queryset=Curso.objects.all().order_by('codigo'),
        widget=forms.CheckboxSelectMultiple,
        label='Marque uno o mas de los cursos disponibles',
        required=False
    )



class RegisterAlumnoForm(forms.ModelForm):


    class Meta:
        model = Alumno
        fields = ['rut','nombre','apellido','fecha_nacimiento','cursos_tomado']


    # Definicion + validacion + style + label de campos
    rut = forms.CharField(validators=[
            validators.MinLengthValidator(9),
            validators.MaxLengthValidator(10)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. 12345678-7'}),
        label='RUT del estudiante'
    )

    nombre = forms.CharField(validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(50)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. Pancho'}),
        label='Nombre'
    )

    apellido = forms.CharField(validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(50)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. Megidez'}),
        label='Apellido'
    )

    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'}),
        label='Fecha de nacimiento'
    )

    #  se encarga de traer todo los objetos ordenarlos  (cursos)  ↓↓
    cursos_tomado = forms.ModelMultipleChoiceField(queryset=Curso.objects.all().order_by('codigo'),
        widget=forms.CheckboxSelectMultiple,
        label='Marque uno o mas de los cursos disponibles'
    )

# OPCION PARA MULTIPLES OPCIONES (CTRL + CLIC) -> widget=forms.SelectMultiple(attrs={'class': 'form-control'})
