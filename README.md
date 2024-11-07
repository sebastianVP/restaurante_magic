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
