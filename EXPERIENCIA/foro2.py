# -*- coding: utf-8 -*-
"""
Created on Mon May 19 01:19:18 2025

@author: MSI-PC
"""
'''
2.	De acuerdo a un promedio de calificaciones indicar si un alumno esta aprobado o hay error en el promedio
'''

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
if prome==3.0:
    print(f"{nombre}, usted ha APROBADO con la nota minima ")
elif prome<3.0:
    print(f"{nombre}, usted ha REPROBADO la asignatura ")
else:
    print(f"{nombre}, usted ha APROBADO con buenas calificaciones ")

print("Fin del programa")