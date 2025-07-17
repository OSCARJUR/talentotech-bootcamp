# DISEÑO DE UNA CALCULADORA CON FUNCIONES 
import math

def mostrar_titulo():
    print('\nEjemplo Calculadora Sencilla (+,-,*,/) por Oscar R. Jurado:')

def mostrar_menu():
    print("\nMENU:")
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

def ingresar_datos():
    try:
        opcion = int(input("\nQué opción deseada (1-12): "))
        if opcion == 12:
            return opcion, None, None, None
            
        if 1 <= opcion <= 6 or opcion == 8:
            num1 = float(input('Ingrese el primer número: '))
            num2 = float(input('Ingrese el segundo número: '))
            return opcion, num1, num2, None
        elif opcion in [7, 9, 10, 11]:
            grados = float(input('Ingrese el ángulo en grados: '))
            return opcion, None, None, grados
        else:
            print("Opción no válida. Intente de nuevo.")
            return None, None, None, None
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return None, None, None, None

def calcular_suma(numero_uno, numero_dos):
    return numero_uno + numero_dos

def calcular_resta(numero_uno, numero_dos):
    return numero_uno - numero_dos

def calcular_multiplicacion(numero_uno, numero_dos):
    return numero_uno * numero_dos

def calcular_division(numero_uno, numero_dos):
    if numero_dos != 0:
        return numero_uno / numero_dos
    else:
        print("¡No es posible dividir entre cero!")
        return None

def calcular_potencia(numero_uno, numero_dos):
    return numero_uno ** numero_dos

def calcular_radicacion(numero_uno, numero_dos):
    return numero_uno ** (1/numero_dos)

def calcular_logaritmo_base10(grados):
    return math.log10(grados)

def calcular_logaritmo_cualquierbase(numero_uno, numero_dos):
    return math.log(numero_dos, numero_uno)

def calcular_seno(grados):
    radianes = math.radians(grados)
    return math.sin(radianes)

def calcular_coseno(grados):
    radianes = math.radians(grados)
    return math.cos(radianes)

def calcular_tangente(grados):
    radianes = math.radians(grados)
    return math.tan(radianes)

def procesar_operacion(opcion, numero_uno, numero_dos, grados):
    if opcion == 1:
        print("\nVamos a sumar(+) los dos valores ingresados:")
        resultado = calcular_suma(numero_uno, numero_dos)
        print(f'{numero_uno} + {numero_dos} = {resultado}')
        
    elif opcion == 2:
        print("\nVamos a restar(-) los dos valores ingresados:")
        resultado = calcular_resta(numero_uno, numero_dos)
        print(f'{numero_uno} - {numero_dos} = {resultado}')
        
    elif opcion == 3:
        print("\nVamos a multiplicar(*) los dos valores ingresados:")
        resultado = calcular_multiplicacion(numero_uno, numero_dos)
        print(f'{numero_uno} * {numero_dos} = {resultado}')
        
    elif opcion == 4:
        print("\nVamos a dividir(/) los dos valores ingresados:")
        resultado = calcular_division(numero_uno, numero_dos)
        if resultado is not None:
            print(f'{numero_uno} / {numero_dos} = {resultado}')
            
    elif opcion == 5:
        print("\nVamos a calcular la potencia:")
        print(f"Base: {numero_uno}, Exponente: {numero_dos}")
        resultado = calcular_potencia(numero_uno, numero_dos)
        print(f'{numero_uno} ** {numero_dos} = {resultado}')
        
    elif opcion == 6:
        print("\nVamos a calcular la raíz enésima:")
        print(f"Radicando: {numero_uno}, Índice: {numero_dos}")
        resultado = calcular_radicacion(numero_uno, numero_dos)
        print(f'Raíz {numero_dos} de {numero_uno} = {resultado}')
        
    elif opcion == 7:
        print("\nCálculo del logaritmo base 10:")
        resultado = calcular_logaritmo_base10(grados)
        print(f'log10({grados}) = {resultado}')
        
    elif opcion == 8:
        print("\nVamos a calcular el logaritmo en base N:")
        print(f"Base: {numero_uno}, Número: {numero_dos}")
        resultado = calcular_logaritmo_cualquierbase(numero_uno, numero_dos)
        print(f'log{numero_uno}({numero_dos}) = {resultado}')
        
    elif opcion == 9:
        print("\nCálculo del seno:")
        resultado = calcular_seno(grados)
        print(f'sen({grados}°) = {resultado}')
        
    elif opcion == 10:
        print("\nCálculo del coseno:")
        resultado = calcular_coseno(grados)
        print(f'cos({grados}°) = {resultado}')
        
    elif opcion == 11:
        print("\nCálculo de la tangente:")
        resultado = calcular_tangente(grados)
        print(f'tan({grados}°) = {resultado}')
        
    elif opcion == 12:
        print("\nSaliendo del programa... ¡Hasta luego! 👋")
        return True
    
    return False

def main():
    mostrar_titulo()
    
    while True:
        mostrar_menu()
        opcion, num1, num2, grados = ingresar_datos()
        
        if opcion is None:
            continue
            
        if procesar_operacion(opcion, num1, num2, grados):
            break
            
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()

    # hola nuevos cambios