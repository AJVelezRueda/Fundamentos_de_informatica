# *Introducción a Linux y Bash*

* [Comandos](#comandos)

Como ya dijimos los comandos que vamos a ver mayormente son los comandos que manejan archivos. Como vimos, la estructura de los comandos es:

```bash
$ comando [opciones] [argumentos]
```

Pero, ¿cómo sabemos cuales son las opciones de un comando? O más aún, ¿cómo sabemos qué es lo que hace un comando dado?
Para estos casos Linux nos ofrece dos maneras de poder obtener estas respuestas. Una de estas opciones es usar otro comando, llamado `man` el cual muestra, justamente, el manual del comando en cuestión:

```bash
man ls
```

La otra opción para contestar estas preguntas es la opción `--help`

```bash
ls --help
```

Veamos rápidamente algunos comandos básicos muy útiles, con algunas opciones según corresponde.

- Algunas opciones útiles del comando `ls` son:

	- `-l` para ver los archivos en forma de listas, con algunos detalles más, alguno de los cuales son los permisos que tiene el archivo o carpeta, a quien pertenece, el peso, la fecha de modificación, etc.
	- `-a` para ver todos los archivos, inluso los ocultos
	- `-d` solo para listar los directorios
	- `-h` para ver el resultado "legible" para el humano. Esta opción solo se puede usar si se utiliza la opción `-l`. De esta forma vamos a poder ver el peso en Bytes, Kilobytes, etc.

- 

