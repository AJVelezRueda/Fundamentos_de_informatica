# [Practica] *HTTP & REST *

🚨 Este material fue creado por Ana Julia Velez Rueda y como todo el repositorio se encuentra bajo licencia 
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


> En este recorrido se basa en el recorrido se basa en el material [http-tutorial](https://github.com/AJVelezRueda/http-tutorial/tree/master/tutorial/es) de los autores Franco Leonardo Bulgarelli y Ana Julia Velez Rueda


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

En general un servidor Web provee varios contenidos diferentes, es por ello que existen las URLs. Estas nos permiten identificar y localizar de forma unívoca un recurso, y dentro del servidor, encontraremos en distintas URLs relativas al mismo. 

En general el diseño de estas URLs se hace tal que cada ruta apunta a un recurso bien definido. La semántica de cada ruta está dada en parte por el sentido propio en el contexto de ese dado dominio, pero también por el método HTTP que se utilice. 

Ejemplos:

    - /productos/45: si se usa GET, se devuelve el producto con id 45. Si se usa DELETE, se lo borra. 

    - /productos: si se usa GET devuelve todos los productos, si se usa PUT, se los actualiza en lote

    - /productos/45/ventasRecientes: si se usa GET, devuelve todas las ventas recientes del producto con id 45

>
> 🧗‍♀️ Desafío I: Estamos construyendo una aplicación Web para un biblioteca, en la cuál podrá:
>- consultar y cargar o borrar información sobre libros
>- consultar y cargar o borrar revistas y audio libros disponibles
> Escribí las posibles rutas indicando sus métodos HTTP correspondientes. 
>
> 🧗‍♀️ Desafío II: Estamos construyendo una aplicación para un e-comerce de venta de productos cosméticos naturales. La aplicación debe permitir:
> - Buscar los productos por número
> - Editar la información de los productos
> - Eliminar la información de los productos
> Escribí las posibles rutas indicando sus métodos HTTP correspondientes.
>