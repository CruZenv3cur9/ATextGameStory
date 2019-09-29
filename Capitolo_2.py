import time, sys, os, pickle
import pygame
import Utility

# INIZIO DEL SECONDO EPISODIO
def scena2():

    global frase1
    frase1 = "ciaoooooo"
     # writing
    for char in frase1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


