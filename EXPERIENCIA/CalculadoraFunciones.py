# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 21:12:29 2025

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
        return opcion, None, None, None


def calcular_suma(numero_uno,numero_dos):
    suma=numero_uno+numero_dos
    return suma

def calcular_resta(numero_uno,numero_dos):
    return numero_uno-numero_dos

def calcular_multiplicacion(numero_uno,numero_dos):
    return numero_uno*numero_dos

def calcular_division(numero_uno,numero_dos):
    if numero_dos != 0:
        divis=numero_uno/numero_dos
        print("Vamos a dividir(/) los dos valores ingresados:\n")
        print(f'{numero_uno}/{numero_dos}={divis}')
        #VALIDANDO EL DENOMINADOR (debe ser diferente de cero)
    else:
        print("¡No es posible dividir entre cero!")
    return numero_uno/numero_dos

def calcular_potencia(numero_uno,numero_dos):
    print("el primer numero ingresado es la base:")
    print("el segundo numero ingresado es el exponente:")
    potencia=round(numero_uno**numero_dos,0)
    return potencia

def calcular_radicacion(numero_uno,numero_dos):
    print("el primer numero sera el radicando:")
    print("el segundo numero sera el indice de la raiz:")
    #aquí uso la función pow para encontrar cualquier raiz de un numero "ENTERO"
    radicacion=pow(numero_uno,1/numero_dos)
    return radicacion


def calcular_logaritmo_base10(grados):
    #aquí uso la función logaritmo que está dentro de math
    print("se le hallara el logaritmo al numero introducido:")
    logaritmo=math.log10(grados)
    return logaritmo


def calcular_logaritmo_cualquierbase(numero_uno,numero_dos):
    #aquí uso la función logaritmo que está dentro de math
    print("el primer numero 'numero_uno'sera la base:")
    print("al segundo numero 'numero_dos' se le hallara el logaritmo:")
    logaritmo=math.log(numero_dos, numero_uno)
    return logaritmo

def calcular_seno(grados):
    #aquí uso la función seno que está dentro de math
    radianes=math.radians(grados)
    seno=math.sin(radianes)#x=numero (angulo_radianes)
    return seno


def calcular_coseno(grados):
    #aquí uso la función coseno que está dentro de math
    radianes=math.radians(grados)
    coseno=math.cos(radianes)#x=numero (angulo_radianes)
    return coseno

def calcular_tangente(grados):
    #aquí uso la función tangente que está dentro de math
    radianes=math.radians(grados)
    tangente=math.tan(radianes)
    return tangente

"""def salir():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-12): ")

        if not opcion.isdigit() or not (1 <= int(opcion) <= 12):
            print("Error: Opción no válida. Intente de nuevo.")
            continue

        opcion = int(opcion)

        # Opción 12: Salir del programa
        if opcion >= 12:
            print("\n Saliendo del programa... ¡Hasta luego! 👋")
            break  # Termina el bucle while
            """
  
  




def procesar_y_mostrar_operacion1(opcion,numero_uno,numero_dos,grados):
    if opcion==1 or opcion=='+' or opcion=='Sumar':
        print("Vamos a sumar(+) los dos valores ingresados:")
        resultado=calcular_suma(numero_uno,numero_dos)
        print('La suma es:',resultado)
        
    if opcion==2 or opcion=='-' or opcion=='Restar':
        print("Vamos a restar(-) los dos valores ingresados:\n")
        resultado=calcular_resta(numero_uno,numero_dos)    
        print("Resultado=",resultado) 
        
    if opcion== 3 or opcion=='*' or opcion=='Multiplicar':
        print("Vamos a multiplicar(*) los dos valores ingresados:\n")
        resultado=calcular_multiplicacion(numero_uno,numero_dos)    
        print("Resultado=",resultado)
        
    if opcion==4 or opcion=='/' or opcion=='Dividir':
        print("Vamos a dividir(/) los dos valores ingresados:\n")
        #VALIDANDO EL DENOMINADOR (debe ser diferente de cero)
        if numero_dos!=0:
            resultado=calcular_division(numero_uno,numero_dos)    
            print("Resultado=",resultado)      
        else:
            print("¡No es posible dividir entre cero!")
            
    if opcion==5 or opcion=='Pot' or opcion=='Potenciacion':
        print("Vamos a calcular la potencia de los valores ingresados:\n")
        resultado1=calcular_potencia(numero_uno,numero_dos)
        print("Resultado1=",resultado1)
        
    if opcion==6 or opcion=='Rad' or opcion=='Radicacion':
        print("Vamos a calcular la raiz enesima del valor ingresado:\n")
        resultado1=calcular_radicacion(numero_uno,numero_dos)
        print("Resultado1=",resultado1)
        
    if opcion==8 or opcion=='logN' or opcion=='NLogaritmo':
        print("Vamos a calcular el log de un numero entero en cualquier base:\n")
        resultado1=calcular_logaritmo_cualquierbase(numero_uno,numero_dos)
        print("Resultado1=",resultado1)
    
    #ojo
    if opcion==7 or opcion=='Logaritmo':
        print("Calculo del logaritmo en base N del valor ingresado:")  
        resultado=calcular_logaritmo_base10(grados)
        print(f'El Logaritmo de {grados} es {resultado}')
        
    if opcion==9 or opcion=='sen' or opcion=='Seno':
        print("Calculo del seno del valor ingresado:\n")
        resultado1=calcular_seno(grados)
        print("Resultado1=",resultado1)
    
   
    if opcion==10 or opcion=='Cos' or opcion=='Coseno':
        print("Vamos a calcular el coseno (Cos) del valor ingresado:\n")
        resultado1=calcular_coseno(grados)
        print("Resultado1=",resultado1) 
    
    if opcion==11 or opcion=='tan' or opcion=='Tangente':
        print("Vamos a calcular el Tangente (tan) del valor ingresad:\n")
        resultado1=calcular_tangente(grados)
        print("Resultado1=",resultado1)
        
''' if opcion==12 or opcion=='S' or opcion=='Salir':
        print("Con esta opcion saldras del programa:\n")
        resultado1=salir()
        print("Resultado1=",resultado1)
      '''

  
  
def llamar_funciones():
    mostrar_titulo()
    mostrar_menu()
    opcion,numero_uno,numero_dos,grados=ingresar_datos1()
    procesar_y_mostrar_operacion1(opcion,numero_uno,numero_dos,grados) 


#EJECUCION DEL PROGRAMA:
llamar_funciones()