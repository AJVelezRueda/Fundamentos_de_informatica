# *Introducción al Command Line Interface*

# Guias de Trabajo
* [1. Interfaces de Línea de Comandos](#1-cli)
* [1. La vida más fácil con Argparse](#2-Argparse)



### [1. Caparazón](#1_shell)

El shell es la capa más externa del sistema operativo, esta es la interfaz entre el usuario y el sistema operativo. Los shells incorporan un lenguaje de programación para controlar procesos y archivos, además de iniciar y controlar otros programas. El shell gestiona la interacción entre el usuario y el sistema operativo solicitándole la entrada, interpretando dicha entrada para el sistema operativo y gestionando cualquier resultado de salida procedente del sistema operativo. La shell es un programa que ejecutamos en la forma de un repl(read printable loop), este interpreta los comandos que ingresa el usuario y posteriormente transmitirlos al sistema y arrojar el resultado. 

Podemos decir en general que los comandos que:
- siguen la siguiente estructura:

```bash
$ comando [parámetros] [argumentos] [separador]
```

- consisten en la palabra (comando) en sí y el argumento u opción

- determinan el código o librería que se va a usar

- pueden ser modificados en su comportamiento por defecto mediante opciones o argumentos: si bien el comando contiene la instrucción que queremos realizar, el argumento indica dónde debe operar el comando y la opción solicita la modificación de la salida.

Existen argumentos se le pasan al comando que le permiten operar sobre un objeto/dato, etc., aunque pueden no existir.

Después de escribir un comando, el resultado que se obtiene  es información de texto o una acción específica realizada por la computadora. Por ello, la clave es escribir el comando correcto, un punto que suele considerarse como una desventaja en este diseño de interfaz de usuario y por lo que se suelen utilizar formas más atractivas de interfaz como GUI (Graphical User Interaction).


[2. Interfaces de Línea de Comandos](#1-cli)

Las **Interfaces de Línea de Comandos** (CLI) son un medio para exponer de manera sencilla el código que desarrollamos, para que pueda ser usado por otras personas y/o programas.  Los **intérpretes** (BASH, CASH, etc.) permiten la recepción de los comandos ingresados desde desde un repl y los evía al sistema operativo para su evaluación.

Un CLI tiene que ser capaz de recibir argumentos de tipo string, interpretarlos y di

Si bien hay muchos comandos que podés usar con CLI, en general se dividen en dos categorías:

+ Los comandos que manejan los procesos
+ Los comandos que manejan los archivos

