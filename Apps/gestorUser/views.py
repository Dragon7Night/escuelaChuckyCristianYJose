
# '======[Importaciones]============================'
from django.urls import reverse_lazy

from django.shortcuts import render

# Autenticación y vistas basadas en clases
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from Apps.gestorUser import forms as UsuariosForms
# '==============================================='

# °==============================°
#    °Views -> gestorUser
# °==============================°

# !|-|--|-|-|-|-|-|-|> VISTA BASADAS EN CLASE PARA LA GESTION DE CLIENTES <|-|--|-|-|-|-|-|-|-|-|-|-|-

class CrearCuentaViewDocente(CreateView):
    form_class = UsuariosForms.DocenteSignUpForm # Formulario personalizado
    success_url = reverse_lazy("iniciarSesionDocente") # redireccionamiento 
    template_name = "gestorUser\Acceso\Registro\\registro_docent.html" # ubicacion del template

class IniciarSesionViewDocente(LoginView):
    form_class = AuthenticationForm
    template_name = "gestorUser\Acceso\Ingreso\\ingreso_docent.html"
    redirect_authenticated_user = False

# !|-|--|-|-|-|-|-|-|> VISTA BASADAS EN CLASE PARA LA GESTION DE ADMINISTRADORES <|-|--|-|-|-|-|-|-|-|-|-|-|-

class CrearCuentaViewAdmin(CreateView):
    form_class = UsuariosForms.AdminSignUpForm
    success_url = reverse_lazy("iniciarSesionAdmin")
    template_name = "gestorUser\Acceso\Registro\\registro_adm.html"

class IniciarSesionViewAdmin(LoginView):
    form_class = AuthenticationForm
    template_name = "gestorUser\Acceso\Ingreso\\ingreso_adm.html"
    redirect_authenticated_user = False









