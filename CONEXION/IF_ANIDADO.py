# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 20:24:24 2025

@author: MSI-PC
EJERCICIO 4 IF ANIDADO
"""

#tiene_invitacion=input("DIGITE SI SI LA TIENE O NO SI NO LA TIENE: ")
tiene_invitacion=False #cambie entre False y True para probar
edad=int(input("DIGITE SU EDAD: "))
acompanado_por_adulto=True

if tiene_invitacion:
    if edad>=18:
        print("USTED SI PUEDE ENTRAR AL CLUB")
    elif(acompanado_por_adulto):
        print("AHORA YA PUEDE ENTRAR AL CLUB")
else:
    print("USTED NO CUMPLE CON LOS REQUISITOS PARA ENTRAR AL CLUB")
        