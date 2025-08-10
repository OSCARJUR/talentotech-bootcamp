# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 19:02:20 2025

@author: MSI-PC
"""

#
suma=0
for i in range(1,101):
    if i%3==0:
        #suma=suma+i
        suma+=i
        print(f"Los multiplos de 3 son: {i}")
print(f"La suma de los multiplos de 3 es, {suma}")