# Rutas, absolutas y relativas

🚨 Este material fue creado por Guillermo I. Benítez y como todo el repositorio se encuentra bajo licencia 
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


[Rutas, absolutas y relativas](os)

Como ya hemos visto, para acceder a los archivos necesitamos saber cuál es la ruta (o path) dónde se encuentran. En este punto surge el inconveniente de los distintos sistemas operativos, ya que hay una diferencia en cómo se arman estas rutas. Para solucionar esto se puede utilizar las bibliotecas **os** y **pathlib** las cuales ya vienen incorporadas en python (built-in modules), de manera de poder armar las rutas necesarias y poder usarlas independientemente del sistema operativo. Veamos como funcionan.
Supongamos que un grupo de alumnos trabajan con los sitemas operativos macOS y Windows y uno de ellos tiene un archivo en la carpeta _/home/usuario/Documentos/UCEMA/Fundamentos/Práctica4/archivo.txt_, a la hora de acceder al archivo podemos enfocarlo de manera de acceder al archivo con la ruta absoluta (completa) o la ruta relativa. Con la primera usamos la ruta desde la carpeta base o raíz hasta el archivo en cuestión, y con la segunda tenemos en cuenta dónde estamos parados y aclaramos la ruta desde allí. En este caso la ruta absoluta es la que está mostrada más arriba y si, por ejemplo, estamos en la carpeta _/home/usuario_ la ruta relativa que deberíamos usar es: _./Documentos/UCEMA/Fundamentos/Práctica4/archivo.txt_ (recuerden que si usamos un punto, _._, estamos diciendo "a partir de esta carpeta"). Ahora bien ¿cómo armamos estas rutas para que se puedan usar en cualquier sistema operativo? (para esto consideramos que todos los alumnos lo tienen guardado en la misma carpeta, es decir, dentro de la carpeta Documentos hay una carpeta UCEMA, etc., sin importar el sistema operativo). Por un lado, si vamos a usar la ruta absoluta, hay que saber cómo se escribe en ese sistema la carpeta del usuario (home), por lo que vamos a usar la biblioteca **pathlib** de la siguiente manera:

```python
>>> from pathlib import Path
>>> home = str(Path.home())
```

Con esto obtenemos cual es la ruta del home para cualquier sistema. Luego hay que completar la ruta con las carpetas que ya conocemos, por lo que para esto vamos a usar **os.path.join()**, el cual genera la ruta con la manera de escritura del sistema operativo, por ejemplo:

```python
>>> ruta_relativa = os.path.join("Documentos", "UCEMA", "Fundamentos", "Práctica4", "archivo.txt")
>>> print(ruta_relativa)
# Para macOS y Linux
'Documentos/UCEMA/Fundamentos/Práctica4/archivo.txt'
# Para Windows
'Documentos\\UCEMA\\Fundamentos\\Práctica4\\archivo.txt'
>>> ruta_absoluta = os.path.join(home, "Documentos", "UCEMA", "Fundamentos", "Práctica4", "archivo.txt")
# Para macOS y Linux
'/home/usuario/Documentos/UCEMA/Fundamentos/Práctica4/archivo.txt'
# Para Windows
'C:\\Users\\Usuario\\Documentos\\UCEMA\\Fundamentos\\Práctica4\\archivo.txt'
```

Las dos barras invertidas en las rutas de Windows se dan porque una barra invertida en general es una secuencia de escape (como **"\n"**) pero aquí es parte de la ruta, por lo que se le agrega otra barra invertida para que python lo entienda (la otra manera es usar el metacaracter **r** antes de un string de manera de escribir solo una barra: ```r"C:\ruta\al\archivo"```).
Como verán esto no genera carpetas o archivos en la computadora, por lo que puede llegar a pasar que la ruta que hayamos armado no exista (o la hayamos escrito mal), en tales casos lo mejor es verificar si la ruta existe:

```python
>>> ruta_relativa = os.path.join("Documentos", "UCEMA", "Fundamentos", "Práctica4", "archivo.txt")
>>> os.path.exists(ruta_relativa) #Cuyo resultado es un booleano
```

Por cuestiones de comodidad muchas veces es recomendable trabajar con rutas relativas ya que de esta manera solo son movemos dentro de las carpetas correspondientes y no hay peligro de poder acceder a otra carpeta y modificar cosas que no deberíamos, siendo, tal vez, el mayor "inconveniente" saber en qué carpeta estamos parados, para saber para dónde hay que moverse.

De esta manera, realizando estos pasos, el mismo código va a funcionar independientemente del sistema operativo dónde se ejecute.

[os.listdir y glob](glob)

Algo que resulta muy útil es poder acceder a los archivos que hayan en una determinada carpeta sin conocer sus nombres en particular, o acceder a un grupo de estos archivos que tengan algo en común (que todos tengan la misma extensión por ejemplo), más aún si son archivos que el programa genera en su ejecución, de manera de que a priori no los tenemos. Para esto podemos usar dos herramientas, el método ```listdir``` de la biblioteca ```os``` y el método ```glob``` de la biblioteca ```glob```. Con el primero obtenemos una lista de todos los archivos que se encuentran en una carpeta, mientras que con el segundo, además de esto, tenemos la posibilidad de listar archivos específicos. Es decir:

```python
>>> import os
>>> import glob
>>> os.listdir()
['Ej1.py', 'Ej3.py', 'archivo2.txt', 'Ej2.py', 'Ej4.py', 'documento.txt', 'Ej5.py'...]
>>> glob.glob("*")
['Ej1.py', 'Ej3.py', 'archivo2.txt', 'Ej2.py', 'Ej4.py', 'documento.txt', 'Ej5.py'...]
>>> glob.glob("*.py")
['Ej1.py', 'Ej3.py', 'Ej2.py', 'Ej4.py', 'Ej5.py'...]
```

Como ven, podemos obtener una lista, la cual podríamos recorrer tanto para todos los archivos de una carpeta como para los archivos específicos.