
# '======[Importaciones]============================'
from django.urls import path
import Apps.gestorCursos.views as GestionCursos
# '==============================================='

# °===========================°
#    °URLs -> gestorCursos
# °===========================°

urlpatterns = [

    path('home/', GestionCursos.homeMain, name='homeMain'),

    # ----------------------------
    #   -URLs gestion de cursos
    # ----------------------------
    path('data-cursos/', GestionCursos.dataCursos, name='data_cursos'),
    path('registrar-curso/', GestionCursos.registrarCurso, name='registrar_curso'),
    path('editar-curso/<int:id_curso>', GestionCursos.editarCurso, name='editar_curso'),
    path('eliminar-curso/<int:id_curso>', GestionCursos.eliminarCurso, name='eliminar_curso'),

    # ----------------------------
    #   -URLs gestion de alumnos
    # ----------------------------
    path('data-alumnos/', GestionCursos.data_alumnos, name='data_alumnos'),
    path('registrar-alumno/', GestionCursos.registrarAlumno, name='registrar_alumno'),
    path('editar-alumno/<int:id_alumno>', GestionCursos.editarAlumno, name='editar_alumno'),
    path('eliminar-alumno/<int:id_alumno>', GestionCursos.eliminarAlumno, name='eliminar_alumno'),



]

