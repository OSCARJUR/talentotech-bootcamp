# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 20:46:24 2025

@author: MSI-PC
"""


#validando que sean enteros a traves de try...except  -- SEGUNDA FORMA
suma = 0

while True:
    try:
        rango_inicial = int(input("Digite el rango inicial para el ciclo for: "))
        rango_final = int(input("Digite el rango final para el ciclo for: "))
       
    except Exception as e:
        print(f"Error: {e}")
    else:
        if rango_final > rango_inicial:
            for i in range(rango_inicial, rango_final + 1):
                if i % 3 == 0:
                    suma += i
            print(f"La suma de los multiplos de 3 entre {rango_inicial} y {rango_final} es igual a {suma}")
            break
        else:
             print("El rango final debe ser mayor que el rango inicial")