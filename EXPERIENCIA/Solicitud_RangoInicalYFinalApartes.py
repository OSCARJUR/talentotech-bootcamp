# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 22:28:52 2025

@author: MSI-PC
"""

suma = 0

# Solicitar rango_inicial una sola vez y validarlo
while True:
    try:
        rango_inicial = int(input("Digite el rango inicial para el ciclo for: "))
        break  # Si no hay error, salimos del bucle
    except ValueError as e:
        print(f"Error: Debe ingresar un número entero válido. Intente nuevamente.")

# Solicitar rango_final y validarlo por separado
while True:
    try:
        rango_final = int(input("Digite el rango final para el ciclo for: "))
        
        # Validar que el rango final sea mayor que el inicial
        if rango_final <= rango_inicial:
            print("El rango final debe ser mayor que el rango inicial. Intente nuevamente.")
            continue  # Vuelve a solicitar solo el rango_final
            
        # Si todo está bien, realizar el cálculo
        for i in range(rango_inicial, rango_final + 1):
            if i % 3 == 0:
                suma += i
        print(f"La suma de los múltiplos de 3 entre {rango_inicial} y {rango_final} es igual a {suma}")
        break
        
    except ValueError as e:
        print(f"Error: Debe ingresar un número entero válido para el rango final. Intente nuevamente.")