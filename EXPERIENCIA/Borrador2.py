# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 18:44:00 2025

@author: MSI-PC
"""

'''
Creen una lista con al menos cinco elementos.
Modifiquen un elemento. []
Agreguen dos nuevos elementos. (.append)
Eliminen un elemento. (.remove)
Capture un elemento con (.pop)
'''
import math 
#LISTA HETEROGENEA
tarea=["casa",2, math.sqrt(8),complex(2),True]
print(tarea)

tarea[2]=1000
print(tarea)

tarea.append("finca")
tarea.append("rio")
print(tarea)

tarea.remove(True)
print(tarea)

a=tarea.pop(0)
print(tarea)

tarea.extend(["volcan",2500])
print(tarea)
