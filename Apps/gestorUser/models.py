
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
