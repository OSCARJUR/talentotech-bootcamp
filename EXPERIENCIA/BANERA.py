# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 19:17:00 2025

@author: MSI-PC
"""

# Declaracion de variables
Cap_Max=500
Llenado_hora=200
Vol_persona=200
Hras_llenado=1
if (Llenado_hora*Hras_llenado)>Cap_Max:
    print("LA BANERA SE REBOSO EN EL TIEMPO DE LLENADO")
elif ((Llenado_hora*Hras_llenado)+Vol_persona>Cap_Max):
    print("LA BANERA SE REBOSO EN EL TIEMPO DE LLENADO Y EL INGRESO DE LA PERSONA")
elif ((Llenado_hora*Hras_llenado)+Vol_persona)==Cap_Max: 
    print("LA BANERA ESTA EN SU CAPACIDAD MAXIMA")
elif (Llenado_hora+Vol_persona)<=Cap_Max:
        print("LA BANERA NO SE HA REBOSADO, PUEDE INGRESAR ")
else: 
    print("OPCION INVALIDA")
