
# '======[Importaciones]============================'
from django.contrib import admin
from django.urls import path, include

from Apps.gestorCursos import views as ViewsGeneral

# IMPORTACION DE REDIRECCIONAMIENTO AUTOMATICO 
# .DOC -> https://docs.djangoproject.com/en/5.2/topics/class-based-views/#:~:text=django.views.generic%20import%20TemplateView
from django.views.generic import RedirectView
# '==============================================='

# °======================================°
#    °URLs -> escuelaChuckyCristianYJose
# °======================================°

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuenta/', include("django.contrib.auth.urls")),

    # ------------------------------------
    #    -URL del LandingPage principal
    # ------------------------------------
    path('landing-page/', ViewsGeneral.landingPage, name='landingPage'),

    # -----------------------
    #    -URLs de Usuarios
    # -----------------------
    path('usuarios/', include("Apps.gestorUser.urls")),

    # -----------------------
    #    -URLs de Cursos
    # -----------------------
    path('cursos/', include("Apps.gestorCursos.urls")),

    # ------------------------------------------------
    # -Redireccionamiento automatico al landingPage
    # ------------------------------------------------
    path('', RedirectView.as_view(pattern_name='landingPage', permanent=False)),

]
