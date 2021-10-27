# TUPLAS EN PYTHON
# En las tuplas muchas funciones y métodos se asemejan a las usadas en las listas.
# La gran diferencia, es que una tupla se declara con el uso de (parentesis).

# CREANDO UNA TUPLA
print('CREANDO UNA TUPLA') # Muestro el título.
colors = ('red', 'green', 'blue') # Creo la var y sus items.
print(colors) # Muestro la var.


# LONGITUD DE UNA TUPLA
# Para saber la cantidad de items que contiene una tupla, lo hacemos mediante la función LEN()

print('LONGITUD DE UNA TUPLA') # Muestro título.
print(len(colors)) # Muestro la longitud de la var. En este caso será 3.


# CREAR UNA TUPLA CON SOLO UN ITEM
# Para crear una tupla con un solo item, debemos agregar al final del mismo una coma.

colors = ('red',)
print(colors)


# TIPOS DE DATOS EN UNA TUPLA
# Las tuplas pueden almacenar cualquier tipo de datos en Python. Int, float, str, boolean, complex.

mytuple = ('hello', 35, True, 2.5)
print(type(mytuple))
