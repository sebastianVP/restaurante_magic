# Sistema de Reservas en Restaurantes
---

Este es un proyecto de aplicacion web en Django que permite a los usuarios 
seleccion entre seis opciones de restaurantes y realizar un reserva en el restaurante
de su eleccion. La interfaz de usuario es intuitiva gracias al uso de Bootstrap.

## DESCRIPCION GENERAL

La aplicacion permite a los usuarios:
- Ver una lista de restaurantes con sus respectivas descripciones y ubucaciones.
- Seleccionar un resturante especifico y llenar un formulario de reserva con sus datos.
- Confirmar su reserva y ver un mensaje de éxito.

## Estructura del Proyecto

El proyecto sigue la estructura estandar de Django con una aplicacion llamada **reservations**.
Los componentes principales incluyen:

- **Modelos:** Representa los restaurantes y las reservas en la base de datos.
- **Vistas:** Gestionan la logica de negocio, como lista de restaurantes y la creacion de reservas.
- **URLs:** Configurar las rutas para acceder a las vistas
- **Plantillas:** HTML para represetar los datos al usuario con una interfaz estilizada en Bootstrap

## Configuracion y Ejecución del Proyecto

### Prerequisitos

- python 3.9
- django 5.1
- django Crispy forms(opcional para formularios en bootstrap)

### Pasos para la instalacion

1. **Clona el repositorio:**

Clonar el repositorio en una maquina local.

$ mkdir PROYECTO_WEB
$ git clone git@github:sebastianVP/restaurante_magic.git
$ cd restaurante_magic
$ git status
$ cd ..

2. **Crear un Entorno Virtual**

Crea y activa un entorno virtual.
$ python -m venv restaurante
$ cd restaurante 
$ source bin/activate
$ cd ..
$ cd resturante_magic

3. **Instalar las Dependencias**

$ pip install django==5.1
$ pip install django-crispy-forms
$ pip install 


# DESARROLLO

Paso 1: Configuracion del Proyecto Django


