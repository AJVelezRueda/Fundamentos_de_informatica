## Ambientes de Python

## Guias de Trabajo
  * [1. Breve repaso de PIP](#1-pip)
  * [2. Entornos virtuales](#1-venv)
  * [3. Entornos reproducibles](#1-entornos-reproducibles)

[1. Breve repaso de PIP](#1-pip)
[PIP](https://packaging.python.org/guides/tool-recommendations/) es la herramienta de Python que nos permite gestionar paquetes en Python. Proporciona las funciones básicas esenciales para encontrar, descargar e instalar paquetes de PyPI y otros índices de paquetes de Python.
- para que sirve y cómo funciona, 
- dónde se instalan las cosas cuando se las guarda: usuario o sistema operativo (esto NO), qué implica una y otra instalación? Instalar a niverl de usuario implica que todas las versiones deberían ser compatibles.

[2. Entornos virtuales](#1-venv)

- Necesidad de entornos independientes
- El gran problema es que cuando tenemos múltiples proyectos queremos desarrollar con versiones diferentes de cada paquete, inclusive potencialmente incompatibles, en cada proyecto. Este problema no es específico de Python, si np que sucede en todos los lenguajes de programación. Por ejemplo, en el entorno Node, NPM te instala las dependencias de forma local denrro de cada proyecto en un directorio node_modules. Así mismo, en Ruby la herramienta GEM, que es equivalente a PIP, tampoco es tan inteligente pero permite a otra herramienta BUNDLE, que entre otras cosas permite que las depencias se almacenen de forma diferencial para cada proyecto. Por último, podemos citar MABEL en Java que es similar a BANDLE.

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

[3. Entornos reproducibles](#1-entornos-reproducibles)

Cuando tenemos varias dependencias y las versiones de ellas son importantes (en general lo son), ejecutar una y otra vez `pip install` repetidas veces puede resultar engorroso. Es por eso que resulta conveniente listarlas todas en un solo archivo, para luego realizar la instalación en un solo paso. Este archivo se llama `requirements.txt` y se ve del siguiente modo:

```python
numpy==1.21.4
pandas==1.1.1
```
Este archivo puede ser generado a mano o lo podemos construir desde un entorno ya configurado, utilizando el comando `pip freeze > requirements.txt`. En cualquier caso, podremos instalar más tarde o en otra máquina todas las dependencias de nuestro proyecto en un solo paso, haciendo `pip install -r requirements.txt`(siempre con el entorno activado). 