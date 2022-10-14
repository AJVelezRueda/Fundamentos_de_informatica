# Aplicaciones sencillas con ipywidgets

🚨 Este material fue creado por **Ana Julia Velez Rueda** y como todo el repositorio se encuentra bajo licencia 

[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

<details>
  <summary>🚨 REQUERIMIENTOS</summary>

En este abordaremos los contenidos relativos programación Web. Para ello vas a necesitar instalarte [ipywidgets] (https://ipywidgets.readthedocs.io/en/latest/user_install.html), [Voilá](https://voila.readthedocs.io/en/stable/using.html) y [Jupyter](https://jupyter.org/install):

```bash
    pip install ipywidgets

    pip install voila

    pip install jupyter
```

Primero puedes verificar si está o no instalado escribiendo en la consola de Python:
```python
  import ipywidgets as widgets
```


</details>

## Take it easy y Voilá: una forma sencilla de unir el back y el front

Ahora que [sabemos](https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/WEB_%26_HTTP/maquetado.md) crear contenido web con `HTML` y darle estilo con `CSS`, vamos a crear nuestra propia aplicación web, uniendo todo lo que aprendimos hasta [aquí](https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/WEB_%26_HTTP/HTTP_%26_REST.md). 

Para poder crear y renderizar (visualizar) nuestra aplicación utilizaremos voilá y crearemos la interfaz gráfica utilizando la biblioteca ipywidgets. Para ello debemos primero instalar las bibliotecas como se indica el [comienzo de este tutorial](#índice), luego:

✅ Crearemos nuestra aplicación en un cuaderno de `Jupyter` (es decir un archivo de extensión 'ipynb'). 

✅ Podés usar el template disponible en la carpeta de [`Recursos`](https://github.com/AJVelezRueda/Fundamentos_de_informatica/tree/master/WEB_%26_HTTP/Recursos).

✅ En una terminal levantaremos el servidor, ejecutando el comando:

```bash
voila ipywidgets.ipynb --autoreload=True
```

Automáticamente se abrirá en nuestro navegador una pestaña que nos mostrará como se vería nuestra aplicación en el cliente a medida que la creamos. 

¡Ahora que tenemos todo andando podemos comenzar!

Como estuvimos explicando anteriormente, la forma de presentar los datos provenientes del servidor del lado del cliente es mediante el uso de HTML. En particular `ipywidgets` posee un constructor de `HTML` que nos permite construir código HTML. Vamos a comenzar entonces agregando un título de nuestra página y un texto de bienvenida:

```python
  import ipywidgets as widgets
  from ipywidgets import HTML

  h1_main_section = widgets.HTML("""
    <h1 style='font-size:25px; color:black'>
        <b>Welcome to my first API!</b>
    </h1>""")

main_text = widgets.HTML("""
    <p style='font-size:25px; color:black'>
    This is an API built in Python 
    </p>""")
```

Como podés ver, estamos estilando cada elemento aprovechando el atributo `style`. En la vida real, no es la forma más recomendada agregar los estilos en el HTML, pero en el universo Python nos lo vamos a permitir.

Una vez creados estos elementos, darle un lugar en nuestro documento HTML, encapsularlo u organizarlo de algún modo para luego poder estilarlo. ¡Y qué mejor forma de organizar las cosas que en cajitas! En este caso echaremos mano del constructor VBox, que nos permite crear contenedores o secciones en nuestro HTML y poner dentro la lista de los elementos que desamos agrupar en dicha sección:

```python
from ipywidgets import VBox

main_section_vbox = widgets.VBox([h1_main_section, main_text])
```

Ahora que tenemos nuestra cajita podemos mostrarla en nuetsra interfaz:


```python
from IPython.display import display
display(main_section_vbox)
```

¡Y Voilá! Pero momento... si,puede ser que querramos estilar nuestra sección para que no se vea tan fea su disposición en la página. Para ello podemos aprovechar el parámetro `layout` del método VBox al que le pasaremos un objeto con todas los estilos desados para nuestra sección:

```python
from ipywidgets import Layout

layouts_intro = Layout(display='flex',
                    flex_flow='flex-wrap',
                    flex_direction='column',
                    width='61%',
                    margin='0px 10px 5px 20px',
                    padding='2px 4% 0 1%',)

main_section_vbox = widgets.VBox([h1_main_section, main_text], layout=layouts_intro)
```

¡Y ahora sí Voilá! ¡Finalmente tenemos nuestra aplicación, con su interfaz!


> 🏅 Desafío IV: Investigá en la documentación de  `ipywidgets` qué otros elementos HTML podés mostrar y probalos
>
> Podés conocer sobre algunas aplicaciones de esta tecnología [aquí](https://www.youtube.com/watch?v=GVuu728P2RU) 