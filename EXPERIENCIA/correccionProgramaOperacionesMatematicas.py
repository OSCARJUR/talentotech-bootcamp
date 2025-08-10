# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 23:49:00 2025

@author: MSI-PC
"""


import math
print()
#MENU:

print("MENU:")
print("===========================")
print("1: Sumar                (+)")
print("2: Sustraccion          (-)")
print("3: Producto             (*)")
print("4: Dividir              (/)")
print("5: Potenciacion        (**)")
print("6: Radicacio  (RaizEnesima)")
print("7: Logaritmacion      (log)")
print("8: Seno                 (S)")
print("9: Coseno              (Cs)")
print("10:Tangente          (Tan)")
print("===========================")
print()
#Ingreso de datos:
opcion=input("Ingrese la opción deseada del menú: ") 

if 1 <= int(opcion) <= 7:
    numero_uno=float(input('Ingrese el primer número de la operación:'))
    numero_dos=float(input('Ingrese el segundo número de la operación:'))
    
    if opcion==1:
      print("Vamos a sumar(+) los dos valores ingresados:")
      print('La suma es:',numero_uno+numero_dos)
    if opcion=='2':
      print("Vamos a restar(-) los dos valores ingresados:\n")
      resta=numero_uno-numero_dos
      #print("Resultado="+str(resta)) # voy a concatenar dos cadenas(str1+str2: no suma sino que junta, str1str2)
      print("Resultado=",resta) # voy a concatenar dos cadenas(str1+str2: no suma sino que junta, str1str2)
    if opcion=='3':
      print("Vamos a multiplicar(*) los dos valores ingresados:\n")
      #print(f'{numero_uno}*{numero_dos}={numero_uno*numero_dos}')
      mult=numero_uno*numero_dos
      print(f'{numero_uno}*{numero_dos}={mult}')
      #print('{}*{}'.format(numero_uno,numero_dos),"=",'{}'.format(mult))
    if opcion=='4'or opcion=='/' or opcion=='Dividir':  
        if numero_dos != 0:
            divis=numero_uno/numero_dos
            print("Vamos a dividir(/) los dos valores ingresados:\n")
            print(f'{numero_uno}/{numero_dos}={divis}')
      #VALIDANDO EL DENOMINADOR (debe ser diferente de cero)
        else:
            print("¡No es posible dividir entre cero!")
    if opcion=='5':
      print("Vamos a elevar el primer numero ingresado (numero_uno) al exponente (2do numero):")
      print(f'La potencia de elevar:{numero_uno} al exponente {numero_dos} es:{round(numero_uno**numero_dos,0)} ')
    if opcion=='6':
      '''print("Vamos a encontrar la raiz 'ENESIMA' de un numero ingresado considerando que,")
      print("el primer numero es la raiz y el segundo numero es el radicando,")
      print(f"La raiz {numero_uno} de {numero_dos} es: {numero_dos**(1/numero_uno)}")'''
      # OTRA OPCION PARA ENCONTRAR LA RAIZ ENESIMA DE UN NUMERO USANDO LA FUNCION pow(a,1/b)
      print("Vamos a encontrar la raiz 'ENESIMA' de un numero ingresado considerando que,")
      print("el primer numero es el radicando y el segundo numero es el indice")
      print(f"La raiz {numero_dos} de {numero_uno} es: {pow(numero_uno,1/numero_dos)}")
    if opcion =='7':
      print(f"Vamos a hallar el logaritmo de un numero cualquiera {numero_dos} en cualquier base {numero_uno} :")
      print(f'El logaritmo de {numero_dos} en base {numero_uno} es: {math.log(numero_dos, numero_uno)}')
      if numero_dos != 0:
          print(numero_uno/numero_dos)
      else:
          print("¡No es posible dividir entre cero!")

if 8 <= int(opcion) <= 10:
    grados=float(input("Introduzca el angulo en grados para hallar la funcion trigonometrica especifica: "))
    radianes=math.radians(grados)
    if opcion =='8':
      print(f"Vamos a hallar el seno de {grados} grados que es un angulo entre 0 y 360 grados")
      print(f'El seno de {grados} es: {math.sin(radianes)}')
    if opcion =='9':
      print(f"Vamos a hallar el coseno de {grados} grados que es un angulo entre 0 y 360 grados")
      print(f'El coseno de {grados} es: {math.cos(radianes)}')
    if opcion =='10':
      print(f"Vamos a hallar la tangente de {grados} grados que es un angulo entre 0 y 360 grados")
      print(f'la tangente de {grados} es: {math.tan(radianes)}')
if (int(opcion)<1 or int(opcion) >10):
    print("la opcion seleccionada es incorrecta.")
    

     