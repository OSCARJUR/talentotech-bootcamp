# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 18:13:36 2025

@author: MSI-PC
"""

Listas_frutas=["manzana","mango","naranja","sandia","pera"]
print(Listas_frutas)

print(Listas_frutas[2])
print(Listas_frutas[4])

print(Listas_frutas[-1])
print(Listas_frutas[-2])

Listas_frutas.append("uva") #adiciona un nuevo elemento a la lista
print(Listas_frutas)

Listas_frutas.insert(2, "melon") #insertar un nuevo elemento en la posicion 2
print(Listas_frutas)

Listas_frutas.remove("sandia") # Eliminar un elemento de la lista
print(Listas_frutas)

'''fruta=Listas_frutas[1]
print(fruta)
Listas_frutas.remove("mango")
print(Listas_frutas)'''

fruta2=Listas_frutas.pop() # quita el ultimo elemento de la lista
print(fruta2)
print(Listas_frutas)
print(len(Listas_frutas))





