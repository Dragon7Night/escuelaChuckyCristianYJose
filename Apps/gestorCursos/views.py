
# '======[Importaciones]============================'
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponseRedirect 
from django.urls import reverse
from django.contrib.auth import get_user_model

from Apps.gestorCursos.forms import RegisterAlumnoForm, RegisterCursoForm

from Apps.gestorCursos import models as CursoModels  

from django.contrib.auth.decorators import login_required
# '==============================================='

# °==============================°
#    °Views -> gestorCursos
# °==============================°

Usuario = get_user_model()

# !|-|--|-|-|-|-|-|-|> VISTAS DE PRINCIPALES <|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

# .|----[LandingPage]-------------------------------------------|.
def landingPage(request):
    return render(request, 'landingPage.html')

# .|----[Home principal de usuarios]----------------------------|.
@login_required(login_url='/landing-page/')
def homeMain(request):
    return render(request, 'index.html')


# !|-|--|-|-|-|-|-|-|> VISTAS DE CURSOS <|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

# .|----[Data cursos]-------------------------------------------|.
@login_required(login_url='/landing-page/')
def dataCursos(request):
    cursosObject = CursoModels.Curso.objects.all()
    data = {
        'CursosKey':cursosObject
    }
    return render(request, 'Gestion/Cursos/data_cursos.html',data)

    
# .|----[Registrar curso]-------------------------------------------|.
@login_required(login_url='/landing-page/')
def registrarCurso(request):
    formCursos = RegisterCursoForm() 
    
    if request.method == 'POST':
        formCursos = RegisterCursoForm(request.POST)
        if formCursos.is_valid():

            curso_instance = formCursos.save(commit=False)
            curso_instance.creador_curso = request.user
            curso_instance.save()

            # Guarda campos ManyToMany en el form
            formCursos.save_m2m()

            return HttpResponseRedirect(reverse('data_cursos'))
    
    data = {
        'formKey': formCursos
    }
    return render(request, 'Gestion/Cursos/registrar_cursos.html', data)


# .|----[Editar curso]-------------------------------------------|.
@login_required(login_url='/landing-page/')
def editarCurso(request, id_curso):

    # obtiene el objeto ↓↓↓ o de caso contrario da un Error 404 
    cursoObject = get_object_or_404(CursoModels.Curso, id=id_curso)
    formCursos = RegisterCursoForm(instance=cursoObject)

    if request.method == 'POST':
        formCursos = RegisterCursoForm(request.POST, instance=cursoObject)
        if formCursos.is_valid():

            # curso_instance = formCursos.save(commit=False)
            # curso_instance.save()
            formCursos.save()
            return HttpResponseRedirect(reverse('data_cursos'))

    data = {
        'formKey':formCursos
    }
    return render(request, 'Gestion/Cursos/registrar_cursos.html',data)


# .|----[Eliminar curso]-------------------------------------------|.
@login_required(login_url='/landing-page/')
def eliminarCurso(request, id_curso):

    cursoObject = get_object_or_404(CursoModels.Curso, id=id_curso)
    cursoObject.delete()
    return HttpResponseRedirect(reverse('data_cursos'))



# !|-|--|-|-|-|-|-|-|> VISTAS DE ALUMNOS <|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

# .|----[Data alumnos]-------------------------------------------|.
@login_required(login_url='/landing-page/')
def data_alumnos(request):
    alumnoObject = CursoModels.Alumno.objects.all()
    data = {
        'alumnoKey':alumnoObject
    }
    return render(request, 'Gestion/Alumnos/data_alumnos.html',data)

    
# .|----[Registrar alumno]-------------------------------------------|.
@login_required(login_url='/landing-page/')
def registrarAlumno(request):

    formAlumno = RegisterAlumnoForm() 

    if request.method == 'POST':
        formAlumno = RegisterAlumnoForm(request.POST)
        if formAlumno.is_valid():

            alumno_instance = formAlumno.save(commit=False)
            alumno_instance.creador_alumno = request.user
            alumno_instance.save()

            formAlumno.save()
            
            return HttpResponseRedirect(reverse('registrar_alumno'))
    
    data = {
        'formKey': formAlumno
    }
    return render(request, 'Gestion/Alumnos/registrar_alumno.html', data)


# .|----[Editar alumno]-------------------------------------------|.
@login_required(login_url='/landing-page/')
def editarAlumno(request, id_alumno):
    alumnoObject = get_object_or_404(CursoModels.Alumno, id=id_alumno)
    formAlumno = RegisterAlumnoForm(instance=alumnoObject)

    if request.method == 'POST':
        formAlumno = RegisterAlumnoForm(request.POST, instance=alumnoObject)
        if formAlumno.is_valid():

            # alumno_instance = formAlumno.save(commit=False)
            # alumno_instance.save()
            formAlumno.save()
            return HttpResponseRedirect(reverse('registrar_alumno'))

    data = {
        'formKey':formAlumno
    }
    return render(request, 'Gestion/Alumnos/registrar_alumno.html',data)


# .|----[Eliminar alumno]-------------------------------------------|.
@login_required(login_url='/landing-page/')
def eliminarAlumno(request, id_alumno):
    alumnoObject = get_object_or_404(CursoModels.Alumno, id=id_alumno)
    alumnoObject.delete()
    return HttpResponseRedirect(reverse('data_alumnos'))













