# **Manejo de excepciones**

##### **Ejercicio 1**
Dado el siguiente bloque de código contestar:

```python
lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
try:
    lista_super + "arroz"
except:
    print("no puedo agregar arroz")
```

¿Es correcto el uso del `try...except`? ¿Qué cosa/s le modificarías?

##### **Ejercicio 2**
Definir una función que tenga como parámetros una lista de números por un lado y un número por otro y devuelva una lista con la división de cada elemento por el número dado. Por ejemplo, si le paso `([2,4,6,8], 2)`, debería retornar `[1,2,3,4]`. Tomar las precauciones necesarias.

##### **Ejercicio 3**
Definir un procedimiento, que reciba una lista y un número, el cual tiene que agregar el número a la lista **solo** si el número es positivo. De lo contrario debería generar un error indicando que el número no es positivo.