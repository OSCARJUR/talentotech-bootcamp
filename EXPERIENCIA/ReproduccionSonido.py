# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 19:32:47 2025

@author: MSI-PC
"""
import pygame
import time

pygame.mixer.init()

# Sonidos predefinidos (beeps)
def tocar_nota(nota, duracion=300):
    pygame.mixer.Sound.play(pygame.mixer.Sound(buffer=bytes([127] * duracion))).set_volume(0.1)
    time.sleep(duracion/1000)

# Reproducir patrón simple
print("Reproduciendo patrón de notas...")
for _ in range(2):
    tocar_nota('C4', 200)
    tocar_nota('E4', 200)
    tocar_nota('G4', 400)
    time.sleep(0.2)

pygame.quit()