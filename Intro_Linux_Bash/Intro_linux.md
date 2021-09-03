# *Introducción a Linux y Bash*

# Guías de Trabajo

* [Linux](#linux)

Como ustedes ya sabrán, Linux es un sistema operativo de código abierto con licencia GNU GPL (General Public License), la cual nos permite poder tomar el código, modificarlo y distribuirlo libremente. Gracias a esta característica se generaron muchas distribuciones, entre las cuales las más recomendadas para iniciar en el mundo de Linux son **Ubuntu** o **Linux Mint**. En este curso recomendamos fuertemente utilizar alguna de estas dos distribuciones, ya que con otro sistema operativo no vamos a poder darles soporte.

Una de las características principales de Linux es la organización jerárquica de las carpetas del sistema, la cual se puede pensar como un árbol, siendo la raíz la base del sistema y a partir de allí las carpetas se ramifican.
![alt text](https://www.linuxadictos.com/wp-content/uploads/linux-arbol-directorios.jpg)

La otra característica que distigue a Linux es la existencia de dos tipos de usuarios, que podríamos dividir en simplemente usuarios y administradores (o usuario root o superusuario). Estos usarios se generan automáticamente cuando configuramos nuestra cuenta y los podemos usar dependiendo de nuestra necesidad. Para la mayoría de las cosas solo vamos a necesitar permisos de usuario, pero para ciertas tareas vamos a necesitar los permisos de superusuario. Dicho esto, recomendamos fuertemente que solo para las tareas específicas se utilice el superusuario, para todo lo demás hay que usar el usuario común.  

* [Interfaz de línea de comandos(CLI)](#CLI")

	* [1. Caparazón](#1_shell)
	* [2. Comandos básicos](#2_comandos)


### [1. Caparazón](#1_shell)

El shell es la capa más externa del sistema operativo, esta es la interfaz entre el usuario y el sistema operativo. Los shells incorporan un lenguaje de programación para controlar procesos y archivos, además de iniciar y controlar otros programas. El shell gestiona la interacción entre el usuario y el sistema operativo solicitándole la entrada, interpretando dicha entrada para el sistema operativo y gestionando cualquier resultado de salida procedente del sistema operativo. La shell es un programa que ejecutamos en la forma de un repl(read printable loop), este interpreta los comandos que ingresa el usuario y posteriormente transmitirlos al sistema y arrojar el resultado. 

Podemos decir en general que los comandos que:
- siguen la siguiente estructura:

```bash
$ comando [opciones] [argumentos]
```

- consisten en la palabra (comando) en sí y opcionalmente las opciones y/o argumentos

- determinan el código o librería que se va a usar

- pueden ser modificados en su comportamiento por defecto mediante opciones o argumentos: si bien el comando contiene la instrucción que queremos realizar, el argumento indica dónde debe operar el comando y la opción solicita la modificación de la salida.

Existen argumentos que se le pasan al comando que le permiten operar sobre un objeto/dato, etc., aunque pueden no existir.

Después de escribir un comando, el resultado que se obtiene es información de texto o una acción específica realizada por la computadora. Por ello, la clave es escribir el comando correcto, un punto que suele considerarse como una desventaja en este diseño de interfaz de usuario y por lo que se suelen utilizar formas más atractivas de interfaz como GUI (Graphical User Interaction).


### [2. Comandos básicos](#2_comandos)

Existen varios shells, la más común es bash (llamada "Bourne Again SHell"). Después de ejecutarse, el shell visualiza un indicador de mandatos o prompt, que en el caso del Bourne shell suele ser un $ (signo de dólar), momento en que el shell está preparado para recibir un comando. Si bien hay muchos comandos que podés usar con CLI, en general se dividen en dos categorías:

+ Los comandos que manejan los procesos
+ Los comandos que manejan los archivos

###  **Comandos que manejan archivos**

**_`ls`_**: 

Este comando lista todos los archivos en una carpeta y acepta como parámetro. El comando predeterminado excluirá los archivos ocultos. Para mostrar todos los archivos, puedes agregar `-a`.


```bash
$ ls -a
```

**_`cd`_**: 

Cambio de directorio 

```bash
$ cd directorio_al_que_quiero_ir
```


**_`mv`_**: 

Renombrar o mover un archivo los archivos y directorios en su sistema de archivos del sistema operativo. Es importante recordar que se debe escribir el nombre del archivo y la extensión. 

Si queremos por ejemplo deseamos renombrar un archivo:


```bash
$ mv recurso.extension recurso_renombrado.extension
```

Si deseamos cambiar la ruta de ese archivo a una nueva debemos ingresar el nombre del archivo seguida la ruta:


```bash
$ mv recurso.extension home/Directorio
```
