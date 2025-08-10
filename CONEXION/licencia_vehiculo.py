# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 19:40:01 2025

@author: MSI-PC
"""

tiene_licencia=True
edad=int(input("DIGITE SU EDAD: "))
vehiculo="motocicleta"
if tiene_licencia:
    if edad<21:
        if (vehiculo =="motocicleta"):
            print(f"Solo puede conducir {vehiculo} ")
        else:
            print("Usted puede conducir cualquier vehiculo19")
        
    else:
        print("Puede conducir cualquier vehiculo")
else:
    print("NO PUEDE CONDUCIR NINGUN VEHICULO. NO TIENE LICENCIA")
        