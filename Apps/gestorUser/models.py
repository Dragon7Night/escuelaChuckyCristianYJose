
# '======[Importaciones]============================'
from django.db import models

from django.contrib.auth.models import AbstractUser
# '================================================='

# °===========================°
#    °Modelo -> Usuarios
# °===========================°

class User(AbstractUser):

    # DEFINICION DE CONSTANTES (roles en la DB)
    ROL_DOCENTE = "Docente"
    ROL_ADMIN = "Administrador"

    # opciones que se pueden seleccionar en los roles
    OPCIONES_ROL = [
        (ROL_DOCENTE, "Docente"),
        (ROL_ADMIN, "Administrador"),
    ]

    rol = models.CharField(max_length=15, choices=OPCIONES_ROL)

    @property
    def is_docent(self):
        return self.rol == self.ROL_DOCENTE

    @property
    def is_custom_admin(self):
        return self.rol == self.ROL_ADMIN
    
    def __str__(self):
        return f'{self.username} - {self.email}'


# ==============================================================================
# DOCUMENTACIÓN: GESTIÓN DE ROLES DE USUARIO
# ==============================================================================
# Este modelo User extiende AbstractUser de Django para implementar un sistema 
# de roles personalizado (Docentes y Administradores). Este archivo es el punto 
# de partida de toda la lógica de autorización del sistema.
#
# A continuación se explica el flujo de todo el proyecto:
#
# 1. MODELOS (models.py - Archivo actual):
#    - Se definen constantes (ROL_DOCENTE, ROL_ADMIN) para mantener consistencia.
#    - Se utilizan decoradores @property (`is_docent`, `is_custom_admin`) para
#      crear métodos booleanos accesibles directamente desde los templates 
#      definidos (ej. `user.is_docent`).
#    - Esta técnica reemplaza las validaciones por defecto de Django y facilita
#      la escalabilidad si en el futuro se agregan más roles.
#
# 2. FORMULARIOS (forms.py):
#    - Se definen formularios separados (DocenteSignUpForm, AdminSignUpForm) 
#      basados en UserCreationForm.
#    - Al sobrescribir el método `save(self, commit=True)`, se asigna de manera
#      automática e invisible el `rol` correspondiente al usuario que se registra.
#    - También se gestionan los permisos nativos de Django en ese momento 
#      (`is_staff` y `is_superuser` en True para admins, False para docentes).
#    - El AdminSignUpForm implementa una validación extra (`claveAcceso`) en su 
#      método clean para restringir la creación de superusuarios.
#
# 3. VISTAS Y URLS (views.py y url.py):
#    - Se separa completamente el flujo de acceso utilizando Vistas Basadas en 
#      Clases (CreateView para registros, LoginView para ingresos).
#    - Cada rol tiene sus propias rutas (ej. /crear-cuenta-docente/ vs 
#      /crear-cuenta-admin/), lo que permite cargar templates de registro e 
#      inicio de sesión personalizados por tipo de usuario.
#
# 4. PLANTILLAS / TEMPLATES (Ej: index.html):
#    - Las propiedades definidas en este modelo se inyectan en el contexto de 
#      los templates a través del objeto `user`.
#    - Permiten estructurar la interfaz con simples condicionales. Por ejemplo:
#      {% if user.is_custom_admin %} -> Muestra estadísticas o listas de alumnos.
#      {% elif user.is_docent %}     -> Muestra la vista simplificada del profesor.
#
#      Ejemplos en el proyecto: raiz_proyecto > templates > index > linea_88 a 
#      linea_104 y en la linea_19 a linea_62
# ==============================================================================

