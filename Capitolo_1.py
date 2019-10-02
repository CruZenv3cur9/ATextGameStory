import atextgamestory, Utility, pygame
import time, sys
import Capitolo_2


# PROLOGO
def prologo():
    # starting del file audio
    # file = 'Piscio.mp3'
    # pygame.mixer.init()
    # pygame.mixer.music.load(file)
    # pygame.mixer.music.play()
    # time.sleep(0.5)
    # starting della prima frase
    # Utility.loading()
    frase_1 = (
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\PROLOGO  \n\n\ni tuoi occhi si aprono a fatica.......... \ncome se non li aprissi da anni......\nti senti stanco..... assonnato... e  non sai dove ti trovi............ \npercepisci che l'ambiente intorno a te è grande............ "
        "\nquando qualcosa inizia a fare del rumore...... \n"
        "lo senti che si avvicina \ncorrendo .......... \ninizi a sentire il suo respiro \n"
        "percepisci che è vicino  \nmolto vicino..... con uno scatto involontario balzi indietro \n"
        "urti con il braccio destro un oggetto solido \ndi forma cubica, spigolosa \n"
        "l'animale indietreggia quasi come se fosse lui più spaventato di te \n"
        "e proprio in quel momento una voce metallica inizia a parlare alla tua destra \n"
        "dice :'nome dell'animale, pacifico, età 3 anni, un piccolo quadrupede simile ad un gatto, pelo schiumoso e leggermente pennato,\n"
        "agile e veloce si preda principalmente di piccoli animali \n"
        "a quel punto per istinto allunghi la mano in un gesto amichevole verso la creatura \n"
        "lui struscia quello che sembra il suo muso sul tuo arto \n"
        "così come per magia la tua mente si dimentica........\n"
        "di ogni cosa, di ogni dubbio, paura, insicurezza \n"
        "così per un momento la tua vita diviene magnifica.....................\n ")
    # modulo di scrittura

    for char in frase_1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.007)
    Intro_tutorial()

def Intro_tutorial():
    time.sleep(3)
    print("""Ciao!
    Benvenuto a questo tutorial!
    Ora ti insegnerò alcuni comandi base!
    Ad esempio per spostarti usa l\'iniziale dei quattro punti cardinali:(n, e, s, o).
    Prova!""")
    tutorial = input("Che cosa faccio?\n-->").lower()
    if tutorial == "n" or  tutorial =="e" or  tutorial =="s" or  tutorial =="o":
        print("\nCi sai fare con le lettere!")
        pass
    else:
        print("Non ho capito. E neanche tu. Te lo ripeto...\n")
        Intro_tutorial()
    print("\nBravo! C'è molta nebbia ma puoi provare a cercare qualcosa con il comando \"guarda\"!Prova a usare questo comando!")
    tutorial = input("Che cosa faccio?\n-->").lower()
    if tutorial == "guarda":
        print("\nTi ho detto che c'è la nebbia!")
        time.sleep(2)
        print("OK. Stavolta ti aiuto io... C'è uno zaino lì per terra.")
        pass
    else:
        print("What?! Ripartiamo da capo...\n")
        Intro_tutorial()
    print("\nOra prova a prendere quello zaino che c'è li per terra! Devi dire \"prendi zaino\"")
    tutorial = input("Che cosa faccio?\n-->").lower()
    if tutorial == "prendi zaino":
        print("\nAbbiamo a che fare con un genio, vedo...\nBene! Il tutorial è finito! Ora comincia la vera avventura.")
        time.sleep(1)
        print("\n\nTeletrasporto a caso nel mondo in corso...")
        Tutorial1()
    else:
        print("IMPEGNATI RECLUTA! Avevi solo da non sbagliare...\n")
        Intro_tutorial()


oggetti1 = ["mela", "pera"]

def Tutorial1():
    # TUTORIAL 1
    print("\n\n")
    def tut_input_1():
        bivio = Utility.my_input("\n  1 Che cosa faccio?\n-->", oggetti1)
        if bivio["azione"] == "movimento":
            if bivio["comando"] == "e":
                print("Vai verso est.")
                Tutorial2()
            elif bivio["comando"] == "s":
                print("Vai verso sud.")
                Tutorial3()
            else:
                print("Non puoi andare qui.")
                tut_input_1()
        elif bivio["azione"] == "guardare":
            print("Vedi un passaggio a est ed una nebbia fitta provenire da sud...")
            tut_input_1()
        else:
            tut_input_1()

    tut_input_1()

    # richiamo motore di saving


# Utility.gioco["frase"] = 1
# Utility.saving()

# TUTORIAL 2

oggetti2 = ["chiave"]


def Tutorial2():
    print("Sei nella seconda stanza.")

    def tut_input_2():
        bivio = Utility.my_input("\n 2  Che cosa faccio?\n-->", oggetti2)
        if bivio["azione"] == "movimento":
            if bivio["comando"] == "o":
                print("Vai verso ovest.")
                Tutorial1()
            elif bivio["comando"] == "s":
                print("Vai verso sud.")
                Tutorial4()
            else:
                print("Non puoi andare qui.")
                tut_input_2()
        elif bivio["azione"] == "guardare":
            print("Vedi un passaggio a ovest ed una nebbia fitta provenire da sud...")
            tut_input_2()
        else:
            tut_input_2()

    tut_input_2()


# TUTORIAL 3

oggetti3 = []


def Tutorial3():
    print("Sei nella terza stanza.")

    def tut_input_3():
        bivio = Utility.my_input("\n 3  Che cosa faccio?\n-->", oggetti3)
        if bivio["azione"] == "movimento":
            if bivio["comando"] == "n":
                print("Vai verso nord.")
                Tutorial1()
            elif bivio["comando"] == "e":
                print("Vai verso est.")
                Tutorial4()
            else:
                print("Non puoi andare qui.")
                tut_input_3()
        elif bivio["azione"] == "guardare":
            print("Vedi la navicella a nord e un buco ad est...")
            tut_input_3()

    tut_input_3()


# TUTORIAL 4

oggetti4 = ["sasso"]


def Tutorial4():
    print("Sei nella quarta stanza.")

    def tut_input_4():
        bivio = Utility.my_input("\n 4  Che cosa faccio?\n-->", oggetti4)
        if bivio["azione"] == "movimento":
            if bivio["comando"] == "n":
                print("Vai verso nord.")
                Tutorial2()
            elif bivio["comando"] == "o":
                print("Vai verso ovest.")
                Tutorial3()
            else:
                print("Non puoi andare qui.")
                tut_input_4()
        elif bivio["azione"] == "guardare":
            print("Vedi un grosso masso ad nord e un animale ad ovest...1")
            tut_input_4()

    tut_input_4()


