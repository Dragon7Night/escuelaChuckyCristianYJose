
# '======[Importaciones]============================'
from django.contrib import admin


from django.contrib.auth.admin import UserAdmin
from Apps.gestorUser import models as ModelsUser

# '================================================='

# °===========================°
#    °Admin CRUD -> Usuarios
# °===========================°

# -.-.-.-.-.- CRUD de usuarios 
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('camposExtras', {'fields': ('rol',)}),
    )
    list_display = ['username', 'email', 'rol', 'is_staff']

admin.site.register(ModelsUser.User, UsuarioAdmin)
