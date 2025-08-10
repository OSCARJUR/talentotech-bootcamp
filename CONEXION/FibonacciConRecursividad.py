# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 22:30:12 2025

@author: MSI-PC
"""
# Serie de Fibonacci con recursividad
def fibonacci_recursivo(a, b, n):
    if b > n:  # Caso base: si superamos n, terminamos
        return
    print(f"La serie de Fibonacci es: {b}")
    fibonacci_recursivo(b, a + b, n)  # Llamada recursiva

# Función "wrapper" para iniciar la recursión
'''
Una función wrapper (o "envoltorio") es una función auxiliar que se usa para:
Inicializar los parámetros de la función recursiva.
Simplificar la llamada al usuario (ocultando detalles técnicos como valores iniciales).
Manejar casos especiales (como el primer término de Fibonacci, que es 0).
'''
def fibonacci(n):
    print(f"La serie de Fibonacci es: 0")  # F(0)
    fibonacci_recursivo(0, 1, n)  # Inicia con a=0, b=1
            
num=int(input("Cuantos terminos de la Serie de Fibonacci desea: "))
print(f"La serie de fibonassi de {num} es: ")

d=fibonacci(num)