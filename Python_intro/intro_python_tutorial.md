# *Introducción a Python*

En este recorrido aprenderemos los conceptos básicos de programación y la sintáxis de [Python](https://www.python.org.ar/). Para ello vas a necesitar instalarte [Python](http://ufq.unq.edu.ar/sbg/archivos/guias_talleres/Guia_Instalacion_Python_2020.pdf) y algún [editor de código](https://code.visualstudio.com/)(IDE) que te sea útil para programar. 

¡Para este recorrido tomaremos como base las presentes guías del Proyecto de Extensión [La Bioinformática Va a La Escuela](http://ufq.unq.edu.ar/sbg/education.html) del cual soy creadora! 🤗


# Guias de Trabajo
  * [1. Pensamiento computacional](#1-PC)
  * [2. Anatomia de la Computadora](#2-computadora)
  * [3. Hablando como Pythonistas](#3-pythonistas)
  * [4. La caja negra](#4-terminal)
  * [5. Una calculadora super-archi-genial](#5-operadores)
  * [6. Apto Doris](#6-variables)
  * [7. Nada es mejor, nada es igual…](#7-operadores-relacionales)
  * [8. Una palabra no dice nada y al mismo tiempo dice todo](#8-strings)
  * [9.En fetas de texto](#9-slicing)
  * [10. Chamuyo: del lunfardo el arte de manipular palabras/cadenas](#10-metodos-strings)
  * [11. El todo y la nada](#11-in)
  * [12. Síndrome de Diógenes](#11-listas)

[1. Pensamiento computacional](#1-PC) 🧠

Si nunca programaste tal vez la programación pueda parecerte algo muy abstracto o lejano, hasta puede que te de miedo intentar aprender a programar, pero lo cierto es que las habilidades que utilizamos para programar son por demás cotidianas. ¿No me crees? ¡Vamos a hacer una prueba!

Pensemos en una actividad cotidiana como la de preparar mate 🧉 (#ArgentinianMood) ¡Una actividad muy programadoril!. Al realizar este ritual tan Argento, sin darte cuenta estás aplicando una serie de pasos lógico-prácticos simlares a los que se utilizan para programar: 
    - Primero, definir el problema que queres resolver. En nuestro caso: preparar mate 🧉 
    - Una vez definido el problema debemos plantear los pasos a seguir de una manera sencilla (no es sería recomendable intentar preparar mate patas para arriba). Empezamos buscando el mate y la yerba. Luego verificamos si el mate está vació o lleno, en el caso de estar vacío procedemos a llenarlo. Si está lleno, buscamos la primer maceta que tengamos a mano para vaciar su contenido y llenarlo con yerba.

Ahora que tenemos un idea de los pasos a seguir para resolver el problema, vamos a escribir nuestra guía para preparar un mate en 20 mil simples pasos (mentira solo son 8! 😝):
    
    Paso 1) Seleccionar el mate
    
    Paso 2) Buscar el yerbero
    
    Paso 3) Verificar si el mate está vacío:
    
        Momento decisivo:
    
            Paso 4) Si el mate está vacío, llenarlo con la yerba del yerbero.
    
            Paso 5) Si el mate está lleno:
    
                    Paso 7) Vaciarlo en una maceta
    
                    Paso 8) Llenarlo con la yerba del yerbero.

Hemos podido hacer un recorrido simplificado de la actividad, con las posibles situaciones a las que nos podemos enfrentar y sus soluciones posibles, para resolver el problema que nos habíamos propuesto: preparar mate 🧉

Veamos como se vería nuestra guía para preparar mate escrita en un lenguaje similar al que una computadora puede entender (pseudocódigo):
    
    mate = mate seleccionado
    yerbero = lata de yerba
    maceta = maceta con cactus del balcón 

    if mate está vacio:
        llenar mate con yerba del yerbero
    de lo contrario:
        vaciar mate en maceta
        llenar mate con yerba del yerbero

Moraleja, programar es como hacer mate...Bueno, no taaanto ¡pero casi! 😝

> 🧗‍♀️ Desafío I: ¿Qué pasos nos faltaron? ¿Podes pensar otras posibles situaciones que no estemos contemplando (como por ejemplo que no haya yerba en el yerbero)?  Agregá a la guía para preparar mate(script) los pasos, problemas posibles y las soluciones que se te ocurran en sentencias u ordenes sencillas (ejemplo; verificar si hay yerba en el yerbero. Si no hay agregar, si hay llenar el mate)  


[2. Anatomia de la Computadora](#1-computadora) 

Una computadora :computer: está formada por el _hardware_ (que son todas las partes o elementos físicos que la componen :keyboard::desktop::mouse_three_button:) y el _software_ (que son todas las instrucciones para el funcionamiento del Hardware). El _sistema operativo_ es el principal software de la computadora, pues proporciona una interfaz con el usuario y permite al resto de los programas una interacción correcta con el Hardware.

> Para pensar 🤔: ¿Y cómo te parece que funciona tu teléfono celular 📱? 

[3. Hablando como Pythonistas](#3-pythonistas)🐍

_¿Y cómo hacemos para decirle a la computadora qué hacer?_

Una computadora está constituida, básicamente, por un gran número de circuitos eléctricos que pueden estar prendidos o apagados. A los circuitos activados los representamos con un (`1`) y a los desactivados, con un (`0`).

Al establecer diferentes combinaciones de prendido y apagado de los circuitos, quienes usamos las computadoras podemos lograr que el equipo realice alguna acción (por ejemplo, que muestre algo en la pantalla 🖥️). ¡Esto es programar!

Los _lenguajes de programación_ actúan como traductores entre humanos y computadora 👩‍💻. En lugar de aprender el difícil lenguaje de la máquina, con sus combinaciones de _ceros_ y _unos_, se puede utilizar un lenguaje de programación para dar instrucciones al equipo de un modo que sea más fácil de aprender y entender. 

Para que la computadora entienda nuestras órdenes, un programa intermedio, denominado compilador, lee las instrucciones dadas por el usuario en un determinado lenguaje de programación y las convierte al lenguaje máquina de ceros y unos.

Esto significa que, como programadores de Python 🐍 (o cualquier otro lenguaje), no necesitamos entender lo que el equipo hace o cómo lo hace 🤔, basta con que entendamos a _hablar y escribir_ en el lenguaje de programación.

Python 🐍 es un lenguaje de programación con una forma de escritura (sintaxis) sencilla. Es lo que se conoce como lenguaje de scripting, que puede ser ejecutado por partes y no necesita ser compilado en un paso aparte (¿Compilado? 🤔 ¡Averiguá de qué se trata!). 
Python tiene muchas características, ventajas y usos que vamos a pasar por alto ahora, pero que iremos viendo a lo largo del curso.

[4. La caja negra](#4-terminal)

Ya vimos que para programar necesitamos tener un lenguaje en común con la computadora (lenguaje de programación). Dijimos también que en este curso usaremos como lenguaje _Python_, pero ¿Dónde debemos cargar nuestros mensajes (código)? ¡Hablar al aire parece no ser la solución!

Aquí es donde vamos a presentarte la Terminal o Consola. Esta pantalla negra es una interfaz gráfica que nos permite comunicarnos con la computadora. Esta interfaz nos permite ingresar ordenes a la computadora, através del teclado. 

Seguramente si abriste la terminal, habrás notado que hay un “chirimbolito” (símbolo) delante del código que ingresas, que se llama _prompt_. Algunas veces será un `>`, otras un `$`, según el lenguaje que entienda dicha terminal. 

👀 Ojo, cuando te mostremos ejemplos de código, si ves un _prompt_ no lo copies, porque forma parte de la consola  

> Tené en cuenta, que al salir de la consola se borrarán los comandos, a menos que los guardemos en un archivo o script para volver a ejecutarlos más adelante 

> 🧗‍♀️ Desafío II: Abrí la terminal de _Python_ que tengas instalada en tu computadora y luego abrí _Visual Code_ y luego presioná las teclas `Ctrl + J`. Se abrirá una terminal en el editor de código. ¿Cómo es el _prompt_ en cada caso? ¿Qué lenguaje "entiende" la terminal de _Visual Code_?

[5. Una calculadora super-archi-genial](#5-operadores)

Con Python podemos hacer todo tipo de cálculos matemáticos. Aunque suene medio embole, aprender a hacer estos cálculos nos va a ayudar después a trabajar sobre otros tipos de datos. 
Vamos a probar algunos cálculos. Para ello tenés que abrir la terminal de tu máquina y escribir _Python_, una vez que des enter y aparezca el _prompt_ podras comunicarte Pytonicamente con la computadora.

Escribí en tu terminal:
```Python
>>> 3*5
```
> Para pensar 🤔:¿Cuál es el resultado? ¿Qué significa entonces el `*`?

Probemos ahora:
```Python
>>> 8/4
```
> Para pensar 🤔:¿Cuál es el resultado? ¿Qué significa entonces el `/`?

Estos chirimbolos se conocen como operadores matemáticos y nos sirven para operar con distintos tipos de datos. ¡Un momento! ¿Cómo distintos tipos? ¿No sirven sólo para números? Dejamos el suspenso abierto...


<details>
  <summary>Tabla resumen operadores matemáticos</summary>

|Operación	|Operador | | | | | | | | | | | | |
|-------------	|----------	|---	|---	|---	|---	|---	|---	|---	|---	|---	|---	|---	|---	|
| Suma | + | | | | | | | | | | | | |
| División | / | | | | | | | | | | | | |
| Multiplicación | * | | | | | | | | | | | | |
| Exponencial | ** | | | | | | | | | | | | |

</details>

[6. Apto Doris](#6-variables) 🐠

Como habrán notado hasta aquí que venimos introduciendo órdenes línea a linea para que la computadora ejecute, lo que desde el púnto de vista práctico no resulta la mejor opción. Desde ya que sería ideal dejar la máquina haciendo cosas y poder irnos a por café. Por suerte existe una herramienta que va a simplificar nuestra tarea de ahora en adelante: las variables. Las variables nos permiten nombrar y reutilizar valores. 

Es decir, le damos un nombre a un conjunto de “cosas” o a una "cosa" y una vez declarada esa variable, Python recordará que contiene las cosas que le hayamos asignado. Las variables se utilizan en todos los lenguajes de programación. En Python, una variable se define con la sintaxis:

```python
>>> variable = valor de la variable
```

[7. Nada es mejor, nada es igual…](#7-operadores-relacionales) 🎶🎵

Existen también formas de comparar dos variables, lo que se conoce como operadores relacionales.
Podemos saber si dos variables son iguales (==), o si son distintas (!=), o si una es mayor que la otra (>). Por ejemplo:
```python
>>> dad_lola = 13
>>> edad_ana = 32
>>> edad_lola == edad_ana
```

> Para pensar 🤔:¿Cuál es el resultado? ¿Qué tipo de dato es?


Los operadores relacionales que se pueden usar en Python son:

<details>
  <summary>Tabla resumen operadores relacionales</summary>

|Operación	|Operador | | | | | | | | | | | | |
|-------------	|----------	|---	|---	|---	|---	|---	|---	|---	|---	|---	|---	|---	|---	|
| Igualdad | == | | | | | | | | | | | | |
| Distinto | != | | | | | | | | | | | | |
| Mayor | > | | | | | | | | | | | | |
| Menor | < | | | | | | | | | | | | |

</details>

[8. Una palabra no dice nada y al mismo tiempo dice todo](#8-strings) 🎶🎵

Estuvimos operando hasta aquí con números (_Int_) y recientemente aprendimos que existe otro tipo de datos lógicos (_boooleanos_), pero aún nos quedan muchos tipos de datos que podemos manipular en Python.

Como _lo que no se nombra, no existe_([Greorge Steiner](https://es.wikipedia.org/wiki/George_Steiner)), en programación y en la vida las palabras importan. En los lenguajes de programación se llama al texto ‘string’, ya que este tipo de datos no es más que una cadena de
caracteres, así como una palabra se puede entender como una cadena de letras. Un string no
necesariamente tiene que tener sentido. En Python las cadenas se definen escribiendo los caracteres entre comillas simples o dobles, indistintamente:

```python
>>> cadena = "este es un ejemplo de cadena"
>>> cadena
```

Las cadenas pueden ser comparadas con los operadores relacionales que vimos antes. Así, podemos
saber entonces si son o no son distintas: 

```python
>>> afirmacion = "si"
>>> gran_afirmacion = "SI"
>>> gran_afirmacion == afirmacion
```

> Para pensar 🤔:¿Qué resultado nos da? ¿Por qué?

[9.En fetas de texto](#9-slicing)

En Python podemos saber qué caracteres o subpartes conforman una cadena o string. Python le asigna
a cada caracter de una cadena un número de posición. 
El primer carácter es la posición cero (¡sí, cero!) y las posiciones aumentan de a una hasta el fin de la cadena. 

En la cadena `saludo = "hola"` , la 'h' tiene asignada la posición cero, la 'o' la posición uno, la 'l' la dos y la 'a' la tres. 


| H | O | L |A |
|-------------	|----------	|---	| ---|	
| 0 | 1 | 2 | 3 |


> Para pensar 🤔:¿Posición tendrá la letra "C' en el string `"Marie Curie"`? ¿Por qué?


Si quisiéramos saber cuál es el primer caracter de la cadena, hacemos referencia al caracter de la posición cero de la misma escribiendo el nombre de la variable seguida de la posición que nos interesa, escrita entre corchetes:

```python
>>> saludo = "Hola mundo"
>>> saludo[0]
```
Podríamos tomar solo un segmento de la cadena, indicando entre corchetes desde qué carácter hasta
qué carácter, separado por dos puntos:


```python
>>> saludo = "Hola mundo"
>>> saludo[0:3]
```

> Para pensar 🤔:¿Qué resultado nos dá el código anterior? ¿Por qué? ¿Qué pasa si removemos el último número (hacemos `saludo[0:]`)? 


[10. Chamuyo: del lunfardo el arte de manipular palabras/cadenas](#10-metodos-strings)

Existen muchas maneras útiles para manipular cadenas en Python.

> len(string) 
>
> string.upper()
>
> string.lower()
>
> string.count('caracter')


```python
>>> saludo = "Hola mundo"
>>> len(saludo)
>>> saludo.upper()
>>> saludo.lower()
>>> saludo.count('o')
>>> saludo.replace('o','a')
```


> 🧗‍♀️ Desafío III: Probá las lineas anteriores y anotate para qué sirve cada uno de los métodos y funciones.  
>
> Para pensar 🤔: ¿Se podrán combinar los métodos? Probá hacer `saludo.upper().lower()` ¿Qué dá? ¿Por qué?
>
> 🧗‍♀️ Desafío IV: Vimos que el método replace nos permite reemplazar un caracter por otro de un string dado, pero nos dejará reemplazar un segemento más largo?  Probá hacer `saludo.replace("mundo", "terricolas")`
>
> Para pensar 🤔: ¿Si imprimís `saludo` luego de ejecutar la linea anterior qué obtenés? ¿Cambió el valor de la variable?
>
>📚 Para investigar: ¿Qué es la inmutabilidad en Python?

[11. El todo y la nada](#11-in)


Cuando trabajamos con strings también puede resultarnos útil saber si uno contiene a otro, para ello utilizamos el operador `in`:

```python
>>> "mar" in "marinero"
```

[12. Síndrome de Diógenes](#11-listas)

Python nos permite pensar en grande y acumular datos en lo que se conoce como un tipo de datos  `lista`. Esta nos permiten manipular un gran número de datos en forma sencilla. Y sus elementos pueden ser cadenas, números, ¡incluso otras listas! 

Las listas se escriben separando a sus elementos con comas, y agrupando a todos entre corchetes:

```python
lista = []
```

Al igual que se puede acceder a los distintos caracteres de una cadena, podemos acceder a los
elementos de una lista indicando entre corchetes el número de elemento que queremos obtener.
Recordá que Python comienza a contar desde cero. Para obtener el segundo elemento, podemos
escribi