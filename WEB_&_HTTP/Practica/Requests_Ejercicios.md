# [Practica] *REQUESTS*

🚨 Este material fue creado por la Dra. Ana Julia Velez Rueda y como todo el repositorio se encuentra bajo licencia 
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


> En esta ejercitación se basa en el recorrido teórico de [HTTP](https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/WEB_%26_HTTP/HTTP_%26_REST.md), si no lo leíste aún te recomiendo hacerlo antes de comenzar.

<details>
  <summary>🚨 REQUERIMIENTOS</summary>

En este abordaremos los contenidos relativos a HTTP y REST. Para ello vas a necesitar instalarte [requests] (https://pypi.org/project/requests/):

```bash
pip install requests
```


Primero puedes verificar si está o no instalado escribiendo en la consola de Python:
```python
import requests
```

 Una vez que hayas completado el recorrido de HTTP podés continuar con este recorrido 👇
</details>


**🧗‍♀️ Desafío I** En base al siguiente enlace "https://pokeapi.co/api/v2/pokemon/pikachu", realizar las siguientes actividades adjuntando los archivos resultantes y el código utilizado para la realización de cada paso:

a) ¿Cuál es el dominio al que estamos consultando?

b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type? Obtené la información correspondiente al campo "forms".

c) Averigüá cuántos Pokemones almacena la API.

d) ¿Cómo esperás que sea la URL para obtener las habilidades de los Pokemons (abilities)? ¿y cómo será la url para obtener la información sobre la habilidad 2?

f) Guardar los datos correspondientes a Pikachu y Sylveon en un archivo de nombre "ficha_tecnica_pokemon.txt".

g) Describí la arquitectura cliente-servidor y los roles de cada parte


**🧗‍♀️ Desafío II** Dado el siguiente enlace "https://jsonplaceholder.typicode.com/todos", realizar las siguientes actividades adjuntando los archivos resultantes y el código utilizado para la realización de cada paso:

a) ¿Cuál es el dominio al que estamos consultando?

b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type?

c) Agregar un contenido cuyo userId es 11 y su id es 2 con un nuevo título e indicando que está completo (completed).

d) En la arquitectura cliente-servidor ¿Qué características tiene el cliente?


**🧗‍♀️ Desafío III** En base al siguiente enlace "https://pokeapi.co/api/v2/pokemon/", crear una clase llamada Pokemon, que tome como parámetro el nombre de un pokemon y realice lo siguiente:

a) Obtenga los datos completos del pokemon en cuestión (en caso de no existir, que devuelva un mensaje diciendo esto).

b) Muestre las estadísticas (stats) de ese pokemon.

c) Nos diga qué movimientos tiene.

d) Obtenga el/los tipo/s del mismo.

f) Devuelva la/s habilidad/es que tenga.

g) Nos diga el número (id) en la pokedex.

h) Obtenga el peso del pokemon

i) Guarde en un archivo la información básica del pokemon: número, nombre, tipos y movimientos. Este archivo tiene que ir juntando la información de cada pokemon que instanciemos.

j) Guarde en otro archivo la información para el competitivo (todo lo obtenido, menos el número). Nuevamente, este archivo tiene que ir acumulando la información.
