# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 23:44:35 2025

@author: MSI-PC
"""

# DISENO DE UNA CALCULADORA CON FUNCIONES 
import math
print()
#MENU:

def mostrar_titulo():
    print('Ejemplo Calculadora Sencilla (+,-,*,/) por Oscar R. Jurado:')
    

def mostrar_menu():
    print()
    print("MENU:")
    print("=============================")
    print("1: Suma                   (+)")
    print("2: Resta                  (-)")
    print("3: Multiplicacion         (*)")
    print("4: Division               (/)")
    print("5: Potenciacion          (**)")
    print("6: Radicacion   (RaizEnesima)")
    print("7: Logaritmacion        (log)")
    print("8: Logaritmacion baseN (logN)")
    print("9: Seno                   (S)")
    print("10:Coseno                (Cs)")
    print("11:Tangente             (Tan)")
    print("12:Salir                  (S)")
    print("=============================")
    print()
    
  

def ingresar_datos1():
    opcion = int(input("Qué opción deseada: ")) 
    if 1 <= opcion <= 6 or opcion == 8:
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        return opcion, num1, num2, None
    elif opcion in [7, 9, 10, 11]:
        grados = float(input('Ingrese el ángulo en grados: '))
        return opcion, None, None, grados
    else:
        if opcion >= 12:
            return opcion, None, None, None





    

def calcular_suma(numero_uno,numero_dos):
    suma=numero_uno+numero_dos
    return suma

def calcular_resta(numero_uno,numero_dos):
    return numero_uno-numero_dos

def calcular_seno(grados):
    #aquí uso la función seno que está dentro de math
    radianes=math.radians(grados)
    seno=math.sin(radianes)#x=numero (angulo_radianes)
    return seno



def procesar_y_mostrar_operacion1(opcion,numero_uno,numero_dos,grados):
    if opcion==1 or opcion=='+' or opcion=='Sumar':
        print("Vamos a sumar(+) los dos valores ingresados:")
        resultado=calcular_suma(numero_uno,numero_dos)
        print('La suma es:',resultado)
    if opcion==2 or opcion=='-' or opcion=='Restar':
        print("Vamos a restar(-) los dos valores ingresados:\n")
        resultado=calcular_resta(numero_uno,numero_dos)    
        print("Resultado=",resultado) 
    if opcion==9 or opcion=='sen' or opcion=='Seno':
        print("Calculo del seno del valor ingresado:\n")
        resultado1=calcular_seno(grados)
        print("Resultado1=",resultado1)
"""        
def salir():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-12): ")

        if not opcion.isdigit() or not (1 <= int(opcion) <= 12):
            print("Error: Opción no válida. Intente de nuevo.")
            continue

        opcion = int(opcion)

        # Opción 12: Salir del programa
        if opcion == 12:
            print("\n Saliendo del programa... ¡Hasta luego! 👋")
            break  # Termina el bucle while
          




def llamar_funciones():
  mostrar_titulo()
  mostrar_menu()
  opcion,numero_uno,numero_dos,grados=ingresar_datos1()
  procesar_y_mostrar_operacion1(opcion,numero_uno,numero_dos,grados) 
  salir()

#EJECUCION DEL PROGRAMA:
llamar_funciones()
"""

def main():
    mostrar_titulo()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-12): ")
        if not opcion.isdigit() or not (1 <= int(opcion) <= 12):
            print("Error: Opción no válida. Intente de nuevo.")
            continue
        opcion = int(opcion)
        if opcion == 12:
            print("\nSaliendo del programa... ¡Hasta luego! 👋")
            break
        numero_uno, numero_dos, grados = ingresar_datos1(opcion)
        procesar_y_mostrar_operacion1(opcion, numero_uno, numero_dos, grados)

# EJECUCIÓN DEL PROGRAMA:
main()
