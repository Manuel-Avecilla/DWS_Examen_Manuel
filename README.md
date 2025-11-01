# Examen - Desarrollo Web Entorno Servidor

Este proyecto está desarrollado con **Django** y tiene como objetivo gestionar concursos, permitiendo que **administradores** creen competencias, **participantes** se inscriban y presenten trabajos, y **jurados** los evalúen.  
También incluye un sistema de **notificaciones** y **perfiles de usuario**.

---
## Instalación y ejecución en local

#### 1. Clonar el repositorio:
```bash
git clone git@github.com:Manuel-Avecilla/DWS_Examen_Manuel.git
```
#### 2. Crear entorno virtual:
```bash
cd DWS_Examen_Manuel/app/
```
```bash
python3 -m venv myvenv
```
#### 3. Activar entorno:
```bash
source myvenv/bin/activate
```
#### 4. Actualizar pip (opcional, pero recomendable):
```bash
python -m pip install --upgrade pip
```
#### 5. Instalar los requerimientos del proyecto:
```bash
pip install -r requirements.txt
```
#### 6. Creamos la base de datos:
```bash
python manage.py migrate
```
---
## Documentación

Para mantener el README principal más limpio, la documentación detallada se encuentra en los siguientes archivos:

- [Modelos del Sistema](docs/modelos.md)
- [URLS del Sistema](docs/url.md)

---

## Tecnologías
- **Framework:** Django (Python)
- **Base de datos:** SQLite
- **ORM:** Django Models

---

## Autor
**Manuel Avecilla 2ºDAW.**
