# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 22:00:45 2025

@author: MSI-PC
"""

import matplotlib.pyplot as plt
import numpy as np

def curva_bomba(caudal, h_max, q_max):
    """
    Calcula la altura (head) de la bomba para un caudal dado,
    usando una curva cuadrática típica: H = Hmax * (1 - (Q/Qmax)^2)
    """
    return h_max * (1 - (caudal / q_max)**2)

def npsh_requerido(caudal, npsh_min, q_max):
    """
    Calcula la altura neta positiva de succión requerida (NPSHr)
    como función creciente del caudal, lineal para simplificar.
    """
    return npsh_min + (caudal / q_max) * (npsh_min * 2)  # ejemplo lineal

def seleccionar_bomba(caudal_deseado, bombas):
    """
    Selecciona la bomba que cumple con el caudal deseado y tiene la mayor altura
    disponible en ese caudal, además verifica NPSH.
    """
    opciones_validas = []
    for bomba in bombas:
        h = curva_bomba(caudal_deseado, bomba['h_max'], bomba['q_max'])
        npsh = npsh_requerido(caudal_deseado, bomba['npsh_min'], bomba['q_max'])
        if h > 0 and npsh <= bomba['npsh_max']:
            opciones_validas.append({
                'nombre': bomba['nombre'],
                'altura': h,
                'npsh': npsh,
                'costo': bomba['costo']
            })
    if not opciones_validas:
        return None
    # Seleccionar la bomba con mayor altura y menor costo (prioridad altura)
    opciones_validas.sort(key=lambda x: (-x['altura'], x['costo']))
    return opciones_validas[0]

def graficar_bombas(bombas, caudal_deseado):
    q = np.linspace(0, max(b['q_max'] for b in bombas), 100)
    plt.figure(figsize=(10,6))
    for bomba in bombas:
        h = curva_bomba(q, bomba['h_max'], bomba['q_max'])
        plt.plot(q, h, label=f"{bomba['nombre']} (Costo: ${bomba['costo']})")
        # Marcar punto optimo (caudal deseado)
        h_opt = curva_bomba(caudal_deseado, bomba['h_max'], bomba['q_max'])
        plt.plot(caudal_deseado, h_opt, 'o')
        plt.text(caudal_deseado, h_opt, f"{bomba['nombre']}", fontsize=9, ha='right')
    plt.axvline(caudal_deseado, color='gray', linestyle='--', label='Caudal deseado')
    plt.xlabel("Caudal (m³/h)")
    plt.ylabel("Altura (m)")
    plt.title("Curvas características de bombas centrífugas")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Definir datos de 3 bombas como ejemplo
    bombas = [
        {'nombre': 'Bomba A', 'h_max': 50, 'q_max': 100, 'npsh_min': 3, 'npsh_max': 6, 'costo': 1200},
        {'nombre': 'Bomba B', 'h_max': 45, 'q_max': 120, 'npsh_min': 2.5, 'npsh_max': 5, 'costo': 1000},
        {'nombre': 'Bomba C', 'h_max': 55, 'q_max': 90, 'npsh_min': 3.5, 'npsh_max': 7, 'costo': 1400},
    ]

    # Datos de entrada del usuario
    caudal_deseado = float(input("Ingrese el caudal deseado (m³/h): "))

    # Selección de bomba óptima
    bomba_seleccionada = seleccionar_bomba(caudal_deseado, bombas)
    if bomba_seleccionada:
        print("\nBomba seleccionada:")
        print(f"Nombre: {bomba_seleccionada['nombre']}")
        print(f"Altura en caudal deseado: {bomba_seleccionada['altura']:.2f} m")
        print(f"NPSH requerido: {bomba_seleccionada['npsh']:.2f} m")
        print(f"Costo estimado: ${bomba_seleccionada['costo']}")
    else:
        print("No se encontró una bomba adecuada para el caudal y condiciones dadas.")

    # Graficar curvas y puntos óptimos
    graficar_bombas(bombas, caudal_deseado)

if __name__ == "__main__":
    main()
