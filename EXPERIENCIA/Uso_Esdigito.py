# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 19:13:56 2025

@author: MSI-PC
"""
#Para trabajar ciclos infinitos hasta que se cumpla lo que quiero
suma=0
while True:
    rango_inic=input("digite el rango inicial para el ciclo for: ")
    rango_fin=input("digite el rango final para el ciclo for: ")
    if rango_inic.isdigit():
        if rango_fin.isdigit():
            rango_inic=int(rango_inic)
            rango_fin=int(rango_fin)
            if rango_fin>rango_inic:
                break
            else:
                print("El rango final debe ser mayor al rango inicial")
        else:
            print("Su rango final no es un numero. Intentelo de nuevo")
    else:
        print("Su rango inicial no es un numero. Intentelo de nuevo")
for i in range(rango_inic,rango_fin+1):
    if i % 3 ==0:
        suma=0
print(f"La suma de los multiples de 3 entre {rango_inic} y {rango_fin} es igual a la {suma} ")
        
        
    