# *Manejo de Excepciones con Python*

# Guias de Trabajo
* [1. La excepción hace a la regla](#1-intro)
* [2. Errores de Sintaxis](#2-sintax_error)


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
> 🧗‍♀️Desafio I: Descargá y ejecutá el [`script1_manejo_errores.py`]()
>
> Para pensar 🤔: ¿Qué tipo de error se obtiene al ejecutar el programa? ¿En dónde se encuentra el error? ¿Cómo te das cuenta? 
>

 
