
# '======[Importaciones]============================'
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponseRedirect 
from django.urls import reverse
from django.contrib.auth import get_user_model

from Apps.gestorCursos.forms import RegisterAlumnoForm, RegisterCursoForm

from Apps.gestorCursos import models as CursoModels  
from Apps.gestorUser import models as UserModels  

from django.contrib.auth.decorators import login_required, permission_required
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
@login_required(login_url='/landing-page/') # <- Requerimiento de login del User
def homeMain(request):

    ultimos_alumnos = CursoModels.Alumno.objects.all().order_by('-id')[:4]

    data = {'ultimos_alumnos': ultimos_alumnos}
    return render(request, 'index.html', data)


# !|-|--|-|-|-|-|-|-|> VISTAS DE CURSOS <|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

# .|----[Data cursos]-------------------------------------------|.
@login_required(login_url='/landing-page/') # <- Requerimiento de login del User
@permission_required(UserModels.User.ROL_ADMIN, login_url='/cursos/home/') # <- Requerimiento de rol especifica del User
def dataCursos(request):
    cursosObject = CursoModels.Curso.objects.all()
    data = {
        'CursosKey':cursosObject
    }
    return render(request, 'Gestion/Cursos/data_cursos.html',data)

    
# .|----[Registrar curso]-------------------------------------------|.
@login_required(login_url='/landing-page/') # <- Requerimiento de login del User
@permission_required(UserModels.User.ROL_ADMIN, login_url='/cursos/home/') # <- Requerimiento de rol especifica del User
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
@login_required(login_url='/landing-page/') # <- Requerimiento de login del User
@permission_required(UserModels.User.ROL_ADMIN, login_url='/cursos/home/') # <- Requerimiento de rol especifica del User
def editarCurso(request, id_curso):

    # obtiene el objeto ↓↓↓ o de caso contrario da un Error 404 
    cursoObject = get_object_or_404(CursoModels.Curso, id=id_curso)
    formCursos = RegisterCursoForm(instance=cursoObject)

    if request.method == 'POST':
        formCursos = RegisterCursoForm(request.POST, instance=cursoObject)
        if formCursos.is_valid():

            formCursos.save()
            return HttpResponseRedirect(reverse('data_cursos'))

    data = {
        'formKey':formCursos
    }
    return render(request, 'Gestion/Cursos/registrar_cursos.html',data)


# .|----[Eliminar curso]-------------------------------------------|.
@login_required(login_url='/landing-page/') # <- Requerimiento de login del User
@permission_required(UserModels.User.ROL_ADMIN, login_url='/cursos/home/') # <- Requerimiento de rol especifica del User
def eliminarCurso(request, id_curso):

    cursoObject = get_object_or_404(CursoModels.Curso, id=id_curso)
    cursoObject.delete()
    return HttpResponseRedirect(reverse('data_cursos'))



# !|-|--|-|-|-|-|-|-|> VISTAS DE ALUMNOS <|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

# .|----[Data alumnos]-------------------------------------------|.
@login_required(login_url='/landing-page/')
def data_alumnos(request):

    # Filtrado en la visualizacion de datos de los alumnos registrados

    # si el usuario tiene el rol de administrador custom (superUser o staff)
    # se muestran todos los alumnos sin restricciones
    if request.user.is_custom_admin:
        alumnoObject = CursoModels.Alumno.objects.all()

    # de caso contrario al usuarios solo se le mostraran los alumnos registrados
    # por el propio usuario
    else:#         FILTRO DE COMPARACION ENTRE EL UserName DEL CREADOR Y DEL USUARIO ACTUAL EN LA SESION
        alumnoObject = CursoModels.Alumno.objects.filter(creador_alumno=request.user)

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
            
            return HttpResponseRedirect(reverse('data_alumnos'))
    
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

            formAlumno.save()
            return HttpResponseRedirect(reverse('data_alumnos'))

    data = {
        'formKey':formAlumno
    }
    return render(request, 'Gestion/Alumnos/registrar_alumno.html',data)


# .|----[Eliminar alumno]-------------------------------------------|.
@login_required(login_url='/landing-page/') # <- Requerimiento de login del User
@permission_required(UserModels.User.ROL_ADMIN, login_url='/cursos/home/') # <- Requerimiento de rol especifica del User
def eliminarAlumno(request, id_alumno):
    alumnoObject = get_object_or_404(CursoModels.Alumno, id=id_alumno)
    alumnoObject.delete()
    return HttpResponseRedirect(reverse('data_alumnos'))
