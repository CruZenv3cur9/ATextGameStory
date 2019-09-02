import time, sys, os, pickle
import pygame
import Utility
# motore di salvataggio

Utility.saving_crea()
# LISTE  GLOBALI
progressi_scena1 = ["1"]
lettura  = open("saving.txt", "r")
lettura2 = str(lettura.read())
salvataggio_progressi = list(lettura2.split(","))
lettura.close()
Utility.saving()

    # INIZIO DEL PRIMO EPISODIO   (prima scena)

# INIZIO DEL PRIMO EPISODIO
def scena1():
    #starting del file audio
    file = 'Piscio.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(0.5)
    #starting della prima frase
    frase1 = (
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\EPISODIO 1\n\n\ni tuoi occhi si aprono a fatica.......... \ncome se non li aprissi da anni......\nti senti stanco..... assonnato... e  non sai dove ti trovi............ \npercepisci che l'ambiente intorno a te è grande............ "
        "\nquando qualcosa inizia a fare del rumore...... \n"
        "lo senti che si avvicina \ncorrendo .......... \n inizi a sentire il suo respiro \n"
        "percepisci che è vicino  \nmolto vicino..... con uno scatto involontario balzi indietro \n"
        "urti con il braccio destro un oggetto solido \ndi forma cubica, spigolosa \n"
        "l'animale indietreggia quasi come se fosse lui più spaventato di te \n"
        "e proprio in quel momento una voce metallica inizia a parlare alla tua destra \n"
        "dice :'nome dell'animale, pacifico, età 3 anni, un piccolo quadrupede simile ad un gatto, pelo schiumoso e leggermente pennato,\n"
        "agile e veloce si preda principalmente di piccoli animali \n"
        "a quel punto per istinto allunghi la mano in un gesto amichevole verso la creatura \n"
        "lui struscia quello che sembra il suo muso sul tuo arto \n"
        "così come per magia la tua mente si dimentica……..\n "
        "di ogni cosa, di ogni dubbio, paura, insicurezza \n"
        "così per un momento la tua vita diviene magnifica…………………\n ")
    # modulo di scrittura

    for char in frase1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)
    # aggiunta del valore 1
    global salvataggio_progressi
    Utility.saving_crea()
    Utility.saving_aggiungi()
    # richiamo motore di saving
    Utility.saving()
    domanda = input ("premi 1 per   continuare con il prossimo episodio oppure premi INVIO per tornare al menù")

    if domanda == "1":
        scena2()
    else:
        menù()


# INIZIO DEL SECONDO EPISODIO
def scena2():
    global salvataggio_progressi
    if "1" in salvataggio_progressi:
        frase1 = "ciaoooooo"
        # writing
        for char in frase1:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
    else:
        print("prima di poter accedere all'episodio 2 devi aver completato l'episodio 1")
        menù()


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

def menù():
    print("\n\n\n\n\n                                                   MENÚ")
    time.sleep(0.2)
    print("            <1                            <GIOCA>                      ")
    time.sleep(0.2)
    print("            <2                            <ESCI>                       ")
    time.sleep(0.5)
    print("            <3                           <EPISODIO-1>                     ")
    print("            <4                           <EPISODIO-2>                     ")
    print("\n            <999                         <ELIMINA DATI DI SALVATAGGIO>                 ")
    print("#####################################################################################################################################################################################################################\n")

    # MENU variabile di inserimento comando a opzioni numeriche
    comando = input("")
    if comando == "2":
        sys.exit(0)
    elif comando == "3":
        scena1()
    elif comando == " ":
        menù()
    elif comando == "4":
        scena2()
   # Cancellazione dati
    elif comando == "999":
        comando2 = input("SEI SICURO? SCRIVI \"Si\" SE CONFERMI.\nNON POTRAI MAI PIU' RECUPERARE I TUOI DATI SE PROCEDI.")
        if comando2 == "Si":
            os.remove("saving.txt")
            print("\n\nDATI RIMOSSI CON SUCCESSO!")
            Utility.saving_crea()
            Utility.saving()
            countdown = 5
            while countdown <= 0:
                print("tornerai al menù principale tra " + countdown + " secondi")
                time.sleep(1)
            menù()
        else:
            menù()

        # inizio del gioco (scena introduttiva)
    elif comando == "1":
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
            scena1()


# MENU richiamo della funzione
menù()
