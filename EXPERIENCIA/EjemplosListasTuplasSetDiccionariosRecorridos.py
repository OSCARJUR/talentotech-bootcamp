# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 21:20:33 2025

@author: MSI-PC
"""

# EJEMPLOS DE LISTAS Y RECORRIDOS
frutas = ["manzana", "banana", "naranja", "kiwi", "mango"]

# Lista 2: Números pares (enteros)
numeros = [2, 4, 6, 8, 10]

# Lista 3: Datos mixtos (heterogénea)
mezcla = [True, 3.14, "Python", (1, 2), {"clave": "valor"}]

# RECORRIDO DE LISTAS CON CICLOS FOR


frutas = ["manzana", "banana", "naranja", "kiwi", "mango"]
print("**** Frutas ****")
for fruta in frutas:
    print(fruta.upper())  # Convertir a mayúsculas

numeros = [2, 4, 6, 8, 10]
print("\n**** Números ****")
for num in numeros:
    print(num ** 2)  # Imprimir el cuadrado de cada número
    
    
mezcla = [True, 3.14, "Python", (1, 2), {"clave": "valor"}]
print("\n**** Mixta ****")
for elemento in mezcla:
    print(f"Valor: {elemento} \t Tipo: {type(elemento)}")

#*********************************
print()
print("*************************************************")
#Tupla 1
datos = (40.4168, -3.7038, "Madrid", 28001, "España")

# Tupla 2:
producto = ("Laptop", 999.99, True, ["Intel i7", "16GB RAM"], (2024, "Marzo"))

for elemento in datos:
    print(f"{elemento}")

print("\n*** Producto ***")
for i in producto:
    print(f" {i}")
    

print()
print("*************************************************")

paises_sudamerica = {"Argentina", "Brasil", "Chile", "Colombia", "Perú"}
paises_caribe = {"Cuba", "República Dominicana", "Colombia", "Jamaica", "Brasil"}

print(f"Sudamérica: {paises_sudamerica}")
print(f"Caribe: {paises_caribe}")
print("OPERACIONES Y RECORRIDO EN CONJUNTOS")
print("\n *** Países en ambos conjuntos ***")
comunes= paises_sudamerica & paises_caribe
print(f"paises comunes= {comunes}")
for pais in comunes:  # Intersección
    print(f"- {pais} pertenece a paises comunes")




print()
print("*************************************************")
print("*** Países ***")

capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "México": "Ciudad de México"
}
# RECORRIDO POR KEY
for pais in capitales.keys():  # También: for pais in capitales:
    print(f"- {pais}")
# RECORRIDO POR VALUES
print("\n*** Capitales ***")
for ciudad in capitales.values():
    print(f"- {ciudad}")
    
# RECORRIDO POR KEY Y POR VALOR AL MISMO TIEMPO
# con .items Devuelve una vista de pares (clave, valor) del diccionario
for pais, capital in capitales.items():
    print(f"Clave: {pais}     Valor: {capital}")