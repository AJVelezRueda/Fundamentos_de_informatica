# *Python avanzado*
En este recorrido aprenderemos los conceptos básicos de expresiones regulares en [Python](https://www.python.org.ar/). Para ello vas a necesitar instalarte el módulo [RE](https://pypi.org/project/regex/).


# Guias de Trabajo
* [1. Lo esencial es invisible a los ojos](#1-Escape-characters)
* [2. ¿Qué son las expresiones regulares?](#2-ER)
* [3. Metacaracteres y expresiones Simples](#3-Metacaracteres)
* [4. Coincidencias o Matches](#4-matches)

[1. Lo esencial es invisible a los ojos](#1-Escape-characters)

Cuando trabajamos con archivos de texto, suele pasar desapercibida la presencia de caracteres que dan formato legible al texto y que no se representan por así decirlo "graficamente explicitos". Un ejemplo de ello es el espacio entre las palabras que tipeamos para constuir una oración. Este tipo de caracteres, comunmente conocidos como caracteres especiales, se encuentran respresentados por _secuencias de escape_. 

Las _secuencias de escape_ son una combinación de caracteres que tiene un significado distinto de los caracteres literales contenidos en ella y se utilizan para definir ciertos caracteres especiales dentro de cadenas de texto, tipicamente aquellos que dan formato al mismo. Y aún cuando son un conjunto de caracteres, una secuencia de escape se considerada un carácter único.

Estas combinaciones constan tipicamente de una barra invertida (`\`) seguida de una letra o de una combinación de dígitos, que tendrá un significado distinto según cuales sean. Por ejemplo, para representar un carácter de _salto de línea_ se utiliza la secuencia de espace `\n`.

Vamos a ver algunas de las secuencias de escape más frecuentes:

| Secuencia de escape| representación | 
|-------------	|----------	|
| \n | salto de línea | 
| \t | Tab o cambio de pestaña |
| \s | espacio |
| \' | Comillas simples |
| \" | Comillas dobles |   



[2. ¿Qué son las expresiones regulares?](#2-ER)

Las expresiones regulares son cadenas de caracteres basadas en reglas sintácticas, que permiten describir secuencias de caracteres. Es decir es un criterio para buscar, capturar o reemplazar texto utilizando patrones. Estas son una herramienta poderosa a la hora de hacer búsquedas sofisticadas en Strings de forma simple.


Las expresiones regulares se pueden concatenar para formar nuevas expresiones regulares; si, por ejemplo, A y B son expresiones regulares, AB también es una expresión regular.


> Para pensar 🤔: ¿Qué usos crees que podemos darle a las expresiones regulares? Proponé una aplicación concreta para tu carrera/disciplina.
>

[3. Metacaracteres](#3-Metacaracteres)

Los `metacaracteres` son caracteres especiales que, dependiendo del contexto, tienen un significado especial para las expresiones regulares. 

Existen lo que se conoce como `metacaracteres delimitadores`, que nos permitirán delimitar dónde queremos buscar los patrones de búsqueda. Entre ellos tenemos:


| Metacaracter| Significado | 
|-------------	|----------	|
| ^	| Inicio de línea | 
| $ | Fin de linea |
| \A | Inicio de texto |
| \Z | Fin de texto |
| . | Coincide con cualquier caracter en una línea dada | 


Ya vimos que en programación suele ser útil repetir la ejecución de porciones de código. Las expresiones regulares nos permiten no solo delimitar la porción de texto donde deseamos buscar, sino que también permite repitir cierta cantidad de veces una busqueda dada. Para ello se utilizan los `metacaracteres cuantificadores`:


| Metacaracter| Significado | 
|-------------	|----------	|
|  *	| Cero o más: todas las ocurrencias de un dado substring |	
|  +	| Una o más ocurrencias del patrón|	
|? | Cero o una|
|{n} | Exactamente n veces|
|{n,m} | Por lo menos n pero no más de m veces.|


>
> Para pensar 🤔: ¿Qué significará la expresión regular `"X(.*)Y"`? Ennumera algunas de las posibles strings que cumplen con dicha condición.
>
>
> 🧗‍♀️ Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?
>
> 🧗‍♀️ Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?
>
> 🧗‍♀️ Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón `ab` en un string?
>

<details>
  <summary>Respuestas</summary>

```bash
Desafio I: \d{4,}

Desafio II: [a-z]{3,6}

Desafio III: ab*

```
</details>

> Para pensar 🤔: ¿Existe una única respuesta para los ejercicios? ¿Qué otras alternativas se te ocurren?

Los dígitos entre llaves de la forma {n,m}, especifican el mínimo número de ocurrencias en n y el máximo en m.

Existen tambien metacaracteres predefinidos, que nos facilitan el uso de las expresiones regulares:

| Metacaracter| Significado | 
|-------------	|----------	|
|  \w	| Caracter alfanumércio|
|  \W	| Caracter NO alfanumércio|	
|  \d	| Caracter numércio|	
|  \D	| Caracter NO numércio|	
|  \s	| Un espacio, de cualquier tipo (\t\n\r\f)|	
|  \S	| Cualquier caracter que no sea un espacio|	


Como ya hemos visto, estos metacaracteres puden combinarse para lograr expresiones regulares complejas. 

>
> 🧗‍♀️Desafio IV: ¿Qué expresión regular usarías para extraer el número de estudiantes que hay en una clase según el siguiente texto:
>
```python
texto = 'En la clase de Introducción a la programación hay 30 estudiantes' 
```
>

<details>
  <summary>Respuestas</summary>

```bash
Desafío IV: /d+
```
</details>

*Rangos*

Un rango es una clase de caracteres abreviada que se crea escribiendo el primer caracter del rango, un guión y el último caracter del rango. Sirve para listar un conjunto de caracteres de interés. Por ejemplo:

    - El rango [a-d] equivale al [abcd]
    - El rango [1-10] equivale al substring [12345678910]

Así como podemos listar los caracteres posibles en cierta posición de la cadena, también podemos listar caracteres que no deben aparecer utilizando el `^`. Así, por ejemplo rango [^a-d] coincide con cualquier caracter que no sea `abcd`.


[4. Coincidencias o Matches](#4-matches)


Comenzaremos por aprender sobre las expresiones regulares más simples posibles. Dado que las expresiones regulares se utilizan para operar en strings, vamos a empezas con la tarea más común: los caracteres coincidentes. 

Si un String se corresponde con el criterio que define una expresión regular, se dice que el String hace match con la expresión, y equivalentemente, se dice que la expresión acepta al String.