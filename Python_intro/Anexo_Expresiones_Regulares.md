[raw string]()

A causa de que las expresiones regulares a menudo utilizan caracteres de escape (como por ejemplo la barra invertida \), es necesario indicar que las mismas no se interpreten como tales sino como parte de la expresión regular propiamente dicha. La forma más simple de hacerlo es comenzar la cadena con una letra r para indicar que la misma debe tomarse literalmente. En Python, esto se denomina un raw string.

>El ejemplo más simple de una raw string es r'\n'. Como resultado, Python «verá» dos caracteres: '\' y 'n'. Por otra parte, si escribiéramos '\n' (sin la r al principio), Python lo interpretaría como un solo caracter (el salto de línea).

[Evaluación resultado de una busqueda]()

Si bien utilizando, por ejemplo, el método _search_ de la biblioteca **re** podemos obtener el string buscado y la posición donde se encuentra, muchas veces lo que queremos es simplemente saber si la búsqueda arrojó un resultado positivo y en base a eso realizar otras acciones. Es decir, lo único que queremos como condición es que exista. Recuerden que si al buscar no se encuentra nada se devuelve ```None```, el cual es un objeto que nos dice que no hay nada. Utilizando esto se puede armar la condición de una manera intuitiva:

```Python
import re
if re.search(patron, texto) is not None:
	bloque de código
else:
	bloque de código
```

De esta manera lo que estamos diciendo es que si la búsqueda no me da un objeto vacío (es decir la búsqueda encontró algo) se ejecuten ciertas órdenes y en caso contario (si se requiere) se ejecutan otras.

[Unión de rangos]()

Los rangos, como ya vieron, es una manera abreviada de escribir una serie de caracteres los cuales van formar parte de nuestra expresión regular para buscarlos o ignorarlos. Para esto simplemente ponían el inicio y el fin del rango entre corchetes y separados por un guión ([a-z] para todas las letras en minúscula) y para ignorar el rango utilizaban el carácter ```^``` ([^a-z] cualquier cosa excepto las letras minúsculas), sin embargo, ¿qué pasa cuando queremos buscar cosas que incluyan a más de un rango? Como por ejemplo, podríamos querer buscar todos los caráteres alfabéticos sean minúsculas o mayúsculas. En este caso los rangos se deben escribir uno seguido del otro sin separación alguna, dentro de los corchetes: [a-zA-Z]

[```group()``` y ```findall```]()

Como vieron en la teoría este método sirve para mostrar el resultado de una búsqueda, pero miremos algo:

```python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
>>> patron = "amet"
>>> re.search(patron, texto).group()
'amet'
>>> re.search(patron, texto).group(0)
'amet'
```

El método ```group()``` (o ```group(0)```) nos devuelve la coincidencia. Sin embargo si lo que se quiere no es encontrar un patrón en particular, sino obtener lo que está dentro de cierto patrón (por ejemplo lo que hay entre ciertas palabras) hay que modificar el patrón. Veamos lo siguiente:

```Python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
>>> patron = "ipsum(.*)sit"
>>> re.search(patron, texto).group()
'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
>>> re.search(patron, texto).group(0)
'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
>>> re.search(patron, texto).group(1)
' dolor sit amet, consectetur ipsum elit. Amet '
```

Acá se utilizaron algunos metacaracteres, como lo son el punto (**.**) para indicar que puede ser cualquier carácter, y el asterísco (__*__) para indicar que puede haber 0 o más de estos caracteres. De esta manera obtenemos como resultado lo que se encuentre entre las palabras "ipsum" y "sit", sin embargo observen dos cosas. Primero, el string que nos devuelve tiene dentro un substring que debería haber sido encontrado en la búsqueda: "ipsum dolor sit", pero que sin embargo no aparece. Segundo, nuevamente al hacer ```group()``` o ```group(0)``` obtenemos la coincidencia, pero si nos queremos quedar con el substring que está contenido entre estas palabras debemos utilizar ```group(1)```.
Ahora bien, como vimos, usar el patrón de búsqueda de esta manera prioriza los matches externos, es decir, busca el primer delimitador ("ipsum" en nuestro caso) y luego abarca todo hasta la última aparición del segundo delimitador ("sit"). Existe una forma de priorizar los matches internos y es con el metacarácter ```?```:

```Python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
>>> patron = "ipsum(.*?)sit"
>>> re.search(patron, texto).group()
'ipsum dolor sit'
>>> re.search(patron, texto).group(0)
'ipsum dolor sit'
>>> re.search(patron, texto).group(1)
' dolor  '
```

Cuando se quieren obtener todas las apariciones del patrón se utiliza el método ```findall``` el cual actúa para cada coincidencia como si devolviera el ```group(1)```, es decir devuelve en una lista la parte que se encuentra dentro de los delimitadores.

```Python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
>>> patron = "ipsum(.*?)sit"
>>> re.findall(patron, texto)
[' dolor ', ' elit. Amet ']
```

[¿Palabras?]()

Como ya saben la computadora no lee a los strings o cadenas de caracteres tal cual lo hacemos nosotros. En el lenguaje humano se tiende a seprar una frase por palabras, sin embargo la computadora no entiende esto, pero tranquilos que hay formas de hacérselo entender. Con las expresiones regulares se puede utilizar un metacarácter ```\b``` el cual delimita caracteres alfanúmericos de otros que no lo son. De esta manera podemos obtener las palabras de alguna frase si delimitamos la búsqueda con este metacarácter al inicio y al final. Así podemos, por ejemplo, reemplazar fácilmente alguna palabra en particular.

```Python
>>> import re
>>> texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
>>> patron = r"\bipsum\b"
>>> re.sub(patron, "lapsus", texto)
re.sub(patron, "lapsus", texto)
```