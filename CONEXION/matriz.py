# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 22:51:33 2025

@author: MSI-PC
"""

m=[[2,4],[6,8],[10,12,14,16]]
print(f"numero de filas, {len(m)} ")
for i in range(len(m)): #numero de filas
    print("")
    for j in range(len(m[i])): #numero de columnas
        print(f"numero de columnas, {len(m[i])} ")
        print(m[i],[j], end="")