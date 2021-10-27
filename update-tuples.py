# ACTUALIZAR UNA TUPLA
# Las tuplas tienen la característica de ser inmmutable, no pueden ser modificadas ni alteradas.
# No podríamos cambiar un item por otro, o agregar un item , como en el caso de la listas.
# Pero podemos hacerlo mediante la alternativa de convertir una tupla en una lista.
# Nos permitirá hacer los cambios y volver a convertir en tupla.

print('CAMBIAR UN ITEM POR OTRO') # Muestro título
colors = ('red', 'green', 'blue', 'yellow', 'pink') # Creo la var y sus items
print(colors) # Muestro la var

colors = list(colors) # Convierto la var de tupla a lista.
colors[1] = 'white' # Modifico la posición 1, en este caso 'green' por 'white'.
colors = tuple(colors) # Convierto nuevamente la var de lista a tupla.

print(colors) # Muestro la var actualizada.


# AGREGAR UN ITEM A UNA TUPLA
# Como vimos las tuplas no pueden modificarse ni ser alteradas.
# Por eso para agregar un elemento a una tupla existente, debemos convertirla en una lista para poder modificarla.
# Una vez que agregamos el o los items, podremos reconvertirla en tupla.

print('AGREGAR UN ITEM A LA TUPLA') # Muestro tìtulo.
colors = ('red', 'green', 'blue') # Creo la tupla y sus items.
print(colors) # Muestri la tupla.
colors = list(colors) # Convierto la tupla en una lista.
colors.append('yellow') # Agrego el item 'yellow' a la lista, mediante append()
colors = tuple(colors) # Vuelvo a convertir la lista en una tupla.
print(colors) # Muetro la tupla actualizada.


# ELIMINAR UN ITEM DE LA TUPLA
# Del mismo modo podemos proceder para eliminar un elemento.

print('ELIMINAR UN ITEM DE LA TUPLA') # Muestro tìtulo.
colors = ('red', 'green', 'blue') # Creo la tupla y sus items.
print(colors) # Muestri la tupla.
colors = list(colors) # Convierto la tupla en una lista.
colors.remove('green') # Elimino el item 'green' a la lista, mediante remove()
colors = tuple(colors) # Vuelvo a convertir la lista en una tupla.
print(colors) # Muetro la tupla actualizada.

input() # Salgo del programa.
