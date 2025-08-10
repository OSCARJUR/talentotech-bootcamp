# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 20:44:56 2025

@author: MSI-PC
"""

#validando que sean números con el metodo isdigit() -- PRIMERA FORMA
suma = 0
while True:    
    rango_inicial = input("Digite el rango inicial para el ciclo for: ")
    rango_final = input("Digite el rango final para el ciclo for: ")

    if rango_inicial.isdigit():
        if rango_final.isdigit():
            rango_inicial = int(rango_inicial)
            rango_final = int(rango_final)
            if rango_final > rango_inicial:
                for i in range(rango_inicial, rango_final + 1):
                    if i % 3 == 0:
                        suma += i
                print(f"La suma de los multiplos de 3 entre {rango_inicial} y {rango_final} es igual a {suma}")
                break
            else:
                print("El rango final debe ser mayor que el rango inicial")
        else:
            print("Su rango final no es un número: INTENTELO DE NUEVO")
    else:
        print("Su rango inicial no es un número: INTENTELO DE NUEVO")

"""for i in range(rango_inicial, rango_final + 1):
    if i % 3 == 0:
        suma += i

print(f"La suma de los multiplos de 3 entre {rango_inicial} y {rango_final} es igual a {suma}")

#-----------------------------------------SEGUNDA FORMA-----------------------------------

"""