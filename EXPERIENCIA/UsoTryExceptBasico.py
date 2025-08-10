# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 18:31:51 2025

@author: MSI-PC
""
# PRIMERA OPCION Sin usar try-except se produce un error 
num1 = int(input("Introduzca un numero: "))
num2 = int(input("Introduzca otro numero: "))
resultado = num1 + num2
print(resultado)

# SEGUNDA OPCION Usando try -except sin ciclo
try:
    num1 = int(input("Introduzca un numero: "))
    num2 = int(input("Introduzca otro numero: "))
    resultado = num1 + num2
    print(resultado)
except:
    print("Debes introducir numeros, vuelve a intertarlo")
finally:
    print("Esta es la ultima linea a ejecutar")
"""
# TERCERA OPCION Usando try -except dentro de un ciclo
while (True):
    try:
        num1 = int(input("Introduzca un numero: "))
        num2 = int(input("Introduzca otro numero: "))
        resultado = num1 + num2
        print(resultado)
        break
    except:
        print("Debes introducir numeros, vuelve a intertarlo")
    finally:
        print("Esta es la ultima linea a ejecutar")