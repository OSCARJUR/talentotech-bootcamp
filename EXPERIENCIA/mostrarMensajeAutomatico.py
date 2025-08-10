# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 15:30:23 2025

@author: MSI-PC
"""

import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Bienvenidos a Python")

# Crear el letrero
letrero = tk.Label(ventana, text="Bienvenidos a Python", font=("Arial", 24))
letrero.pack()

# Función para mostrar y ocultar el letrero de manera automática
def mostrar_ocultar_letrero():
    if letrero.winfo_ismapped():
        letrero.pack_forget()
    else:
        letrero.pack()
    ventana.after(700, mostrar_ocultar_letrero)

# Iniciar la función de mostrar y ocultar el letrero
mostrar_ocultar_letrero()

# Iniciar la ventana
ventana.mainloop()