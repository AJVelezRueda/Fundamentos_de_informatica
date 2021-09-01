# *Introducción al Command Line Interface*

# Guias de Trabajo
* [1. Interfaces de Línea de Comandos](#1-cli)
* [2. Invocacion de comandos](#2-ivocaciones)
* [3. Argumentos](#3-argumentos)



## [1. Interfaces de Línea de Comandos](#1-cli)

Las **Interfaces de Línea de Comandos** (CLI) son un medio para exponer de manera sencilla el código que desarrollamos, para que pueda ser usado por otras personas y/o programas.  Los **intérpretes** (BASH, CASH, etc.) permiten la recepción de los comandos ingresados desde desde un repl y los evía al sistema operativo para su evaluación.

Un CLI tiene que ser capaz de recibir argumentos de tipo string, interpretarlos y, en caso de ser necesario, dialogar con el sistema operativo. Después de escribir un comando, el resultado que se obtiene  es información de texto o una acción específica realizada por la computadora. Por ello, la clave es escribir el comando correcto, un punto que suele considerarse como una desventaja en este diseño de interfaz de usuario por linea de comando y por lo que se suelen utilizar formas más atractivas de interfaz como GUI (Graphical User Interaction) para usuarios finales.

Los comandos básicos que vienen con el sistema operativo en general se puede dividir en dos categorías: los que manejan los procesos y los que manejan los archivos. 

## [2. Invocacion de comandos](#2-ivocaciones)

La invocación de un comando consiste en la palabra (comando) en sí y los argumentos y opciones, y determinan el nombre del ejecutable que se va a usar. Podemos decir en general que los comandos siguen la siguiente estructura:

```bash
$ comando [argumentos] 
```

La invocación de los comandos puede ser modificada en su comportamiento por defecto mediante los argumentos. 


## [3. Argumentos](#3-argumentos)

Es muy común encontrar en las CLI dos tipos de argumentos: 

- posicionales, que por extensión se los suele denominar argumentos a secas

- los nombrados, que se los conocen como flags u opciones. 

Veamos el ejemplo de `ls`, un comando disponible en casi todos los sistemas _UNIX_. Este comando sirve para listar archivos del directorio actual:

<pre><font color="#4E9A06"><b>ana@ana-X541UAK</b></font>:<font color="#3465A4"><b>/</b></font>$ ls
<font color="#06989A"><b>bin</b></font>    <font color="#3465A4"><b>dev</b></font>   <font color="#06989A"><b>lib</b></font>    <font color="#06989A"><b>libx32</b></font>      <font color="#3465A4"><b>mnt</b></font>   <font color="#3465A4"><b>root</b></font>  <font color="#3465A4"><b>snap</b></font>      <font color="#3465A4"><b>sys</b></font>  <font color="#3465A4"><b>var</b></font>
<font color="#3465A4"><b>boot</b></font>   <font color="#3465A4"><b>etc</b></font>   <font color="#06989A"><b>lib32</b></font>  <font color="#3465A4"><b>lost+found</b></font>  <font color="#3465A4"><b>opt</b></font>   <font color="#3465A4"><b>run</b></font>   <font color="#3465A4"><b>srv</b></font>       <span style="background-color:#4E9A06"><font color="#2E3436">tmp</font></span>
<font color="#3465A4"><b>cdrom</b></font>  <font color="#3465A4"><b>home</b></font>  <font color="#06989A"><b>lib64</b></font>  <font color="#3465A4"><b>media</b></font>       <font color="#3465A4"><b>proc</b></font>  <font color="#06989A"><b>sbin</b></font>  swapfile  <font color="#3465A4"><b>usr</b></font>
</pre>


Vamos qué sucede cuando hacemos `ls /usr`:
<pre><font color="#4E9A06"><b>ana@ana-X541UAK</b></font>:<font color="#3465A4"><b>/</b></font>$ ls /usr
<font color="#3465A4"><b>bin</b></font>    <font color="#3465A4"><b>include</b></font>  <font color="#3465A4"><b>lib32</b></font>  <font color="#3465A4"><b>libexec</b></font>  <font color="#3465A4"><b>local</b></font>  <font color="#3465A4"><b>share</b></font>
<font color="#3465A4"><b>games</b></font>  <font color="#3465A4"><b>lib</b></font>      <font color="#3465A4"><b>lib64</b></font>  <font color="#3465A4"><b>libx32</b></font>   <font color="#3465A4"><b>sbin</b></font>   <font color="#3465A4"><b>src</b></font>
</pre>



Como vemos en este caso, mediante el uso del argumento `/usr` podemos especificar el directorio cuyos archivos vamos a listar. Pero podemos controlar la salida de esta invocación, adicionando la opción la opción `-l` obtenemos el listado de archivos dentro del directorio usr:

<pre><font color="#4E9A06"><b>ana@ana-X541UAK</b></font>:<font color="#3465A4"><b>/</b></font>$ ls -l /usr
total 128
drwxr-xr-x   2 root root 57344 ago 31 08:03 <font color="#3465A4"><b>bin</b></font>
drwxr-xr-x   2 root root  4096 jul 31  2020 <font color="#3465A4"><b>games</b></font>
drwxr-xr-x  45 root root  4096 jul 10 20:47 <font color="#3465A4"><b>include</b></font>
drwxr-xr-x 124 root root  4096 jul 25 18:19 <font color="#3465A4"><b>lib</b></font>
drwxr-xr-x   2 root root  4096 jul 31  2020 <font color="#3465A4"><b>lib32</b></font>
drwxr-xr-x   2 root root  4096 feb 23  2021 <font color="#3465A4"><b>lib64</b></font>
drwxr-xr-x  12 root root  4096 feb 23  2021 <font color="#3465A4"><b>libexec</b></font>
drwxr-xr-x   2 root root  4096 jul 31  2020 <font color="#3465A4"><b>libx32</b></font>
drwxr-xr-x  10 root root  4096 jul 31  2020 <font color="#3465A4"><b>local</b></font>
drwxr-xr-x   2 root root 20480 jul 25 18:19 <font color="#3465A4"><b>sbin</b></font>
drwxr-xr-x 272 root root 12288 jul 10 21:27 <font color="#3465A4"><b>share</b></font>
drwxr-xr-x   6 root root  4096 ago 24 18:51 <font color="#3465A4"><b>src</b></font>
</pre>