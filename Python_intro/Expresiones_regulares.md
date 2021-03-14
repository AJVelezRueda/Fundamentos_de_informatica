# *Python avanzado*
En este recorrido aprenderemos los conceptos básicos de expresiones regulares en [Python](https://www.python.org.ar/). Para ello vas a necesitar instalarte el módulo [RE](https://pypi.org/project/regex/).


# Guias de Trabajo
* [1. Lo esencial es invisible a los ojos](#1-Escape-characters)
* [2. ¿Qué son las expresiones regulares?](#2-ER)

[1. Lo esencial es invisible a los ojos](#1-Escape-characters)

Cuando trabajamos con archivos de texto, suele pasar desapercibida la presencia de caracteres que dan formato legible al texto y que no se representan por así decirlo "graficamente explicitos". Un ejemplo de ello es el espacio entre las palabras que tipeamos para constuir una oración. Este tipo de caracteres, comunmente conocidos como caracteres especiales, se encuentran respresentados por _secuencias de escape_. 

Las _secuencias de escape_ son una combinación de caracteres que tiene un significado distinto de los caracteres literales contenidos en ella y se utilizan para definir ciertos caracteres especiales dentro de cadenas de texto, tipicamente aquellos que dan formato al mismo. Y aún cuando son un conjuntod e caracteres, una secuencia de escape se considerada un carácter único.

Estas combinaciones constan tipicamente de una barra invertida (`\`) seguida de una letra o de una combinación de dígitos, que tendrá un significado distinto según cuales sean. Por ejemplo, para representar un carácter de _salto de línea_ se utiliza la secuencia de espace `\n`.

Vamos a ver algunas de las secuencias de escape más frecuentes:


| Secuencia de escape| represntación | 
|-------------	|----------	|
| \n | salto de línea | 
| \t | Tab o cambio de pestaña |
| \s | espacio |
| \' | Comillas simples |
| \" | Comillas dobles |   


[2. ¿Qué son las expresiones regulares?](#2-ER)
Las expresiones regulares son cadenas de caracteres basadas en reglas sintácticas, que permiten describir secuencias de caracteres. Es decir es un criterio para buscar, capturar o reemplazar texto utilizando patrones. Estas son una herramienta poderosa a la hora de hacer búsquedas sofisticadas en Strings de forma simple.


