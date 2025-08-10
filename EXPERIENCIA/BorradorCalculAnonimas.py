# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 23:38:57 2025

@author: MSI-PC
"""

'''
# Función Lambda para calcular el cuadrado de un número
square = lambda x: x ** 2
print(square(3)) # Resultado: 9

# Funcion tradicional para calcular el cuadrado de un numero
def square1(num):
  return num ** 2
print(square(5)) # Resultado: 25
'''

import math
print()

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
        return opcion, None, None, None



suma=lambda numero_uno,numero_dos: numero_uno+numero_dos
print(suma(3,5))
resta=lambda numero_uno,numero_dos: numero_uno-numero_dos
print(resta(3,5))
multiplicacion=lambda numero_uno,numero_dos: numero_uno*numero_dos
print(multiplicacion(3,5))
division=lambda numero_uno,numero_dos: numero_uno/numero_dos  
print(division(3,5))
potencia=lambda numero_uno,numero_dos: round(numero_uno**numero_dos,0)
print(potencia(3,5))
radicacionene=lambda numero_uno,numero_dos: pow(numero_uno,1/numero_dos)
print(radicacionene(3,5))

Logaritmacion=lambda grados: math.log10(grados)
print(Logaritmacion(3))
Logaritmacionene=lambda numero_uno,numero_dos: math.log(numero_dos, numero_uno)
print(Logaritmacionene(3,5))

#Seno=lambda grados: math.sin(grados)
Seno = lambda grados: math.sin(math.radians(grados))
print(Seno(60))
Coseno=lambda grados: math.cos(math.radians(grados))
print(Coseno(60))
Tangente=lambda grados: math.tan(math.radians(grados))
print(Tangente(60))


def procesar_y_mostrar_operacion1(opcion,numero_uno,numero_dos,grados):
    if opcion==1 or opcion=='+' or opcion=='Sumar':
        print("Vamos a sumar(+) los dos valores ingresados:")
        resultado=suma(numero_uno,numero_dos)
        print('La suma es:',resultado)
        
    if opcion==2 or opcion=='-' or opcion=='Restar':
        print("Vamos a restar(-) los dos valores ingresados:\n")
        resultado=resta(numero_uno,numero_dos)    
        print("Resultado=",resultado) 
        
    if opcion== 3 or opcion=='*' or opcion=='Multiplicar':
        print("Vamos a multiplicar(*) los dos valores ingresados:\n")
        resultado=multiplicacion(numero_uno,numero_dos)    
        print("Resultado=",resultado)
        
    if opcion==4 or opcion=='/' or opcion=='Dividir':
        print("Vamos a dividir(/) los dos valores ingresados:\n")
        #VALIDANDO EL DENOMINADOR (debe ser diferente de cero)
        if numero_dos!=0:
            resultado=division(numero_uno,numero_dos)    
            print("Resultado=",resultado)      
        else:
            print("¡No es posible dividir entre cero!")
            
    if opcion==5 or opcion=='Pot' or opcion=='Potenciacion':
        print("Vamos a calcular la potencia de los valores ingresados:\n")
        resultado1=potencia(numero_uno,numero_dos)
        print("Resultado1=",resultado1)
        
    if opcion==6 or opcion=='Rad' or opcion=='Radicacion':
        print("Vamos a calcular la raiz enesima del valor ingresado:\n")
        resultado1=radicacionene(numero_uno,numero_dos)
        print("Resultado1=",resultado1)
        
    if opcion==8 or opcion=='logN' or opcion=='NLogaritmo':
        print("Vamos a calcular el log de un numero entero en cualquier base:\n")
        resultado1=Logaritmacionene(numero_uno,numero_dos)
        print("Resultado1=",resultado1)
    
    #ojo
    if opcion==7 or opcion=='Logaritmo':
        print("Calculo del logaritmo en base N del valor ingresado:")  
        resultado=Logaritmacion(grados)
        print(f'El Logaritmo de {grados} es {resultado}')
        
    if opcion==9 or opcion=='sen' or opcion=='Seno':
        print("Calculo del seno del valor ingresado:\n")
        resultado1=Seno(grados)
        print("Resultado1=",resultado1)
    
   
    if opcion==10 or opcion=='Cos' or opcion=='Coseno':
        print("Vamos a calcular el coseno (Cos) del valor ingresado:\n")
        resultado1=Coseno(grados)
        print("Resultado1=",resultado1) 
    
    if opcion==11 or opcion=='tan' or opcion=='Tangente':
        print("Vamos a calcular el Tangente (tan) del valor ingresad:\n")
        resultado1=Tangente(grados)
        print("Resultado1=",resultado1)
        
 
  
'''def llamar_funciones():
    mostrar_titulo()
    mostrar_menu()
    opcion,numero_uno,numero_dos,grados=ingresar_datos1()
    procesar_y_mostrar_operacion1(opcion,numero_uno,numero_dos,grados) 


#EJECUCION DEL PROGRAMA:
llamar_funciones()   '''

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
        opcion,numero_uno, numero_dos, grados = ingresar_datos1()
        procesar_y_mostrar_operacion1(opcion, numero_uno, numero_dos, grados)

# EJECUCIÓN DEL PROGRAMA:
main()
