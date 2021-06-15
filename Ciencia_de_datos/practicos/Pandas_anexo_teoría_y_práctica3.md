## [pd.merge()]()

**how**: indica la manera de unión de los data frames, por defecto es “inner” (intersección).

**on**: indica en base a qué columna se van a unir los data frames. Esta columna tiene que estar presente en ambos data frames.

**left_on**: nombre de la columna de los datos de la izquierda el cual se va a usar para unir los data frames.

**right_on**: igual al anterior, pero con una columna de los datos de la derecha. Ambos tienen que explicitarse.

## **Hora de probar**

Creá un nuevo DataFrame a partir del DataFrame **Personas**, el cual solo tenga las columnas "persona_id", "anio" y "categoria_conicet_id" (guardalo en una variable llamada **pers**)

### **how**

```python3
pd.merge(pers, conicet,how="right", on = "categoria_conicet_id")
```

```python3
pd.merge(pers, conicet,how="left", on = "categoria_conicet_id")
```

```python3
pd.merge(pers, conicet,how="outer", on = "categoria_conicet_id")
```

```python3
pd.merge(pers, conicet,how="inner", on = "categoria_conicet_id")
```

### **left_on, right_on**

```python3
pd.merge(pers, conicet, left_on="persona_id", right_on = "categoria_conicet_id")
```

Creá un DataFrame **pers2** que contenga las columnas de **pers** excepto la columna "categoria_conicet_id" y luego probá hacer:

```python3
pd.merge(pers2, conicet,how = "inner", left_on="persona_id", right_on = "categoria_conicet_descripcion")
```

## [pd.df.set_index]()

Mediante este método se puede definir el índice (nombre de las filas) de manera explícita.

```python3
df = pd.DataFrame({'mes': [1, 4, 7, 10], 'anio': [2012, 2014, 2013, 2014], 'venta': [55, 40, 84, 31]})

print(df)
     mes  anio  venta
0      1  2012    55
1      4  2014    40
2      7  2013    84
3     10  2014    31


print(df.set_index('anio'))
         mes  venta
anio
2012      1    55
2014      4    40
2013      7    84
2014     10    31

# Podemos crear múltiples índices
print(df.set_index(['anio', 'mes']))
            venta
anio  mes
2012  1     55
2014  4     40
2013  7     84
2014  10    31
```

## [pd.df.sort_values]()

Como su nombre lo indica, ordena los valores de un data frame. Este orden se puede hacer tanto por columnas como por filas, ascendente o descendente, y eligiendo dónde deben ir los NaN.

**axis**: por defecto es 0. Con esto elegimos si se ordenan las columnas o las filas.

**ascending**: por defecto es True, por lo que se ordena de menor a mayor. Si es False se invierte el orden.

**na_position**: por defecto es "last", por lo que todos los valores NaN se ordenan al final, pero se puede configurar como "first" para que aparezcan primero.

```python3
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})
print(df)
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F

# Ordenamos por columna 1:
print(df.sort_values(by=['col1']))
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D

# Se pueden ordenar por más de una columna a la vez:
print(df.sort_values(by=['col1', 'col2']))
  col1  col2  col3 col4
1    A     1     1    B
0    A     2     0    a
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D

# Ordenamos de forma descenciente y con los NaN al principio:
print(df.sort_values(by='col1', ascending=False, na_position='first'))
  col1  col2  col3 col4
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
```

## [pd.df.to_csv]()

Con este método podemos guardar un data frame en un archivo csv (separado por comas).

**path_or_buf**: por defecto es None, por lo que si no le damos una ruta donde debe ser guardado nos va a devolver un string. La ruta puede ser completa o relativa.

**sep**: por defecto el separador es una coma, pero igual que con la apertura, este se puede definir.

**na_rep**: es la representación de los valores NaN, que por defecto es un string vacío, "", pero también puede ser configurado.

**header**: por defecto es True, guarda el archivo con los nombres de las columnas.

**index**: idem a header. Cuando los nombres de los índices son generados automáticamente (del 0 en adelante) es mejor que este parámetro tome el valor False.


## Ejercicio
Obtener las 10 personas con mayor edad y generar un nuevo DataFrame con la información de el id de la persona, el año, su edad, el id de la categoría conicet y las producciones académicas de los últimos 4 años. Unirlo con el DataFrame **conicet** y en base a ese generar una tabla con el id de la persona y la descripción de la categoría en conicet. Luego guardar este último DataFrame en un archivo.
