
# '======[Importaciones]============================'
from django import forms

from Apps.gestorUser import models as ModelsUser 

from django.contrib.auth.forms import UserCreationForm
# '================================================='

# °===========================°
#    °Formulario -> gestorUser
# °===========================°

# -=-=-=-=-=-=- FORMULARIO DE REGISTRO DE DOCENTES -=-=-=-=-=-=-

class DocenteSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = ModelsUser.User
        fields = ('username', 'email') 

    def save(self, commit=True):
        user = super().save(commit=True) 
        
        # ACTUALIZACION DE CAMPOS
        user.rol = ModelsUser.User.ROL_DOCENTE
        user.is_staff = False
        user.is_superuser = False
        
        # SE GUARDAN LOS CAMBIOS DEFINIDOS ANTES
        user.save(update_fields=['rol', 'is_staff', 'is_superuser']) 
        return user


# -=-=-=-=-=-=- FORMULARIO DE REGISTRO DE ADMINISTRADORES -=-=-=-=-=-=-

class AdminSignUpForm(UserCreationForm):

    # CLAVE temporal USADA PARA CONTROLAR EL acceso REALIZADO POR LOS USER
    claveAcceso = forms.CharField(max_length=30, label="Clave de acceso")

    class Meta(UserCreationForm.Meta):
        model = ModelsUser.User
        fields = ('username', 'email')

    def clean_claveAcceso(self):
        claveAcceso = self.cleaned_data['claveAcceso']

        # Validacion de identidad con la clave de acceso
        if claveAcceso != "CLAVE_SECRETA":
            raise forms.ValidationError("Error clave de acceso incorrecta.")
        return claveAcceso

    def save(self, commit=True):
        user = super().save(commit=False) 
        
        user.rol = ModelsUser.User.ROL_ADMIN
        user.is_staff = True
        user.is_superuser = True

        # si el commit es true se guardan los datos
        if commit:
            user.save() 
        return user



