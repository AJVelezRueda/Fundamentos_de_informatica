# **Práctica Objetos - Parte 2**

##### **Ejercicio 1**
Dadas las siguientes clases responder:
* cuales son sus estados

* cuales son sus interfaces

* ¿Comparten interfaz?

* ¿Son polimórficas?


```python
class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

    def alimento(self):
	print(self.alimento)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 2

    def pasear(self, km):
	self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

    def caricias(self):
	print(self.caricias)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 4
```


##### **Ejercicio 2**
Modificar la clase **Golondrina** vista en la teoría para poder preguntar si una golondrina está en equilibrio. Este estado se alcanza cuando la energía se encuentra entre 150 y 300.


##### **Ejercicio 3** 
Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o Jeuna golondrina. Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos.
Se propone:

* implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio(). Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio, que responden True cuando se les consulta estaEnEquilibrio().

* comprobar el código que se escribió con esta secuencia:
	* definir un ornitólogo, dos golondrinas y dos gorriones,
	* inicializar las aves con valores conocidos,
	* decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
	* decirle al ornitólogo que realice su rutina sobre aves,
	* verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.


##### **Ejercicio 4**
Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:

* comienzan con una cantidad que podemos establecer de _combustible_

* los autos pueden llevar 5 personas como máximo y al _recorrer_ una distancia consumen medio litro de _combustible_ por cada kilómetro recorrido


* las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;

* pueden *cargar_combustible* en la cantidad que digamos y al hacerlo suben su cantidad de _combustible_


* saben responder si _entran_ una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

Definí las clases **Moto**, **Auto** y **MedioDeTransporte** y hace que las dos primeras hereden de la tercera.
