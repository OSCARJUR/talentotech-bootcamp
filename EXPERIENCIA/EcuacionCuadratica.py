# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 00:50:14 2025

@author: MSI-PC
"""
import numpy as np

def ecuaCuadratica(a,b,c):
    x1=(-b+np.sqrt((b**2)-(4*a*c)))/(2*a)
    x2=(-b-np.sqrt((b**2)-(4*a*c)))/(2*a)
    return x1, x2

x1,x2=ecuaCuadratica(1, -14, 49)
print(x1,x2)