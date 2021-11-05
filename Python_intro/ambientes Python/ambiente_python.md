## Ambientes de Python
> Este material fue desarrollado por [flbulgarelli](https://github.com/flbulgarelli) y [AJVelezRueda](https://github.com/AJVelezRueda)

## Guias de Trabajo
  * [1. Breve repaso de PIP](#1-pip)
  * [2. Entornos virtuales](#2-venv)
  * [3. Entornos reproducibles](#3-entornos-reproducibles)
  * [4. Distribución de paquetes](#4-distribucion-paquetes)
  * [5. Ejecución de tareas](#5-tox)
  * [6. Un atajo por favor!](#6-pyscafold)


[1. Breve repaso de PIP](#1-pip)


[PIP](https://packaging.python.org/guides/tool-recommendations/) es la herramienta de Python que nos permite gestionar paquetes en Python. Proporciona las funciones básicas esenciales para encontrar, descargar e instalar paquetes de PyPI y otros índices de paquetes de Python por medio de su interfaz por linea de comando, haciendo:

```bash
$ pip install nombre-paquete
```

Es posible especificar la versión exacta o mínima del paquete que nos queremos instalar haciendo: 

```bash
$ pip install nombre-paquete==1.1.2
```

¿Dónde se instalan los paquetes cuando se los instala con pip? Básicamente existen dos alternativas: que se instalen en  usuario, o que se instalen en el sistema operativo (esto NO). ¿Y qué implica una y otra instalación? Instalar a nivel de usuario implica que todas las versiones deberían ser compatibles.

[2. Entornos virtuales](#2-venv)

El gran problema es que cuando tenemos múltiples proyectos queremos desarrollar con versiones diferentes de cada paquete, inclusive potencialmente incompatibles, en cada proyecto. Este problema no es específico de Python, si np que sucede en todos los lenguajes de programación. Por ejemplo, en el entorno Node, NPM te instala las dependencias de forma local denrro de cada proyecto en un directorio node_modules. Así mismo, en Ruby la herramienta GEM, que es equivalente a PIP, tampoco es tan inteligente pero permite a otra herramienta BUNDLE, que entre otras cosas permite que las depencias se almacenen de forma diferencial para cada proyecto. Por último, podemos citar MABEL en Java que es similar a BANDLE.

¿Y en Python qué tenemos? [VENV](https://docs.python.org/3/library/venv.html) y [Virtualenv](https://virtualenv.pypa.io/en/latest/).  ¡Sí, son dos cosas distintas! Sin embargo, las dos nos permiten instalar versiones difernetes de los paquetes en distintos proyectos, descargándolas localmente en cada uno de ellos. La diferencia entre estas dos bibliotecas es que virtualenv no forma parte del stack standar de Python y tiene más funcionalidades. 

```bash
#creamos la carpeta example y nos movemos dentro de ella
$ mkdir example
$ cd example
#creamos un entorno virtual en el directorio .venv
$ python3 -m venv .venv 
#activamos el entorno para que a partir de ahora las dependencias se instalen dentro de .venv
$ source .venv/bin/activate
$ pip install pandas==1.1.1
#Abrimos el interprete python3
$ python3
```
```python
>>> import pandas as pd
>>> pd.__version__
´1.1.1´
```

Si ahora hacemos esto en otra terminal e instalamos otra versión de pandas en el directorio example2, veremos el poder de venv en acción:

```bash
$ mkdir example2
$ cd example2
$ python3 -m venv .venv 
$ source .venv/bin/activate
$ pip install pandas==1.3.3
$ python3
```
```python
>>> import pandas as pd
>>> pd.__version__
´1.3.3´
```

Moraleja, siempre que desarrollemos en Python scripts que no sean sencillos y usemos dependencias, nos convendrá utilizar un entorno virtual.

PD: podés desactivar tu entorno haciendo `deactivate` 🤪

[3. Entornos reproducibles](#3-entornos-reproducibles)

Cuando tenemos varias dependencias y las versiones de ellas son importantes (en general lo son), ejecutar una y otra vez `pip install` repetidas veces puede resultar engorroso. Es por eso que resulta conveniente listarlas todas en un solo archivo, para luego realizar la instalación en un solo paso. Este archivo se llama `requirements.txt` y se ve del siguiente modo:

```python
numpy==1.21.4
pandas==1.1.1
```
Este archivo puede ser generado a mano o lo podemos construir desde un entorno ya configurado, utilizando el comando `pip freeze > requirements.txt`. En cualquier caso, podremos instalar más tarde o en otra máquina todas las dependencias de nuestro proyecto en un solo paso, haciendo `pip install -r requirements.txt`(siempre con el entorno activado). 

>
> 🤖  ¡Ahora te toca a vos! Levantá un entorno virtual de nombre `ejemplo_venv` e instalá los requerimientos desde el [requirements.txt](https://github.com/AJVelezRueda/ejemplo_venv_requirements) que creamos para este ejemplo
>


[4. Distribución de paquetes](#4-distribucion-paquetes)

Tener un entorno reproducible a veces no es suficiente cuando deseamos que nuestro código sea utilizado por cualquier persona en el mundo ¿Por qué? porque la distribución de un paquete involucra más que solo listar las dependencias de nuestro proyecto.  Por ejemplo, debemos indicar su nombre, quién lo hizo, su versión actual. Si lo que distribuímos es un ejecutable, tendremos también que indicar cuál es su nombre. Además, esto le permitirá a la comunidad colaborar con nuestro proyecto de manera más sencilla. 

Python tiene dos formatos de distribución de paquetes:
- egg: que es el clásico y está en desuso
- wheel: que hoy en día es el más frecuente

Para resolver estas complejidades y formalizar la metadata de nuestro proyecto contamos con una herramienta que se llama `setuptools`. Setuptools nos permite declarar toda la información acerca de nuestros proyecto en un archivo `setup.cfg`, que se ve del siguiente modo:

```python
[metadata]
name = ejemplo_setuptools_tox
description = Add a short description here!
author = Franco Leonardo Bulgarelli
author_email = franco@mumuki.org
license = MIT
long_description = file: README.rst
long_description_content_type = text/x-rst; charset=UTF-8
url = https://github.com/pyscaffold/pyscaffold/
project_urls =
    Documentation = https://pyscaffold.org/

platforms = any

classifiers =
    Development Status :: 4 - Beta
    Programming Language :: Python


[options]
zip_safe = False
packages = find_namespace:
include_package_data = True
package_dir =
    =src

python_requires = >=3.8

install_requires =
    importlib-metadata; python_version<"3.8"


[options.packages.find]
where = src
exclude =
    tests

[options.extras_require]
testing =
    setuptools
    pytest
    pytest-cov

[options.entry_points]
# Add here console scripts like:
# console_scripts =
#     script_name = ejemplo_setuptools_tox.module:function
# For example:
console_scripts =
    fib = ejemplo_setuptools_tox.fib:run
```

A modo de cierre, vale la pena mencionar que existe una alternativa llamada `pyproject`, pero aún la comunidad de Python no se pone de acuerdo en cuál usar... De hecho, en la mayoría de los casos terminamos usando las dos. 

[5. Ejecución de tareas](#5-tox)

¿Y qué pasa cuando las tareas de construcción y mantenimiento son más complejas que instalar dependencias? Por ejemplo, podríamos tener tareas para:
- publicar el proyecto en pypi (usando [`twine`](https://pypi.org/project/twine/))
- configurar la base de datos de tu proyecto
- compilar dependencias en otros lenguajes de programación
- correr tests (usando [`pytest`](https://docs.pytest.org/en/6.2.x/))

Y así lo que se te ocurra. En casi todas las tecnologías de programación necesitamos herramientas gestoras de tareas:
- `rakefile` en Ruby
- `makefile` en c y varios otros lenguajes
- `npm` y `maven` en node y Java respectivamente (¡vuelven a parecer estos dos!)

Python en particular cuenta con varias opciones, entre ellas `invoque`, `nox` y `tox`. Estos últimos dos además nos van a permitir correr tests facilmente, contra distintas versiones de Python.

>
>✅ ¡Te dejamos [aquí](https://github.com/AJVelezRueda/ejemplo_setuptools_tox) un proyecto de ejemplo para inspeccionar, pensar y responder:
>  ¿Cómo se espefica en el proyecto la versión de Python necesaria para su instalación? 🤔 
>  
> 


[6. Un atajo por favor!](#6-pyscafold)

Es un montón lo que tenemos que hacer para arrancar un proyecto ¿No? En general en cualquier proyecto de mediana complejidad vamos a necesitar todo esto, y aún así no mencionamos otras cosas importantes si queremos tener compatibilidad con versiones más viejas de estas herramientas. 

Pero, sí, entendemos que te resulte un poco desalentador y es por eso que te proponemos un atajo. Para simplificarnos la vida entonces podemos utilizar una herramienta que nos permite generar todos los archivos de configuración del proyecto en un solo paso...¡o casi! ¡Bienvenido [Pyscafold](https://pypi.org/project/PyScaffold/)!

>
> ✅ ¡Te dejamos un [tutorial](https://gist.github.com/flbulgarelli/634973631c7c0f668b5100f09226eb8c) para configurar y publicar tu paquete en `pypi`! ¿Te gustó? ¡Dale ⭐️, compartilo, sé feliz 😋!
>