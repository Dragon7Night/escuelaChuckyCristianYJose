# 🎓 Escuela Chucky | Sistema de Gestión Escolar

Escuela Chucky es una aplicación web desarrollada con Django orientada a la administración de información académica y escolar.

## Características principales

- 👨‍🎓 **Gestión de estudiantes:** Registro y administración de información estudiantil.
- 🏫 **Administración escolar:** Organización de datos académicos y administrativos.
- 🗄️ **Persistencia de datos:** Almacenamiento seguro mediante MariaDB/MySQL.
- 🌐 **Aplicación web Django:** Arquitectura basada en el patrón MVT (Model-View-Template).

---

## Pre-requisitos

### Gestión de Base de Datos

Para el correcto funcionamiento del sistema es necesario contar con una instancia de base de datos MariaDB o MySQL.

Se recomienda utilizar alguna de las siguientes opciones:

- MariaDB 10.11 o superior.
- MySQL 8.0 o superior.
- XAMPP con el motor MySQL.

🔗 https://www.apachefriends.org/es/index.html

### Python

Se recomienda utilizar Python 3.11 o superior.

Verificar instalación:

```bash
py --version
```

---

## Librerías principales

El núcleo del proyecto utiliza las siguientes dependencias:

- `django` (Framework Web)
- `pymysql` (Conector para MariaDB/MySQL)
- `mysqlclient` (Controlador de base de datos MySQL)

**Nota:** No es necesario instalar las dependencias manualmente, ya que el proyecto incorpora un archivo `requirements.txt`.

---

# Configuración de Base de Datos necesaria (MySQL)

Antes de ejecutar la aplicación, es necesario crear una base de datos y un usuario con privilegios sobre ella.

Ejemplo:

```sql
CREATE DATABASE db_django;

CREATE USER 'django_db'@'localhost'
IDENTIFIED BY 'django_pass';

GRANT ALL PRIVILEGES
ON db_django.*
TO 'django_db'@'localhost';

FLUSH PRIVILEGES;
```

Posteriormente, verificar que las credenciales coincidan con la configuración definida en el archivo `settings.py`, el cual debe tener una estructura similar a la siguiente:

Ejemplo:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_django',
        'USER': 'django_db',
        'PASSWORD': 'django_pass',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
```

---

# Pasos para la Instalación

## 1. Ubicarse en una ruta de trabajo

Ejemplo:

```bash
cd C:/
mkdir ProyectosGit
cd ProyectosGit
```

---

## 2. Clonar el repositorio

```bash
git clone https://github.com/Dragon7Night/escuelaChuckyCristianYJose.git
```

---

## 3. Acceder a la carpeta del proyecto

```bash
cd escuelaChuckyCristianYJose
```

**Nota:** Si no deseas trabajar con un entorno virtual, puedes avanzar directamente al paso 6.

---

## 4. Crear entorno virtual (Opcional)

```bash
py -m venv .env
```

---

## 5. Activar entorno virtual (Opcional)

```bash
.env\Scripts\activate
```

Para desactivar el entorno virtual:

```bash
deactivate
```

---

## 6. Instalar dependencias

```bash
pip install -r requirements.txt
```

Verificar dependencias instaladas (Opcional):

```bash
pip list
```

---

## 7. Aplicar migraciones


Crear migraciones
```bash
py manage.py makemigrations
```

Migraciónes por aplicaciónes (en caso de error con la migraciones):

```bash
py manage.py makemigrations gestorCursos
```

```bash
py manage.py makemigrations gestorUser
```

Aplicar migraciones-
```bash
py manage.py migrate
```

---

## 8. Iniciar servidor de desarrollo

Opción 1:

```bash
py manage.py runserver
```

Opción 2:

```bash
py -m django runserver
```

---

## Acceso al sistema

Una vez iniciado el servidor, acceder desde el navegador a:

```text
http://127.0.0.1:8000/
```
