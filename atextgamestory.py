import time, sys, os, pickle
import pygame
import Utility
import Capitolo_1
import Capitolo_2
import json
# motore di salvataggio

Utility.saving_crea()
# STARTUP

print("#######################################################################################################################################################################################################")
time.sleep(2)
print("In un mondo molto lontano dal nostro viveva una civiltà.............")
time.sleep(2)
print("Un unico sopravvissuto rimase.. ")
time.sleep(2)
print("e questo....... sei Tu!")
print("")
print("")
time.sleep(0.5)
print("")
print("")
print("")
time.sleep(0.5)
print("")
print("")
print("")
time.sleep(0.5)
print("")
print("")
print("")

# printing del titolo
titolo = str(
        "########################################################################################################################################################\n"
        "#######################################################################################################################################_######_#########\n"
        "#####¯¯##|        ||¯¯¯¯¯¯¯##¯#####¯##|      |### /¯¯¯¯¯¯¯ ######¯¯#####¯¯####¯¯##|¯¯¯¯¯¯¯## /¯¯¯¯¯|#|        |##/¯¯¯¯¯\###|¯¯¯¯¯¯¯¯|#\ ###### /########\n"
        "####    #####  ####|_____  #### _ #######  ######||  ____  #####    #### # ## # ##|_____  ##(_____  #####  #####/       \##|    ____|##\ #### /#########\n"
        "### #### ####  ####|¯¯¯¯¯  #### ¯ #######  ######|| | || | #### #### ### ##__## ##|¯¯¯¯¯  ##      \ #####  #####\       /##|    \########|  |###########\n"
        "##_/    \_###__####|_______##_#####_#####_ ###### \___||__ ###_/    \_##_######_##|_______##|______)#####__######\_____/###|____ \#######|__|###########\n"
        "########################################################################################################################################################\n"
        "########################################################################################################################################################\n")

# gestore del timing della scrittura
for char in titolo:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.005)


# MENU di gioco

def menu():

    print("\n\n\n\n\n                                                   MENÚ")
    time.sleep(0.2)
    print("            <G                            <GIOCA>                      ")
    time.sleep(0.2)
    print("            <E                            <ESCI>                       ")
    time.sleep(0.5)
    print("            <1                           <EPISODIO-1>                     ")
#if Utility.gioco["livello"] >= 1:
    print("            <2                           <EPISODIO-2>                     ")
# else:
# pass
    print("\n            <999                         <ELIMINA DATI DI SALVATAGGIO>                 ")
    print("#####################################################################################################################################################################################################################\n")

    # MENU variabile di inserimento comando a opzioni numeriche
    comando = input()
    if comando == "E":
        print("Come vuoi tu capo! ;)")
        sys.exit(0)
    elif comando == "1":
        Capitolo_1.prologo()
    elif comando == "2":
        menu()
      # Cancellazione dati
    elif comando == "999":
        delete = input("SEI SICURO? SCRIVI ESATTAMENTE \"Si\" (case sensitive) SE CONFERMI.\nNON POTRAI MAI PIU' RECUPERARE I TUOI DATI SE PROCEDI.")
        if delete == "Si":
            #Rimozione e rimpiazzo
            os.remove("saving.txt")
            print("\n\nDATI RIMOSSI CON SUCCESSO!")
            Utility.saving_crea()
            #countdown
            countdown = 3
            print("")
            time.sleep(2)
            while countdown != 0:
                print("tornerai al menù principale tra " + str(countdown) + " secondi")
                countdown -= 1
                time.sleep(1)
            menu()
        elif delete != "Si":
            print("Annullo l'operazione...")
            time.sleep(1)
            menu()
        else:
            menu()
        # inizio del gioco (scena introduttiva)
    elif comando == "G":
        print("")
        print("")
        print("                   COMUNICAZIONE DI SERVIZIO")
        print(" la vita sul tuo pianeta è terminata ")
        time.sleep(1)
        print(" la distruzione ha preso possesso della tua anima vedi ancora la tua casa in fiamme................... ")
        time.sleep(1)
        print(" eri su una nave diretto su un altro pianeta")
        time.sleep(2)
        print(" sei stato espulso aadwinpaipdpiandPIUFIIP SEI L'ULTIMOADAD,AàDò,, ")
        time.sleep(1)
        print("                     TERMINE COMUNICAZIONE")
        time.sleep(3)

        collegamento = input("premi invio per procedere all' episodio successivo")
        if collegamento == "":
            Capitolo_1.prologo()

    else:
        print("\nSi è verificato un problema!\n\n")
        print('''          _ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              ;   ;
              /   \ 
_____________/_ __ \_____________\n''')

        # countdown
        countdown = 3
        print("")
        time.sleep(2)
        while countdown != 0:
            print("tornerai al menù principale tra " + str(countdown) + " secondi")
            countdown -= 1
            time.sleep(1)
        menu()

# MENU richiamo della funzione
menu()