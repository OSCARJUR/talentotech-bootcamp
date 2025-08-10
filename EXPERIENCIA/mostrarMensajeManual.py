# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 15:34:25 2025

@author: MSI-PC
"""

import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Bienvenidos a Python")

# Crear el letrero
letrero = tk.Label(ventana, text="Bienvenidos a Python", font=("Arial", 24))
letrero.pack()

# Función para mostrar el letrero
def mostrar_letrero():
    letrero.pack()

# Función para ocultar el letrero
def ocultar_letrero():
    letrero.pack_forget()

# Crear botones para mostrar y ocultar el letrero
boton_mostrar = tk.Button(ventana, text="Mostrar", command=mostrar_letrero)
boton_mostrar.pack()

boton_ocultar = tk.Button(ventana, text="Ocultar", command=ocultar_letrero)
boton_ocultar.pack()

# Iniciar la ventana
ventana.mainloop()