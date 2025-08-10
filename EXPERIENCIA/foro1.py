# -*- coding: utf-8 -*-
"""
Created on Sun May 18 23:19:20 2025

@author: MSI-PC
"""

"""
FORO 3 - EJERCICIOS ALGORITMOS SECUENCIALES
Estimados campistas,
Bienvenidos a este espacio donde encontraran dos ejercicios para desarrollar con respecto al tema de algoritmos secuenciales
1. Obtener el nombre y la edad de una persona y mostrarlas en pantalla
2. Mostrar la suma y el promedio de tres calificaciones que ingrese un alumno

"""
# ENTRADA
nombre=input('digita tu nombre por favor: ')
cal1=float(input('Introduzca su primera calificacion: '))
cal2=float(input('Introduzca su segunda calificacion: '))
cal3=float(input('Introduzca su tercera calificacion: '))

# PROCESO
sum=cal1+cal2+cal3
prome=sum/3
prome=round(prome,2)
# SALIDA
print(f"{nombre}, la suma de tus notas es {sum} y el promedio de tus calificaciones es {prome} ")
