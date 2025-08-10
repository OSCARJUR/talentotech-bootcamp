# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 20:55:28 2025

@author: MSI-PC
"""
# Calculo del factorial de un numero sin recursividad
def factorial_Sin_Recursidad(n):
    resultado = 1
    for i in range(1, n + 1):  # Desde 1 hasta n
        resultado *= i
    return resultado

# LLAMADA ELEGANTE
numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es: {factorial_Sin_Recursidad(numero)}")

# LLAMADA SENCILLA DE LA FUNCION
a=factorial_Sin_Recursidad(5)
print(a)

# **********************************************************************

# Calculo del factorial de un numero con recursividad

print()
print("Factorial con recursividad")
print()

def factorial_Con_Recursidad(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial_Con_Recursidad(n - 1)  # Llamada recursiva

# LLAMADA SENCILLA DE LA FUNCION
a=factorial_Con_Recursidad(4)
print(a)

# LLAMADA ELEGANTE
numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es: {factorial_Con_Recursidad(numero)}")