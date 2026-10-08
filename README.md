# 🏎️ F1 Hub

Aplicación web desarrollada con **Django** que permite consultar y administrar información relacionada con la Fórmula 1, incluyendo pilotos, escuderías y temporadas.

El proyecto corresponde a la **Evaluación Sumativa N.º 2 de Programación Back End** y representa la evolución de una aplicación que inicialmente utilizaba archivos JSON hacia un sistema con persistencia en una base de datos relacional.

## Funcionalidades

- Visualización de pilotos y escuderías mediante tarjetas Bootstrap.
- Búsqueda de pilotos y escuderías.
- Selección y consulta de temporadas.
- Administración de registros mediante Django Admin.
- Operaciones CRUD: crear, consultar, modificar y eliminar registros.
- Gestión de relaciones entre pilotos, escuderías y temporadas.
- Acceso diferenciado para usuarios públicos y administradores.

## Tecnologías utilizadas

| Tecnología | Función |
|---|---|
| Python | Lenguaje de programación |
| Django | Framework web y ORM |
| HTML, CSS y Bootstrap | Interfaz de usuario |
| SQLite | Base de datos para desarrollo local |
| MariaDB | Base de datos relacional en AWS |
| phpMyAdmin | Verificación de tablas y registros |
| Git y GitHub | Control de versiones |
| AWS EC2 | Infraestructura cloud |
| Ubuntu | Sistema operativo del servidor |
| Gunicorn | Servidor de aplicaciones |
| Nginx | Servidor web y proxy inverso |

## Estructura del proyecto

```text
F1_Project/
├── escuderias/
├── f1_hub/
├── old_data/
├── pilotos/
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

Las aplicaciones principales son:

**pilotos:** administra la información de pilotos, temporadas y participaciones.

**escuderias:** administra los equipos de Fórmula 1 y sus datos.

## Modelos de datos

El proyecto utiliza cuatro entidades principales:

- **Piloto:** nombre, nacionalidad, fotografía e información.
- **Escuderia:** nombre, país, logotipo e información.
- **Temporada:** año y descripción.
- **ParticipacionPiloto:** relaciona un piloto con una escudería durante una temporada e incluye su número de competición.

Las relaciones se implementan mediante claves foráneas de Django ORM.

## Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/shinyx17/F1_Project.git
cd F1_Project
```

### 2. Crear y activar un entorno virtual

En Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

En Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

En Windows, la instalación de `mysqlclient` puede requerir herramientas adicionales de compilación, aunque el desarrollo local utilice SQLite.

### 4. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DJANGO_SECRET_KEY=tu_clave_secreta
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

Por defecto, el proyecto utiliza SQLite si no se define `DB_NAME`.

Para utilizar MariaDB, configurar también:

```env
DB_NAME=nombre_base_datos
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=3306
```

**Importante:** nunca subir el archivo `.env` ni las contraseñas al repositorio.

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

### 6. Importar datos iniciales

```bash
python manage.py importar_datos
```

### 7. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/` en el navegador.

Para acceder a Django Admin, crear primero un superusuario:

```bash
python manage.py createsuperuser
```

Después visitar `/admin/`.

## Despliegue en AWS

La aplicación fue desplegada en una instancia **Amazon EC2 con Ubuntu 24.04 LTS**.

Su arquitectura utiliza:

1. **Nginx:** recibe las solicitudes HTTP.
2. **Gunicorn:** ejecuta la aplicación Django.
3. **Django ORM:** gestiona las consultas y operaciones sobre los modelos.
4. **MariaDB:** almacena la información de manera persistente.
5. **phpMyAdmin:** permite verificar la estructura y los registros de la base de datos.

Gunicorn está configurado como servicio de `systemd` para iniciarse automáticamente con la instancia.

El acceso administrativo a phpMyAdmin se realiza mediante un túnel SSH.

La dirección IP pública de EC2 puede cambiar cuando la instancia se detiene y vuelve a iniciarse.

## Control de versiones

El código fuente se administra mediante Git y GitHub, utilizando commits para registrar los avances y cambios del proyecto.

**Repositorio:** https://github.com/shinyx17/F1_Project

## Uso de inteligencia artificial

Durante el desarrollo se utilizó ChatGPT como herramienta de apoyo para:

- Orientar la implementación de modelos y relaciones.
- Revisar configuraciones de Django.
- Resolver errores de desarrollo y despliegue.
- Apoyar la configuración de AWS, Gunicorn, Nginx y MariaDB.
- Elaborar documentación técnica.

Las soluciones propuestas fueron aplicadas y comprobadas mediante pruebas del proyecto.

## Estado del proyecto

La aplicación cuenta con visualización pública de datos, administración mediante Django Admin, persistencia relacional y despliegue en AWS EC2.

Proyecto desarrollado con fines académicos para la asignatura **Programación Back End**.