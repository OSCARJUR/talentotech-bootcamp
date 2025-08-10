# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 21:25:51 2025

@author: MSI-PC


cadena=input() #solicita al usuario la cadena a convertir
print(cadena.lower())#.lover es una funcion de python que permite convertir la cadena a minusculas
"""
print('Ejemplo Calculadora Sencilla (+,-,*,/) por Felipe Escallón:')
'''
ESTO ES UN COMENTARIO MULTILINEA
print('Ejemplo Calculadora Sencilla (+,-,*,/,**,sqrt,log) por Felipe Escallón:\n')
PODEMOS DESCOMENTAR Y PROBAR EL print ANTERIOR
'''
import math
print()
#MENU:
print("MENU:")
print("1: Sumar")
#print("1: +")
print("2: -")
print("3: *")
print("4: Dividir (/)")
print("5: Potenciacion (**)")
print("6: Radicacion (sqrt)")
print("7: Logaritmacion (log)")
print("8: Seno (S)")
print("9: Coseno (Cs)")
print("10: Tangente (Tan)")

print()
#Ingreso de datos:
opcion=input("Ingrese la opción deseada del menú: ") # la opción se guarda como cadena
#opcion=int(input("Ingrese la opción deseada del menú: ")) # la opción se guarda como cadena
numero_uno=float(input('Ingrese el primer número de la operación:'))# guarda como flotante (número real)
numero_dos=float(input('Ingrese el segundo número de la operación:'))# guarda como flotante (número real)
#Posibilidades para ejecutar la calculadora:
#if opcion=='1':
#if opcion=='+':
#if opcion=='Sumar':
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
  print("Vamos a dividir(/) los dos valores ingresados:\n")
  #VALIDANDO EL DENOMINADOR (debe ser diferente de cero)
if opcion=='5':
  print("Vamos a elevar el primer numero ingresado (numero_uno) al exponente (2do numero):")
  print(f'La potencia de elevar:{numero_uno} al exponente {numero_dos} es:{round(numero_uno**numero_dos,0)} ')
if opcion=='6':
  '''print("Vamos a encontrar la raiz 'ENESIMA' de un numero ingresado considerando que,")
  print("el primer numero es la raiz y el segundo numero es el radicando,")
  print(f"La raiz {numero_uno} de {numero_dos} es: {numero_dos**(1/numero_uno)}")'''
  # OTRA OPCION PARA ENCONTRAR LA RAIZ ENESIMA DE UN NUMERO USANDO LA FUNCION pow(a,1/b)
  print("Vamos a encontrar la raiz 'ENESIMA' de un numero ingresado considerando que,")
  print("el primer numero es el radical y el segundo numero es el inverso de la raiz")
  print(f"La raiz {numero_dos} de {numero_uno} es: {round(pow(numero_uno,1/numero_dos),1)}")
if opcion =='7':
  print(f"Vamos a hallar el logaritmo de un numero cualquiera {numero_dos} en cualquier base {numero_uno} :")
  print(f'El logaritmo de {numero_dos} en base {numero_uno} es: {math.log(numero_dos, numero_uno)}')
if opcion =='8':
  print(f"Vamos a hallar el logaritmo de un numero cualquiera {numero_dos} en cualquier base {numero_uno} :")
  print(f'El logaritmo de {numero_dos} en base {numero_uno} es: {math.log(numero_dos, numero_uno)}')
if opcion =='9':
  print(f"Vamos a hallar el logaritmo de un numero cualquiera {numero_dos} en cualquier base {numero_uno} :")
  print(f'El logaritmo de {numero_dos} en base {numero_uno} es: {math.log(numero_dos, numero_uno)}')
if opcion =='10':
  print(f"Vamos a hallar el logaritmo de un numero cualquiera {numero_dos} en cualquier base {numero_uno} :")
  print(f'El logaritmo de {numero_dos} en base {numero_uno} es: {math.log(numero_dos, numero_uno)}')


if numero_dos != 0:
    
    print(numero_uno/numero_dos)
else:
    print("¡No es posible dividir entre cero!")
     
"""Ejemplo Calculadora Sencilla (+,-,*,/) por Felipe Escallón:

MENU:
1: Sumar
2: -
3: *
4: Dividir (/)

Ingrese la opción deseada del menú: /
Ingrese el primer número de la operación:100
Ingrese el segundo número de la operación:2
Vamos a dividir(/) los dos valores ingresados:
"""