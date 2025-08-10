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
if (prome>=3.0) and (prome<5.0):
    print(f"{nombre}, Usted aprobó el curso con un  puntaje de ",prome)
elif (prome>0.0) and (prome<3.0):
    print(f"{nombre}, usted ha REPROBADO la asignatura ")
else:
    print(f"{nombre}, Hay algun error en los calculos ")

print("Fin del programa")