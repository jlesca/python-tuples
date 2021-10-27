# DESEMPAQUETAR TUPLAS
# Cuando creamos una tupla y asignamos sus elementos, lo llamamos empaquetar una tupla.
# Python nos permite desempaquetarlas creando variables para cada elemento de la tupla.
# El nùmero de variables debe coincidir con la cantidad de elementos de la tupla.

print('DESEMPAQUETAR TUPLAS') # Muestro el tìtulo.
colors = ('red', 'green', 'blue') # Creo la tupla y asigno sus elementos.
(a, b, c,) = colors # Asigno variables para cada elemento de la tupla 'colors'
print(a) # Muestro la variable 'a'. En este caso serà 'red'
print(b) # Muestro la variable 'b'. En este caso serà 'green'
print(c) # Muestro la variable 'c'. En este caso serà 'blue'


# DESEMPAQUETAR USANDO ASTERISCOS
# Si el nùmero de varialbes es menor a la cantidad de elementos, podemos agrear un asterìsco en la ùltima variable.

print('DESEMPAQUETAR USANDO ASTERISCO') # Muestro tìtulo
colors = ('red', 'green', 'blue', 'yellow', 'black', 'white') # Creo la tupla y asigno sus elementos.
(a, b, *c) = colors # Creo las variables para cada elemento y la ùltima le antepongo un * (asterìsco).
print(a) # Muestro la variable 'a'. En este caso serà 'red'
print(b) # Muestro la variable 'b'. En este caso serà 'green'
print(c) # Muestro la variable 'c'. En este caso serà 'blue, 'yellow', 'black', 'white')  

# Si anteponemos asterìsco a otra variable, Python le asignarà los elementos hasta coincidir con las variables restantes.

  (a, b, *c) = colors # Creo las variables para cada elemento y la ùltima le antepongo un * (asterìsco).
print(a) # Muestro la variable 'a'. En este caso serà 'red'
print(b) # Muestro la variable 'b'. En este caso serà 'green', 'blue', 'yellow', 'black'
print(c) # Muestro la variable 'c'. En este caso serà 'white'
