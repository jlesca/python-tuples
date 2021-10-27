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
