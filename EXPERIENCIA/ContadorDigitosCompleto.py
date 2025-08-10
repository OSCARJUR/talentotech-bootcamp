# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 21:25:13 2025

@author: MSI-PC
"""

while True:
    try:
        numero = int(input("Digite un número entero positivo: "))
    except ValueError:
        print("Error: Debe ingresar un número entero válido. Intente nuevamente.")
    else:
        if numero > 0:
            contador = 0
            n = numero

            while n > 0:
                n = n // 10
                contador += 1

            print(f"El número {numero} tiene {contador} dígitos")
            break
        else:
            print("Error: El número debe ser positivo. Intente nuevamente.")