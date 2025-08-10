# -*- coding: utf-8 -*-
"""
Created on Mon May 19 01:02:45 2025

@author: MSI-PC
"""
'''
Sumar dos números siempre que no sean iguales, de ser asi indicarlo.
'''

# ENTRADA
num1=int(input('introduzca primer numero: '))
num2=int(input('introduzca segundo numero: '))

# PROCESO Y SALIDA
if num1!=num2:
    sum=num1+num2
    print(f"El numero {num1} es diferente del numero {num2} ")
    print(f'La suma de los dos numeros es {sum}')
else:
    print(f"El numero {num1} es igual al numero {num2} ")
print("Fin del programa")