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
