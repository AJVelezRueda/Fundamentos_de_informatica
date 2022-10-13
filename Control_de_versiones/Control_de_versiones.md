# *Control de Versiones*
En este recorrido repasaremos los conceptos básicos de de control de versiones utilizando [Git](https://git-scm.com/downloads) y [GitHub](https://github.com/). 

# Guias de Temas
* [1.Introdurción](#1-intro)


[1.Introdurción](#1-intro)

Los sistemas de control de versiones comienzan con una versión base del documento y luego registran los cambios que realiza en cada paso del camino. 

Se podría pensar como un video: puede retroceder para comenzar en el documento inicial y reproducir cada estado o cambio que realizó, llegando finalmente a su versión más reciente.

### Sistema de Control de Versiones

Un **sistema de control de versiones** es una herramienta que realiza un seguimiento de los cambios de un documento o directorio de forma automática, creando efectivamente diferentes versiones de nuestros archivos. 

Cada registro de estos cambios se denomina commit y mantiene metadatos útiles sobre ellos. 

El historial completo de commits para un proyecto en particular y sus metadatos forman un repositorio. 


### ¿Cómo funciona?

Siguiendo con la analogía del video, podemos pensar cada _commit_ como un fotograma en nuestro video, siendo este el historial completo de cambios de un archivo o directorio. 

Cada _commit_ funciona como un “paquete” de cambios realizados, que se pueden ir agregando al stage (estado intermedio con cambios) mediante el comando git add. 

Estos cambios se gestionan como una unidad, al generar un _commit_, y quedan registrados en una “foto” al hacer git _commit_.

Es muy importante especificar los cambios realizados en cada _commit_, esto nos ayudará a rastrear cualquier cambio al querer volver atrás.

