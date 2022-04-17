# Paradigmas de programación

# Introducción a la programación con objetos
> Estas guías están basadas en las guías de [Objetos y mensajes en Python 3](https://github.com/mumukiproject/mumuki-guia-python3-objetos-y-mensajes) de [Mumuki.org](https://mumuki.io/home/), el material teórico de [PdeP de UTN]() y el recorrido [recursos de Python](https://github.com/flbulgarelli/recursos-python)
>
> Cada contenido teórico puede ir desarrollandose segun el recorrido teórico que se propone en la guía de POO del repositorio de [recursos de Python](https://github.com/flbulgarelli/recursos-python/tree/master/4_programacion_con_objetos) Autor: [Franco Leonardo Bulgarelli](https://github.com/flbulgarelli)

# Guias de Temas
* [1. Paradigmas de Programación](#1-paradigmas)
* [2. Programación Orientada a Objetos](#2-POO)
* [3. Objetos y mensajes](#3-obejtos-y-mensajes)
* [4. Ambientes e interfaces](#4-interfaz)
* [5. Calses y polimorfismo](#5-clases-polimorfismo)
* [6. Interfaces compartidas](#6-interfaz-compartidas)
* [7. Clases](#7-clases)
* [8. Parecidos pero distintos: métodos vs funciones](#8-metodos)
* [9. Herencia](#9-herencia)


[1. Paradigmas de Programación](#1-paradigmas)
Un paradigma de programación es un conjunto de ideas que describe una forma de entender la construcción de programa. Estas ideas nos permiten pensar y estructurar el código de distintas formas. Ninguna forma es mejor que otra,si no que son útiles o no para una circunstancia dada o para resolver un problema dado.
Existen lenguajes que se concentran en las ideas de un único paradigma así como hay otros que permiten la combinación de ideas provenientes de distintos paradigmas.

[2. Programación Orientada a Objetos](#2-POO)
En particular el paradigma de Programación Orientada a Objetos (POO) es un estilo o una forma de pensar los programas en la cual se estructura un programa construyendo piezas simples y reutilizables de código para crear instancias individuales de objetos. 

Un programa basado en este paradigma es un conjunto de objetos que interactúan entre sí en un ambiente mandándose mensajes para lograr un objetivo determinado.

[3. Objetos y mensajes](#3-obejtos-y-mensajes)
Un objeto es un ente computacional que con el que podemos comunicarnos mediante mensajes y puede (o no) tener un estado interno (referencias a otros objetos).

¡Veamos un ejemplo concreto que nos ayude a entender un poco más! Imaginemos que somos ornitólogos y ornitólogas que estudiamos el comportamiento de las aves, y Pepita es una golondrina que tenemos en nuestro conjunto de aves:

```python
from aves import pepita
```

¿Qué características tendrá Pepita? ¿Qué sabe hacer? ¿Será distinto de lo que hacen otras aves? Por ejemplo ¿Sabrá volar_en_circulos?

```python
pepita.volar_en_circulos()
```

¿Sabrá cantar_boleros?

```
pepita.cantar_boleros()
# AttributeError: 'Golondrina' object has no attribute 'cantar_boleros'
```

¡Ups, no! Parece que no sabe cantar voleros 😖 ¿Y sabrá comer_alpiste?

```
pepita.comer_alpiste()
# TypeError: comer_alpiste() missing 1 required positional argument: 'gramos'
```
😱 ¡Ups! sí, pero tenemos que decirle cuantos gramos de alpiste queremos que coma:

```
pepita.comer_alpiste(10)
```

> 💡 Formalización:  
> `pepita` es un objeto, y como todo **objeto**, entiende algunos **mensajes**.
> En particular, nuestra golondrina entiende los mensajes `comer_alpiste` y `volar_en_circulos`,
> pero no entiende `cantar_boleros` (ni casi ninguna otra cosa que se te ocurra :wink:).
>
>En otras palabras, `pepita` _sabe_ comer alpiste y volar en circulos.
>
> Por otro lado, aprendimos que si le pedimos a un objeto que haga cosas que no sabe hacer, éste se rehusará.

¿Y qué pasa cuando le _enviamos_ estos mensajes? ¡Porque es de esperar que `pepita` no tenga infinita energía para hacer todo lo que le pidamos! Sin embargo puede saber cuanta es la `energia` que le queda:

```python
pepita.energia
```

> 🎯 Sabiendo esto, ¿te animás a averiguar cómo queda la energia después de hacerla comer alpiste? ¿y después de hacerla volar en círculos?


Como vemos, cada vez que hacemos que pepita coma y vuele, su energia cambia.



> 💡 Formalización: 
>los objetos pueden tener **estado** (en el caso de pepita, su estado es la energía), el cual puede cambiar a lo largo del tiempo.

> 🎯 ¿Te animás a averiguar según qué formula?

> 💡 Formalización: cada vez que un objeto recibe un mensaje, _hace_ algo, reaccionando al mismo. Por tanto, decimos que los objetos tienen un cierto _comportamiento_ (por ejemplo, cuando pepita come alpiste, su energia sube en tantas unidades como los gramos ingeridos)


[4. Ambientes e interfaces](#4-interfaz)

`pepita` no es nuestra única golodrina. También contamos con `anastasia`. ¿Tendrá su misma energia?

```
anastasia.energia
pepita.energia
```

`anastasia` es otro objeto, y como tal, cuenta con su propio estado. Por eso es que si bien las dos tienen `energia`, presentan valores diferentes. ¿Qué cosas sabrá hacer `anastasia`?


```python
anastasia.volar_en_circulos()
anastasia.comer_alpiste(10)
```

Como `anastasia` es otra golondrina, sabe hacer las mismas cosas que `pepita`.

> 💡 Formalización:
> llamaremos _ambiente_ al contexto en el que el viven los objetos, tienen su estado y pueden entender mensajes. En un mismo ambiente podemos contar con varios objetos, como por ejemplo, pepita y anastasia. En otras palabras es el mundo que los objetos habitan y en que se relacionan. Cada vez que apretamos play en replit, o le damos reset en colab, o cerramos nuestro intérprete de python en nuestra computadora y lo volvemos a iniciar, estamos destruyendo ese mundo y volviendo a empezar.
>   

Pero no sólo contamos con `pepita` y `anastasia`, sino también con `roberta`. ¿Cuánta energía tendrá inicialmente?

```python
roberta.energia
```

😱 Ohh, ¡tiene mucha energia! Y también sabrá volar en círculos, ¿no?

```python
roberta.volar_en_circulos()
roberta.energia
```

Bien, aunque como vemos perdió sólo una unidad de energía, pese a que anastasia y pepita gastan 10 al hacerlo.
Parece que las tres saben hacer lo mismo, pero roberta lo hace de forma _diferente_.

> 💡 Formalización: no todos los objetos tienen que reaccionar de igual forma a los mismos mensajes. En otras palabras, no todos los objetos tienen por qué comportarse igual.

¿Y qué hay sobre `comer_alpiste`?

```python
roberta.comer_alpiste(10)
```

Ey, ¡no le gusta el alpiste! Pero nos dijeron que sí le gusta comer peces:

```python
roberta.comer_peces(2)
roberta.energia
```

> 💡 Formalización: 
>no todos los objetos tienen qué entender los mismos mensajes. Por ejemplo `roberta` no entiende `comer_alpiste`, pero sí entiende `comer_peces` (que anastasia y pepita no entienden, si no nos creés podés comprobarlo vos :smile:). Al conjunto de mensajes que cada objeto expone lo llamaremos **interfaz**, la cual puede ser (y típicamente será) diferente para cada objeto.

Qué rara es nuestra nueva golondrina, ¿no? ¡Es que no es una Golondrina! ¡Es un dragón! :fire:

```python
roberta.escupir_fuego()
```

Perdón, esperamos no haber quemado nada :see_no_evil:

[5. Calses y polimorfismo](#5-clases-polimorfismo)

Momento, ¿y cómo están definidas `pepita`, `anastasia`  y `roberta`? ¿Dónde dice _qué_ saber hacer cada una y _cómo_?

En el paradigma de objetos, los mismos se crean a partir de _moldes_ llamados **clases**, que sirven para dar vida a objetos que se comporten de igual forma. Por ejemplo nuestras golondrinas `pepita` y `anastasia` se crearán de la siguiente forma....

```
pepita = Golondrina(100)
anastasia = Golondrina(200)
```

... partir de una clase llamada `Golondrina` que se verá así:


```python
class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms
```


> 💡 Formalización: al acto de crear un objeto a partir de una clase se lo denomina _instanciación_, y por tanto a los objetos también se los denomina _instancias_ (de una clase particular). Por ejemplo, `pepita`  es una instancia (de la clase `Golondrina`).
>
> Si bien el término _instancia_ quizás no nos diga mucho, en este contexto significa "ejemplo", dado que cada golondrina como pepita o anastasia son ejemplo concretos (es decir, casos particulares) de la idea más general de una Golondrina.


Como vemos, una clase es nuevo tipo de definición, que se suma a las funciones y procedimientos que ya conocíamos. Se escribe mediante la palabra reservada `class`, seguida de un nombre y `:`. Dentro de ella encontraremos los métodos, que son el código que especifica cómo se comportará un objeto cuando reciba un mensaje.


> 📝**Nota**: sí, los métodos se definen usando la misma palabra clave `def` que usabamos para funciones y procedimientos. Sin embargo, no son lo mismo: como podemos ver los métodos siempre están "dentro" de una clase, y además tienen como primer parámetro `self`. El _self_ representa la instancia de la clase. Al usar la palabra clave "self" podemos acceder a los atributos y métodos de la clase en Python. Más sobre esto, en breve.

> Desafío: Ahora te toca a vos!
>
> * Hacer `esta_debil`: si tienen menos de 10 puntos de energia (golondrinas) o 50 (dragones)
> * Hacer `esta_feliz`: si tiene más de 500 puntos de eneria (sin importar cuál)
> * Hace a `hipo`, entrenador de dragones: sabe aceptar a dragones y luego hacerlos entrenar, haciendoles dar 20 vueltas en circulos y luego comer su comida favorita hasta saciarse (3 peces)
>

[6. Interfaces compartidas](#6-interfaz-compartidas)

Entonces, ¿`pepita` y `roberta` se comportan igual? ¡No! ¿Y tienen la misma interfaz? ¡Tampoco!
Pero sí tienen una parte común; en otras palabras comparten (parcialmente) una interfaz:


|              | 🌾 `comer_alpiste` | 🐟 `comer_peces` | 🔥 `escupir_fuego` | ✈️ `volar`| 🔄 `volar_en_circulos`|
|:------------:|:----------------:|:-------------:|:-------------:|:------:|:------------------:|
| `pepita`     |   ✅️             |               |               | ✅️     | ✅️                 |
| `anastasia`  |   ✅️             |               |               | ✅️     | ✅️                 |
| `roberta`    |                  |✅️             |✅️             | ✅️     | ✅️                 |


[7. Clases](#7-clases)

Momento, ¿y cómo están definidas `pepita`, `anastasia`  y `roberta`? ¿Dónde dice _qué_ saber hacer cada una y _cómo_?

En el paradigma de objetos, los mismos se crean a partir de _moldes_ llamados **clases**, que sirven para dar vida a objetos que se comporten de igual forma. Por ejemplo nuestras golondrinas `pepita` y `anastasia` se crearán de la siguiente forma....

```
pepita = Golondrina(100)
anastasia = Golondrina(200)
```

... partir de una clase llamada `Golondrina` que se verá así:


```python
class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms
```


> 💡 Formalización: al acto de crear un objeto a partir de una clase se lo denomina _instanciación_, y por tanto a los objetos también se los denomina _instancias_ (de una clase particular). Por ejemplo, `pepita`  es una instancia (de la clase `Golondrina`).
>
> Si bien el término _instancia_ quizás no nos diga mucho, en este contexto significa "ejemplo", dado que cada golondrina como pepita o anastasia son ejemplo concretos (es decir, casos particulares) de la idea más general de una `Golondrina`.

Como vemos, una clase es nuevo tipo de definición, que se suma a las funciones y procedimientos que ya conocíamos. Se escribe mediante la palabra reservada `class`, seguida de un nombre y `:`. Dentro de ella encontraremos los métodos, que son el código que especifica cómo se comportará un objeto cuando reciba un mensaje.

> 📝 Nota: sí, los métodos se definen usando la misma palabra clave `def` que usabamos para funciones y procedimientos. Sin embargo, no son lo mismo: como podemos ver los métodos siempre están "dentro" de una clase, y además tienen como primer parámetro `self`. Más sobre esto, en breve.

[8. Parecidos pero distintos: métodos vs funciones](#8-metodos)

Tomemos este método como ejemplo:

```python
class Golondrina:
  def comer_alpiste(self, gramos):
    self.energia = self.energia + 4 * gramos
```

👀 Ojo, porque los métodos y las funciones, si bien se ven parecidos, no son lo mismo.

1. Las funciones se invocan como `funcion(argumentos)`, pero los métodos se evaluan a través el envio de mensajes como `objeto.mensaje(argumentos)`
2. los métodos tienen siempre declaran como primer parámetro `self`, las funciones no
3. los métodos siempre van dentro de un `class`, mientras que las funciones van por fuera

Habrán notado que una diferencia importante entre una función y un método es el parámetro
`self` (en inglés, _si mismo_) que reciben todos los métodos en su definición. Este parámetro representa al objeto receptor del mensaje, y Python lo pasará automáticamente siempre que enviemos uno.

Por ejemplo cuando hagamos...

```python
>> pepita.comer_alipste(10)
```
... Python pasará automáticamente a `pepita` a través del parámetro `self`. Y si hacemos...

```python
>> anastasia.comer_alipste(10)
```

... `self` representará a `anastasia`. Esto nos permite que definamos métodos que accedan al estado del objeto que está recibiendo el mensaje (como en `comer_alpiste`) o que le enviemos más mensajes (como en `volar_en_circulos`, que envía a `self` el mensaje `volar`).

> ### Un poco de práctica

Ahora te toca a vos:

1. Creá a la golondrina `maria` con 42 puntos de energía inicial
2. Creá al dragón `chimuelo`, con 200 dientes y 1000 de energía inicial
3. Definí el método `esta_debil`, que nos dice si nuestras "aves" tiene menos de 10 puntos de energía (golondrinas) o menos de 50 puntos de energía (dragones)
4. Definí el método `esta_feliz`, que nos dice si nuestras "aves" tiene más de 500 puntos de energía (sin importar de qué clase sean)
5. Hace a `hipo`, entrenador de dragones: sabe aceptar a dragones, quienes son sus entrenados y hacerlos entrenar todos los dias, haciendoles dar 20 vueltas en circulos y luego comer su comida favorita hasta saciarse (3 peces)
6. Hacé que hipo pueda entrenar a las golondrinas. ¿Qué comportamiento deberían entender las golondrinas ahora?
7. Definí el método `entrenamiento_intensivo`, que hace dar vultas en circulos a sus entrenados hasta que estén débiles.


[9. Herencia](#9-herencia)

¿Ves algo repetido entre las golondrinas y los dragones? Sí, ¡el método `está_feliz`! Extraigamos la lógica común a una clase `AnimalAlado`.

```python
class AnimalAlado:
  def esta_feliz(self):
    return self.energia >= 500

class Golondrina(AnimalAlado):

  ... etc ...

class Dragon(AnimalAlado):

  ... etc ...
```

Diremos además que esta clase es una _clase abstracta_, porque no existe para tener instancias directas.

> 💡 Formalización:
> La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una clase madre sus métodos y atributos.



# Bibliografía

["Objeto, mensaje, métodos". Fernando Dodino. Material de Cátedra de Paradigmas de Programación - UTN FRBA, Argentina.](https://docs.google.com/document/d/1RBfNmKZFKZ90XvfQsN7zhtuUPV2Mvj7t-iyZiL2bClQ/edit)
