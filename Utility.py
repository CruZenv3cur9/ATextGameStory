import atextgamestory, sys, time, Capitolo_2
import os.path
import json
from os import path


gioco = {"livello": 0, "frase": 3}
episodi = {"ep1" : "Capitolo1.txt", "ep2" : "Capitolo2.txt"}
file_salva = "saving.txt"
ep1 = "Capitolo1.txt"

def loading():

    with open(episodi["ep1"], 'r') as f:
        ep1 = json.load(f)
    f.close()




def saving_crea():

    if path.exists(file_salva):
        with open(file_salva, 'r') as f:
            gioco = json.load(f)
        f.close()

        #todo
        print(gioco)

    else:
        gioco = {"livello":0, "frase":3}
        with open(file_salva, 'w') as f:
            json.dump(gioco, f)
        f.close()

        #Todo
        print(gioco)

        # METTERE A POSTO STA ROBA
def saving():

    with open(file_salva, 'w') as f:
        json.dump(gioco, f)
    print("SV-OK")
    #todo
    print(gioco)


pass


def chapter_level():

    pass

# def continuer():
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
# SETUPPARE COLLEGAMENTO TRA LISTE DI FILE DIVERSI
