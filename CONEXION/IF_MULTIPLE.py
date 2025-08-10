# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 20:11:40 2025

@author: MSI-PC
EJERCICIO 3 IF MULTIPLE
"""

sueldo=int(input("DIGITE EL SUELDO QUE USTED GANA: "))
if sueldo<1000000:
    print("***** SU SUELDO ESTA EN EL MENOR RANGO *****")
elif(sueldo>=1000000 and sueldo<=2000000):
    print("**** SU SUELDO ESTA EN El RANGO 2 ****")
elif(sueldo>2000000 and sueldo<=3000000):
    print("**** SU SUELDO ESTA EN El RANGO 3 ****")
elif(sueldo>3000000 and sueldo<=4000000):
    print("**** SU SUELDO ESTA EN El RANGO 4 ****")
else:
    print("**** SU SUELDO ESTA EN El MEJOR RANGO ****")