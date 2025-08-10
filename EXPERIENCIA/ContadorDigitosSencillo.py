# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 21:15:12 2025

@author: MSI-PC
"""

numero = int(input("Digite un número entero positivo: "))

contador = 0

n = numero

while n > 0:
    n = n//10
    contador += 1

print(f"El número {numero} tiene {contador} digitos")
