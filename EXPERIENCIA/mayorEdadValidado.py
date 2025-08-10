# -*- coding: utf-8 -*-
"""
Created on Fri May 23 00:15:58 2025

@author: MSI-PC
"""

# Validar edad (solo números enteros positivos)
while True:
    edad = input("Ingresa tu edad: ")
    if edad.isdigit():  # Verifica si es un número entero positivo
        edad = int(edad)
        break  # Sale del bucle si la edad es válida
    else:
        print("Error: Debes ingresar un número entero positivo. Intenta de nuevo.")

# Determinar si es mayor o menor de edad
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")