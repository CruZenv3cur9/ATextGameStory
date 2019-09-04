import time, sys, os, pickle
import pygame
import Utility

controllo = 0


# INIZIO DEL SECONDO EPISODIO
def scena2(controllo=0):
    try:
        if controllo != 0:
            controllo = 0
            frase1 = "ciaoooooo"
     # writing

            for char in frase1:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
        else:
            Utility.continuer()
    finally:
        print (frase1)
        
