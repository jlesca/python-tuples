# ACCEDER A UNA TUPLA
# Podemos acceder a los items de una tupla, haciendo referencia a su posición.
# El primer item de una tupla tendrá siempre la posición 0 (Cero).

print('ACCESS TUPLE ITEMS')
colors = ('red', 'green', 'blue') # Creo la variable con sus items.
print(colors[1]) # Mostrará el item con la posición 1. En este caso será 'green'.

# También podemos encontrar los items por su posición negativa.
# La posición -1 será siempre el último item de nuestra lista. 


# RANGO DE ITEMS EN UNA TUPLA
# Python nos permite acceder un rango de items dentro de una tupla.
# Debemos especificar desde donde comienza y donde termina nuestro rango.

print('RANGE OF INDEXES')
colors = ('red','green','blue', 'yellow', 'black', 'white')
print(colors[2:5]) # Le pido que imprima el rango comenzando por la posición 2 y termine en la posición 5 (pero no incluida).
                   # Esto va imprimir desde blue hasta black.
  
# Si no completamos el segundo campo, entonces la función entiende que debe tomar hasta el último valor.
print(colors[2:]) # Esto va imprimir desde blue, hasta white.


# EXISTENCIA DE UN ITEM EN UNA TUPLA
# Podemos verificar la existencia de un valor específico dentro de una tupla.
# Esto se realiza mediante la keyword IN.

print('CHECK IF EXIST BLACK')
colors = ('red','green','blue', 'yellow', 'black', 'white')
if 'black' in colors:
  print('Yes, Black exist in the tuple')
