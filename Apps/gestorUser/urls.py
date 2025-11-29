
# '======[Importaciones]============================'
from django.urls import path
import Apps.gestorUser.views as GestionUsers
# '==============================================='

# °===========================°
#    °URLs -> gestorUser
# °===========================°

urlpatterns = [

    # ----------------------------
    #   -URLs ingreso de docentes
    # ----------------------------
    path("crear-cuenta-docente/", GestionUsers.CrearCuentaViewDocente.as_view(), name="crearCuentaDocente"),
    path("iniciar-sesion-docente/", GestionUsers.IniciarSesionViewDocente.as_view(), name="iniciarSesionDocente"),

    # ----------------------------
    #   -URLs ingreso del admin
    # ----------------------------
    path("crear-cuenta-admin/", GestionUsers.CrearCuentaViewAdmin.as_view(), name="crearCuentaAdmin"),
    path("iniciar-sesion-admin/", GestionUsers.IniciarSesionViewAdmin.as_view(), name="iniciarSesionAdmin"),
]

