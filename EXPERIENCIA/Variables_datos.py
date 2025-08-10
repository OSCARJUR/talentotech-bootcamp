""""
# RETO 1 ****** VARIABLES Y TIPO DE DATOS *******
nombre="OSCAR"
edad=53
altura=1.72
mayor_de_edad=True
print()
print(nombre)
print(edad)
print(altura)
print(mayor_de_edad)
print("****************************")


# RETO 2 ******  listas  *******

frutas=["manzana","banana","naranja","uva","kiwi"]
# imprime el segundo elemento de la lista
print(frutas[1])
# adiciona el elemento pera al final de la lista
frutas.append("pera")
print(frutas)
# eliminar narana de la lista
frutas.remove("naranja")
print(frutas)


# RETO  3 ******  CICLO FOR ****** 

numeros=[1,2,3,4,5,6,7,8,9,10]
for i in numeros:
    print(i*2, end="") #Aqui mprime los numeros en forma horizontal

    
# RETO 4 ****** CONDICIONALES *******

condicional=int(input("introduzca un numero entre 1 y 10:"))
if condicional ==9 or condicional == 10:
    print("Sobresaliente")
elif condicional ==7 or condicional == 8:
    print("Notable")
elif condicional ==6:
    print("Aprobado")
elif condicional <=6:
    print("Reprobado")
else:
    print("La opcion no es valida")

# 5TO RETO *****  COMBINACION DE CONCEPTOS  *****

palabras=["casa","carro","magdalena","cartagena","AMIGO"]
for i in palabras:
    #print(i)
    if len(i) >5:
        print(i.upper())
    else:
        print(i.lower())  """

# 6TO RETO FILTRADO DE NUMEROS CON ENTRADA DE USUARIO

limite=int(input("introduzca un numero entre 1 y 10: "))
numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a=0
for i in numeros:
    if i< limite:
        print(i)
        a+=1
print()
print(f"La cantidad de numeros menores al limite {limite} es: {a}")

if a==0:
    print("Ningun numero es menor o igual al limite")
    print()


