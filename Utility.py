import atextgamestory, sys, time, Capitolo_2
import os.path
from os import path

# motore di salvataggio
salvataggio_progressi = []
def saving_crea():
    if path.exists("saving.txt") == True:
       print()
    else:
        saving = open("saving.txt", "x")
        saving.close()
# METTERE A POSTO STA ROBA
def saving():
    saving = open("saving.txt", "w")
    saving.write(str(salvataggio_progressi))
    saving.close()
    print("SV-OK")
    return saving
def saving_aggiungi():
    global salvataggio_progressi

    if "1" in salvataggio_progressi :
        domanda = input("premi 1 per   continuare con il prossimo episodio oppure premi INVIO per tornare al menù")
        if domanda == "1":
            Capitolo_2.scena2()
        # richiamo menu
        else:
            Capitolo_2.menù()
    else:
        salvataggio_progressi.append("1")

        # richiamo motore di saving
        saving()
        domanda = input ("premi 1 per   continuare con il prossimo episodio oppure premi INVIO per tornare al menù")

        if domanda == "1":
            Capitolo_2.scena2()
        else:
            atextgamestory.menù()
def continuer():
    global salvataggio_progressi
    if "1" in salvataggio_progressi:
        Capitolo_2.controllo += 1
        Capitolo_2.scena2()
    else:
        print("\nprima di poter accedere all'episodio 2 devi aver completato l'episodio 1")
        #countdown
        countdown = 3
        print("")
        time.sleep(2)
        while countdown != 0:
            print("tornerai al menù principale tra " + str(countdown) + " secondi")
            countdown -= 1
            time.sleep(1)
        atextgamestory.menù()

#SETUPPARE COLLEGAMENTO TRA LISTE DI FILE DIVERSI