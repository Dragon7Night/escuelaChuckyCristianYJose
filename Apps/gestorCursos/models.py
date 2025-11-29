from django.db import models

# Create your models here.

class Curso(models.Model):

    codigo = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=300)

    class Meta:
        ordering = ['codigo']

    def __str__(self):
        return f"Curso: {self.nombre} Descripción: {self.descripcion} Codigo de curso: {self.codigo}"


class Alumno(models.Model):

    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    cursos_tomado = models.ManyToManyField(Curso, related_name='alumnoCursos', blank=True)

    class Meta:
        ordering = ['apellido']

    def __str__(self):
        return f"Rut: {self.rut} Nombre completo: {self.nombre} {self.apellido} Fecha de nacimiento: {self.fecha_nacimiento}"








