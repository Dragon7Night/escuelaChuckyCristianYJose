from django.contrib import admin

from Apps.gestorCursos import models as ModelsCurso

# Register your models here.


class CursoAdmin(admin.ModelAdmin):
    list_display = ['id','codigo','nombre','descripcion']

admin.site.register(ModelsCurso.Curso, CursoAdmin)



class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['id','rut','nombre','apellido','fecha_nacimiento']

admin.site.register(ModelsCurso.Alumno, AlumnoAdmin)


