# *Introducción a Python*

En este recorrido aprenderemos los conceptos básicos de programación y la sintáxis de [Python](https://www.python.org.ar/). Para ello vas a necesitar instalarte [Python](http://ufq.unq.edu.ar/sbg/archivos/guias_talleres/Guia_Instalacion_Python_2020.pdf) y algún [editor de código](https://code.visualstudio.com/) (IDE) que te sea útil para programar. 

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
  * [10. Chamuyo: del lunfardo el arte de manipular palabras](#10-metodos-strings)
  * [11. El todo y la nada](#11-in)
  * [12. Síndrome de Diógenes](#12-listas)
  * [13. Piano piano se va lontano](#13-listas-metodos)
  * [14. Matryoshka de datos ](#14-diccionarios)
  * [15. Comentario aparte ](#15-comentarios)
  * [16. ¡Atender, atender! Comienza la función](#16-funciones) 🤡
  * [17. Quedándote o yéndote](#17-if)
  * [18. Vueltas y mas vueltas](#18-for)


  * [19. Salir de la caja](#19-scripts)


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
>>> lista = [2,5,4]
```

Al igual que se puede acceder a los distintos caracteres de una cadena, podemos acceder a los
elementos de una lista indicando entre corchetes el número de elemento que queremos obtener.
Recordá que Python comienza a contar desde cero. Para obtener el segundo elemento, podemos
escribir:

```python
>>> lista[0]
```

> Para pensar 🤔: ¿Cómo podrías conocer la longitud de la lista?


[13. Piano piano se va lontano](#13-listas-metodos)

Podemos agregar (append) elementos a nuestra lista o quitarlos (remove) del siguiente modo:

```python
>>> lista.append('25')
>>> lista.remove('2')
```

> Para pensar 🤔: Probá la sentencia `lista.index('25')` ¿Qué resultado obtenes? ¿Para qué sirve _index()_

[14. Matryoshka de datos ](#14-diccionarios)

Los diccionarios, al igual que las listas, nos permiten almacenar datos. Los diccionario son mutables, es decir que podemos agregar o quitar elementos de él y los valores almacenados en él  pueden ser modificados.

A diferencias de las listas los valores que se almacenen en el diccionario no poseen un orden. Es decir, que no accesdemos a los valores por su posición (index), sino por su llave (_key_).

Podemos declarar un  diccionario vacío haciendo:

```python
>>> diccionario = {}
>>> diccionario = dict()
```

O dando un cierto valor a una llave dada:

```python
>>> diccionario = {"llave": "valor"}
```

Vale la pena aclara que una llave podrá ser cualquier objeto inmutable y el valor puede ser cualquier tipo de dato ¡Hasta un diccionario!

Podeemos acceder, entonces al valor de una llave en particular por medio de su llave:

```python
>>> diccionario["llave"]
```

¿Y si no recordamos las llaves del diccionario? Podemos acceder a todas las llaves mediante:

```python
>>> diccionario.keys()
```

> Para pensar 🤔: ¿Cómo harías para obtener todos los valores de un diccionario?


[15. Comentario aparte ](#15-comentarios)

En Python tenemos la posibilidad de incluir texto que, aunque esté escrito en el programa, no deba
ejecutarse. Esto se logra empezando la línea con el símbolo # (el hash o numeral). Estas líneas se
llaman “comentarios” y se utilizan para incluir en el programa algunas aclaraciones acerca del código:

```python
>>> # definir la variable ‘nombre’ e imprimirla
>>> nombre = “Ana”
>>> nombre
```

[16. ¡Atender, atender! Comienza la función](#16-funciones) 🤡

¿Vos también flashaste obra de teatro? 🧐 Bueno, en realidad hablamos de otro tipo de funciones… Nos referimos a esos bloques de código a los que les ponemos un nombre (¿Cuca? 🐁), que ejecuta las operaciones deseadas y devuelve un valor o realiza una tarea.

Hasta ahora hemos venido ejecutando código línea a línea para lograr nuestro cometido. Pero, si bien no es estrictamente necesario que tu código tenga funciones para hacer lo que querés que haga, sí es muy recomendable. ¿Por qué? Bueno, las funciones nos permiten separar las tareas y reutilizarlas en otros programas.

¿Cómo se usan estas funciones? ¿Cómo hago para obtener resultados? ¿Cómo puedo indicarles ciertos
parámetros que modifiquen los resultados obtenidos? 
Basta con poner el nombre de la función y, entre paréntesis, sus argumentos. Veamos entonces cómo
es que se define una función:


```python
def funcion(argumento):
    Operación sobre el argumento
    return aquí va el resultado quiero devolver
```

Así por ejemplo si quisiéramos escribir una función que nos permita obtener el doble de un número,
podemos escribirla del siguiente modo:

```python
def doble(numero):
    resultado = numero * 2
    return resultado
```

Cómo ves definir funciones en Python resulta relativamente sencillo, estas nos permiten recibir
múltiples parámetros, hacer algo con ellos y devolver un resultado procesado ¡Unas verdaderas
maquinitas!


>
> 🧗‍♀️ Desafío VI: Después de tanto programar necesitamos unos matecitos. Hoy aprendiste a prepararlos. Lo que no estoy segura es de que el agua alcance para toda la ronda. Suponiendo que cada cebada de mate consume del 30 ml de agua. Cosntruí una función que nos permita calcular cuántos termos de 1000 ml llenos consumiremos para un ronda dada (es decir una cantidad de personas dada).
>
>
> 🧗‍♀️ Desafío VII: Siempre con los mates, vienen bien unas facturitas 🥐🥐
>
>¿Si hacemos una `vaquita` ? _Vaquita_ se le dice en Argentina a hacer una colecta de plata para un fin común. Creá función que nos permita dividir los costos de una docena de facturas entre cierta cantidad de comensales.
>
>

Ahoraa que sabemos cómo definir funciones y podemos reciclar código y automatizar cálculos 
¡¡El cielo es el límite!! 



[17. Quedándote o yéndote](#17-if) 🎶🎵

Como en todo, a la hora de escribir un programa debemos tomar decisiones y las decisiones que
tomamos siempre dependen de los condicionantes que se presentan. 
En Python (como en otros los lenguajes de programación) existe una sentencia llamada if (del inglés: si condicional) que le permite al programa hacer una cosa u otra, dependiendo de las condiciones que fijemos. Si cierta condición se cumple, entonces el programa hace algo. En el caso de que la condición no sea cierta podemos pedirle que haga algo más usando la sentencia else.

La estructura de esta sentencia es la siguiente:

```python
if condición:
aquí van las órdenes que se ejecutan si la condición es cierta
else:
aquí van las órdenes que se ejecutan si la condición es falsa
```

Como verás una sentencia if se compone de un `if`, que significa “si”, seguido de una ’condición’ y terminando con dos puntos (:). Una condición es un cálculo de programación cuyo resultado es verdadero (`True`) o falso (`False`), y se crea utilizando los operadores relacionales que ya conocés (==, >, <, !=). 

La línea siguiente son las órdenes a ejecutar si la condición es cierta, y siempre comienza con un `tab`. La sentencia else consiste de un `else`, que significa “de lo contrario”, y dos puntos (:). En la línea de abajo se escriben las órdenes a ejecutar en caso de que la condición if no sea cierta, también comenzando con un `tab`. 

Es muy importante dejar esta tabulación o sangría (un espacio en blanco, insertado con la tecla tab; o cuatro espacios con el ingresados espaciador) en el comienzo de la línea de abajo; ya que le permite al intérprete de Python saber en qué orden debe ejecutar cada cosa. De olvidar esta sangría Python te hará saber que no le gustó, con el cartel: `IndentationError:expected an indented block`.



>
> 🧗‍♀️ Desafío VIII: En una ronda pequña de mate 🧉 no hace falta llenar tooooodo el termo, con un poco de agua quizás alcanza. Definí una función _calcular_cantidad_de_agua_ que espere una cantidad de personas como argumento y devuelva la cantidad de mililitros con los que tenemos que cargar el termo. 
>
>👀  ¡OJO!  Si llega a 1000 debería retornar la advertencia `"vas a necesitar más de un térmo"` 
>


[18. Vueltas y mas vueltas](#18-for)


[17. Salir de la caja](#17-scripts)

Un script es una secuencia de comandos, o en criollo un programa muy simple. Eso que fuimos ejecutando linea a linea, perfectamente podría escribirse en un archivo para ejecutarse una sola vez, más comodamente.

Por convención, los archivos de los scripts de python tienen extensión ‘.py’. Para ejecutar un script de python en la consola simplemente debemos escribir:

```bash
python3 <nombre_del_archivo.py> <argumentos>
```
Bueno..no tan simplemente. Esta forma de correr un script puede variar de un sistema operativo a otro. Si estas en Windows, tenés que abrir el cmd de windows en la carpeta donde tengas el script y correr el comando:

```bash
 "python script.py"
```