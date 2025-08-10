# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 19:53:27 2025

@author: MSI-PC
"""

#a=0
#b=0
while True:
    a=input("Introduzca  el primer numero: ")
    b=input("Introduzca  el segundo numero: ")
    try:
        a=float(a)
        b=float(b)
        division= round((a/b),2)
        #break
    except ValueError:
        print("ERROR DEBES INTRODUCIR NUMEROS")
        print()
        continue
    except ZeroDivisionError:
        print("ERROR RECUERDA QUE LA DIVISION ENTRE '0' NO EXISTE")
        print()
        continue
    except:
       print("ERROR DESCONOCIDO")
       print()
       exit()
    else:
       print(f"{a} / {b} = {division}")
       break
    finally:
        print("EXCELENTE")