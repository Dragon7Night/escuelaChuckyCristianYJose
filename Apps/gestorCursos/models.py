
# '======[Importaciones]============================'
from django.db import models
from django.conf import settings
# '================================================='

# °==============================°
#    °Modelo -> Gestor de cursos
# °==============================°

class Curso(models.Model):

    codigo = models.CharField(max_length=60)
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=300)

    creador_curso = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='cursos_creador')

    class Meta:
        ordering = ['codigo']

    def __str__(self):
        return f"Codigo: {self.codigo} - Curso: {self.nombre}"


class Alumno(models.Model):

    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    creador_alumno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='alumnos_creador')
    cursos_tomado = models.ManyToManyField(Curso, blank=True, related_name='alumnos_cursos')

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"Rut: {self.rut} - Nombre completo: {self.nombre} {self.apellido} - Fecha de nac.: {self.fecha_nacimiento}"
