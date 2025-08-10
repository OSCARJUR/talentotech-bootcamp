# -*- coding: utf-8 -*-
"""
Created on Mon May 19 00:06:37 2025

@author: MSI-PC
"""
'''
FORO 4: ALGORITMOS DE DECISION SIMPLE.
Pedir un numero  e indicar si es positivo o negativo.
Sumar dos números siempre que no sean iguales, de ser asi indicarlo.
'''
num=float(input('Introduzca un numero: '))
if (num>0):
    print('El numero introducido es "POSITIVO"')
elif (num==0):
    print('El numero introducido es "CERO"')
else:
    print('El numero introducido es "NEGATIVO"')
print("Fin del programa")