# **Práctica de introducción a Python - Parte 1**
_Antes de iniciar con los ejercicios asegúrense de tener instalado correctamente Python y un IDE (preferentemente Visual Studio Code). Además, en los sistemas que tengan Linux y Mac tienen que tener instalado Bash._

##### **Ejercicio 1**
 Escribir un programa que imprima la longitud de un string el cual se lee por teclado.

##### **Ejercicio 2**
Realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado en mayúscula (Asegurarse de que el string tenga la cantidad de caracteres suficientes).

##### **Ejercicio 3**
Escribir un programa que pregunte el nombre y apellido al usuario y lo salude.

##### **Ejercicio 4**
Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas

##### **Ejercicio 5**
Realizar un programa que lea tres números por teclado y calcule el promedio de ellos.

##### **Ejercicio 6**
Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuántas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.

##### **Ejercicio 7**
Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada venta que realiza. Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, teniendo en cuenta estas ventas y su sueldo base.

##### **Ejercicio 8**
Escribir un programa para calcular la nota final de un estudiante, teniendo en cuenta que por cada respuesta correcta el estudiante suma 4 puntos, por cada incorrecta se le resta 1 punto y si la respuesta está en blanco no se le suma ni se le resta.

##### **Ejercicio en grupo I - Compra de una casa**
Uno de los sueños comunes entre las personas sin duda es poder tener una casa propia, sin embargo (en general) no es algo muy sencillo, ya que hay que ahorrar bastante solo para el depósito de la casa. En este ejercicio hay que determinar cuánto tiempo tomaría ahorrar la cantidad suficiente de dinero para pagar el depósito. Para esto vamos a tomar algunas suposiciones:

>    1. Llamemos al valor de la casa **costo_total**.
>    2. El porcentaje de este costo que se corresponde con el depósito será **porcentaje_deposito**. Para este caso el porcentaje va a ser de 25%.
>    3. La cantidad actual de ahorros, **cantidad_ahorrada**, empezará en 0.
>    4. Consideremos que se realiza una inversión del dinero ahorrado por la cual se obtiene cierta ganancia, **g**, por año (es decir, por mes se obtendrían **cantidad_ahorrada** multiplicada por **g/12**). Supongamos que por esta inversión se gana 4% (**g = 0.04**).
>    5. El sueldo anual será **sueldo_anual**.
>    6. La cantidad que se ahorra por mes será **porcentaje_ahorrado**, el cual debe ser expresada como un valor decimal del sueldo mensual (si es 10%, este porcentaje será 0.1)
>    7. Por último, al sueldo mensual lo llamaremos **sueldo_mensual** (**sueldo_anual/12**)

El programa debe calcular cuantos meses tomaría ahorrar el dinero necesario para pagar el depósito. Este programa debe preguntarle al usuario cual es su sueldo anual, que porcentaje del sueldo quiere ahorrar por mes y cual es el costo de la casa en cuestión.

- Para este problema se va a asumir que el usuario va a introducir valores válidos para las variables (es decir, no van a ingresar un string en el valor de la casa).