# *Lectura & Escritura de archivos con Python*

# Guias de Trabajo
* [1. Archivos](#1-archs)
* [2. Lectura de archivos](#2-open)
* [3. Rutas absolutas y relativas](#3-paths)

[1. Archivos](#1-archs)


Python tiene la capacidad de acceder y realizar operaciones de lectura/escritura sobre los documentos localizados en un sistema de archivos

Los sistemas _UNIX_, _MacOS_ X y _GNU/Linux_ se basan en la premisa de que todo es un archivo o un directorio, por lo que es común acceder a flujos de datos del dispositivos y/o procesos como si se accediera a un archivo binario. En los sistemas operativos de Windows sin embargo esta premisa no se cumple.

LPara Python existen dos tipos de archivos: de texto o binarios. Estos se manipulan de modos distintos. Los **archivos de texto** están formados por una secuencia de líneas, donde cada línea incluye una secuencia de carácteres. Típicamente, cada línea finaliza con el carácter especial de _fin de linea_ (EOL). Si bien existen distintos tipos de carácteres de fin de línea, el más común es ([\n](https://github.com/AJVelezRueda/UCEMA_Fundamentos_de_informatica/blob/master/Python_intro/Expresiones_regulares.md)).

Un **archivo binario** es cualquier tipo de archivo que no es un archivo de texto. Estos solo pueden ser interpretados o leídos por aplicaciones.


[2. Lectura de archivos](#2-open)

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
|  r+	| abre un archivo para lectura y escritura|
|  a	| Abre un archivo para agregar información. Si el archivo no existe, crea un nuevo archivo para escritura|	
|  w	| Abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura|	

* [3. Rutas absolutas y relativas](#3-paths)


En todos los sistemas operativos modernos la estructura de archivos es jerárquica y depende de los directorios. Semejante a una estructua arbórea en la que existe un nodo (un directorio o carpeta), que contiene los restantes directorios o archivos.

El path o ruta a un archivo, será entonces, el recorrido de directorios o carpetas que debemos recorrer para llegar a nuestro archivo. Esta se escribe separando los nombres de los respectivos directorios separados por `/`. Esto es lo que se conoce como la ruta absoluta al archivo:


```bash
windows  "C:\home\Facultad\Fundamentos\Manipulación_de_archivos.md"
Linux  "/home/Facultad/Fundamentos/Manipulación_de_archivos.md"
```

Las rutas tambien pueden ser escritas de un modo más compacto o acortado. Se suelen escribir de forma relativa a un determinado directorio. Veamos un ejemplo:


```
/
└── home/  ← carpeta de referencia
    │
    ├── Facultad/ ← Direcotiorio de trabajo
    |   └── Estadística 
    │   └── Fundamentos/  
    │       └── Manipulación_de_archivos.md
    └── Fotos  ← Otro directorio
```

Imaginemos que esta es la estructura de archivos de nuestra computadora, donde existen dos carpetas en el home: _Fotos_ y _Facultad_. Dentro de la carpeta _Facultad_, podemos encontrar a su vez dos directorios: _Fundamentos_ y _Estadistica_. Nuestra carpeta de trabajo actual es la de Fundamentos, donde tenemos nuestro archivo de interes _Manipulación_de_archivos.md_. 

Desde el directorio _Facultad_ podemos escribir la ruta relativa a nuestro archivo del siguiente modo:

```bash
"ls ./Fundamentos/Manipulación_de_archivos.md"
"ls /Fundamentos/Manipulación_de_archivos.md"
```
Ahora si quisieramos acceder a las _Fotos_, podemos hacer:

```bash
"ls ../Fotos"
```

