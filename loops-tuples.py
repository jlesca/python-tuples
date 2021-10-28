# LOOPS A TRAVES DE UNA TUPLA
# Podemos crear un bucle de funciones con los elementos de nuesrta tupla.
# Debemos crear una variable que almacene el valor de cada elemento de la tupla.

print('LOOPS A TRAVÉS DE UNA TUPLA') # Muestro titulo
colors = ('red', 'green', 'blue') # Creo la tupla y sus elementos
for item in colors: # Creo mediante for una variable llamada 'item' que toma los valores de los elementos de 'colors'
  print(item): # Muestro el valor de la var 'item' para cada elemento de la tupla 'colors'
    

# METODO ABREVIADO
print('METODO ABREVIADO') # Muestro tìtulo
colors = ['red', 'green', 'blue'] # Creo la variable y sus elementos.
[print(item) for item in colors] # Entre [llaves] indicamos que muestre la variable 'item' asignandole el valor de cada elemento de la lista 'colors'.


# BUCLES MEDIANTE LA FUNCIÓN WHILE
# Podemos hacer bucles usando la función LEN() para indicar que inicie desde la posición 0 (cero) 
# y avance por cada elemento de la tupla hasta llegar al final de su longitud.

colors = ('red', 'green', 'blue', 'yellow', 'pink', 'brown') # Creo la variable y sus elementos.
item = 0 # Creo la variable 'item' y le asigno el valor 0 
while item < len(colors): # Le digo que mientras la variable 'item' sea menor a la longitud, 6 en este caso, haga lo siguiente:
  print(colors[item]) # Muestre el valor de la variable item, el cual tomará el valor de cada elemento.
  item = item + 1 # Incremento el valor de la variable en +1 para que avance en la lista de elementos.
  
