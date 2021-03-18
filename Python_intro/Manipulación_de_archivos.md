# *Lectura & Escritura de archivos co Python*

# Guias de Trabajo
* [1. Lectura de archivos](#1-open)

[1. Lectura de archivos](#1-open)

Python tiene la capacidad de acceder y realizar operaciones de lectura/escritura sobre los documentos localizados en un sistema de archivos

Los sistemas _UNIX_, _MacOS_ X y _GNU/Linux_ se basan en la premisa de que todo es un archivo o un directorio, por lo que es común acceder a flujos de datos del dispositivos y/o procesos como si se accediera a un archivo binario. En los sistemas operativos de Windows sin embargo esta premisa no se cumple.

LPara Python existen dos tipos de archivos: de texto o binarios. Estos se manipulan de modos distintos. Los **archivos de texto** están formados por una secuencia de líneas, donde cada línea incluye una secuencia de carácteres. Típicamente, cada línea finaliza con el carácter especial de _fin de linea_ (EOL). Si bien existen distintos tipos de carácteres de fin de línea, el más común es ([\n](https://github.com/AJVelezRueda/UCEMA_Fundamentos_de_informatica/blob/master/Python_intro/Expresiones_regulares.md)).

Un **archivo binario** es cualquier tipo de archivo que no es un archivo de texto. Estos solo pueden ser interpretados o leídos por aplicaciones.


Para abrir un archivo de texto, ya sea para usarlo o escribir en el, podemos usar la función nativa de Python `open()`:

```python
open(path_al_archivo, modo) 
```

Donde:

    - "path_al_archivo" es un objeto de tipo str que indica la ruta en la que se encuentra el archivo.
    
    - "modo" es un objeto de tipo str que indica la forma en la que Python accederá al archivo en cuestión.



| Modo de apertura| Significado | 
|-------------	|----------	|
|  r	| abre un archivo solo para lectura|
|  a	| Abre un archivo para agregar información. Si el archivo no existe, crea un nuevo archivo para escritura|	
|  w	| Abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura|	