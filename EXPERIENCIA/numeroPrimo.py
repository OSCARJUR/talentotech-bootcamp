# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 22:02:22 2025

@author: MSI-PC
"""

n = int(input("Ingrese un número: "))

if n <= 1:
    print("No es primo")
elif n == 2 or n == 3 or n == 5 or n == 7:
    print("Es primo")
elif n % 2 == 0:
    print("No es primo")
elif n % 3 == 0:
    print("No es primo")
elif n % 5 == 0:
    print("No es primo")
elif n % 7 == 0:
    print("No es primo")
else:
    print("Es primo")