# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 18:41:34 2025

@author: MSI-PC
"""

#MENU
print("************************")
print("* ******  MENU  ****** *")
print("************************")
print("[1]. Calculos")
print("[2]. Graficas")
print("[3]. Imagenes")
print("")

opcion=0
intento=0
while opcion<1 or opcion >3:  #0<= opcion <3
    opcion=input("Selecione una opcion: ")
    try:
        opcion=int(opcion)
    except ValueError:
        opcion=0
    intento+=1
    if intento >=5:
        print("HAZ SUPERADO EL NUMERO DE INTENTOS PERMITIDOS")
        break
    else:
        print(f"Seleccionaste la opcion {opcion}")
        