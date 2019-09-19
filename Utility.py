import atextgamestory, sys, time, Capitolo_2
import os.path
from os import path

# motore di salvataggio
salvataggio_progressi = []
def saving_crea():
    if path.exists("saving.txt") == True:
       print()
    else:
        saving = open("saving.txt", "w")
        saving.write(str())
        saving.close()
# METTERE A POSTO STA ROBA
def saving():
    saving = open("saving.txt", "w")
    saving.write(str(salvataggio_progressi + 1))
    saving.close()
    print("SV-OK")
print()

def chapter_level():
    global salvataggio_progressi
    progressi = open("saving.txt", "r")
    salvataggio_progressi = progressi
    if "0" in salvataggio_progressi and atextgamestory.menu().comando == "2":
        print("Non hai ancora sbloccato questo livello!")
        # countdown
        countdown = 3
        print("")
        time.sleep(2)
        while countdown != 0:
            print("tornerai al menù principale tra " + str(countdown) + " secondi")
            countdown -= 1
            time.sleep(1)
        atextgamestory.menu()
    else:
        Capitolo_2.scena2()
print()



#def continuer():
#    global salvataggio_progressi
#    if "1" in salvataggio_progressi:
#              Capitolo_2.scena2()
#    else:
#        print("\nprima di poter accedere all'episodio 2 devi aver completato l'episodio 1")
#        #countdown
#        countdown = 3
#        print("")
#        time.sleep(2)
#        while countdown != 0:
#            print("tornerai al menù principale tra " + str(countdown) + " secondi")
#            countdown -= 1
#            time.sleep(1)
#        atextgamestory.menu()
#
#SETUPPARE COLLEGAMENTO TRA LISTE DI FILE DIVERSI