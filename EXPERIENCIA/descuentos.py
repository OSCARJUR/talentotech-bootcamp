# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 19:47:23 2025

@author: MSI-PC
"""

membresia_activa=True
edad=int(input("DIGITE SU EDAD: "))

if membresia_activa:
    if edad<18:
        print("Usted tiene un descuento del 10%")
    elif (edad>=18 and edad<=60):
        print("Usted tiene un descuento del 20%")
    else:
        print("Usted tiene un descuento del 30%")
else:
    print("NO HAY DESCUENTOS PARA USTED.pues no tiene membresia")
        

