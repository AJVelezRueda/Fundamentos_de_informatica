# *Manejo de Excepciones con Python*

# Guias de Trabajo
* [1. La excepción hace a la regla](#1-intro)
* [2. Errores de Sintaxis](#2-sintax_error)
* [3. Excepciones](#3-exceptions)
* [4. Con intentar no se pierde nada](#4-try)


[1. La excepción hace a la regla](#1-intro)
Si estuviste haciendo bien las cosas hasta aquí, te habrás equivocado ¡y mucho! En todo proceso de aprendizaje los ‘errores’ tienen un rol muy importante: nos plantean nuevos interrogantes, nos acercan a nuevas hipótesis y sobre todo nos dan oportunidades para seguir aprendiendo. 
En la programación los ‘errores’ también importan, ¡y mucho! Son una suerte de comunicación con la máquina, que nos advierte cuando no funciona algo de lo que intentamos hacer.
Existen (al menos) dos tipos diferentes de errores en Python: errores de sintaxis y excepciones. Con cada tipo de error la máquina nos indica qué es lo que puede estar fallando de nuestro código. 
No tengas miedo de equivocarte, ¡no se rompe nada! Y como diría la señorita Ricitos del Autobús Mágico: _a cometer errores, tomar oportunidades y rockear con Python, que donde termina la carretera comienza la aventura!_

[2. Errores de Sintaxis](#2-sintax_error)
Cuando existen errores en el código se detiene la ejecución del programa que hemos creado. Uno de los tipos de errores mas frecuente al iniciarnos en la programación con Python son los errores de sintaxis, o también conocidos como errores de interpretación. ¿A ver si te suena?

```Python
>>> print(Hola mundo')
  File "<stdin>", line 1
    print(Hola mundo')
               ^
SyntaxError: invalid syntax
```

Si observamos el error este tiene en su mensaje información que nos permitirá encontar el origen del problema.

>
> 🧗‍♀️Desafio I: Descargá y ejecutá el [`script1_manejo_errores.py`](https://github.com/AJVelezRueda/UCEMA_Fundamentos_de_informatica/blob/master/Python_intro/script1_manejo_errores.py)
>
> Para pensar 🤔: ¿Qué tipo de error se obtiene al ejecutar el programa? ¿En dónde se encuentra el error? ¿Cómo te das cuenta? 
>

Como has visto el intérprete de Python imprime la línea responsable del error y muestra una flecha el lugar donde se detectó el error. El error ha sido provocado (o al menos detectado) en el elemento que precede a la flecha. En nuestro ejemplo, el error fué detectado al ejecutar la función print(), ya que faltan las comillas que abre el string.


[3. Excepciones](#3-exceptions)

Sin embargo, aún cuando nuestro código sea sintácticamente correcto, puede generar errores de ejecuciones. Los errores detectados durante la ejecución se llaman excepciones.

Para el manejo de excepciones Python nos provee palabras reservadas, que nos permiten manejar las excepciones que puedan surgir y tomar acciones que evitan la interrupción del programa o permitan especificar información adicional antes de interrumpir el programa.

Existen distintos tipos de excepciones y generalmente el tipo de excepción se imprime como parte del mensaje, al surgir la excepción:

```Python
>>> 3 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

```

```Python
>>> print(divisor)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'divisor' is not defined
```
>
> Para pensar 🤔: ¿Qué nos dice el mensaje de excepción? ¿Qué es la excepción de nombre? 
>

```Python
>>> 0 + "2"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

```

>
> Para pensar 🤔: ¿Qué nos dice el último mensaje de excepción? ¿Qué es la excepción de tipo? 
>


[4. Con intentar no se pierde nada](#4-try)