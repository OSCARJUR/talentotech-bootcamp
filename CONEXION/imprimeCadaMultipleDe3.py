# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 19:41:06 2025

@author: MSI-PC
"""

#Validar que sean enteros a traves de try...except
suma=0
while True:
    try:
        rango_inic=int(input("digite el rango inicial para el ciclo for: "))
        rango_fin=int(input("digite el rango final para el ciclo for: "))
    except Exception as e:
        print("Error")
    else:
        if rango_fin>rango_inic:
            for i in range(rango_inic,rango_fin+1):
                if i % 3 ==0:
                    suma += i
                    print(f"Los multiplos de 3 son: {i}")
            print(f"La suma de los multiples de 3 entre {rango_inic} y {rango_fin} es igual a la {suma} ")
            break        
        else:
            print("El rango final debe ser mayor al rango inicial")

    
    