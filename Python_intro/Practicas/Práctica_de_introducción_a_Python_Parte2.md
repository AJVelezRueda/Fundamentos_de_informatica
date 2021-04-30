# **Práctica de introducción a Python - Parte 2**

### Alternativa condicional

##### **Ejercicio 1**
Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.

##### **Ejercicio 2**
Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).

##### **Ejercicio 3**
Escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en la cara opuesta de un dado. Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.

##### **Ejercicio 4**
Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, América Central, América del Norte, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido, tal como se muestra en la tabla:
| Zona | Ubicación | Costo/gramo |
| -- | -- | -- |
| 1 | América del Sur | 10.00 dólares |
| 2 | América Central | 15.00 dólares |
| 3 | América del Norte | 18.00 dólares |
| 4 | Europa | 24.00 dólares |
| 5 | Asia | 30.00 dólares |

Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. Realizá un programa para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

##### **Ejercicio 5**
Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.

### Listas

##### **Ejercicio 6**
Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.

_Recordá que la manera de copiar una lista en otra es:_

```python
lista2 = list(lista1)
```

##### **Ejercicio 7**
Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista.

##### **Ejercicio 8**
Realizá un programa que declare tres listas _lista1_, _lista2_ y _lista3_, donde las dos primeras listas deben tener cinco enteros cada una, ingresados por teclado y asigne para cada elemento de la _lista3_ la suma de los elementos de la _lista1_ y la _lista2_ (es decir, el primer elemento de la _lista3_ tiene que ser la suma del primer elemento de la _lista1_ y el primero de la _lista2_)

##### **Ejercicio 9**
Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. Se debe introducir el nombre y la edad de cada alumno por teclado. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (__*__). Al finalizar se deben mostrar los siguientes datos:

* La edad máxima de todos los alumnos.
* Los alumnos que tengan la edad máxima

### Diccionarios

##### **Ejercicio 10**
Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).

##### **Ejercicio 11**
Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.

##### **Ejercicio 12**
Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo. Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.

### Funciones

##### **Ejercicio 13**
Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro creando la función **esMultiplo**.

##### **Ejercicio 14**
Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa tiene que pedir el número de días que se van a introducir.

##### **Ejercicio 15**
Creá un programa para gestionar datos de los socios de un club, el cual permita:

* Cargar la información de los socios en un diccionario para acceder por número de socio. Los datos que se deben almacenar son: _número_, _nombre y apellido_, _fecha de ingreso (ddmmaaaa)_, _cuota al dia (s/n)_ (el programa tiene que dejar de cargar cuando se ingrese el _número_ **0**). El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

  **Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día**
  
  **Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día**
  
  **Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día**

* Informar la cantidad de socios que tiene el club.

* Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.

* Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.

* Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).

* Imprimir el listado de socios completos.

Definir las funciones que creas necesarias.
