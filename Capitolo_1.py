import atextgamestory, Utility, pygame, time, sys
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
    Stanza1()


oggetti1 = ["mela", "pera"]


def Stanza1():
    # STANZA 1
    def st_input_1():
        bivio = Utility.my_input("\n  1 Che cosa faccio?\n-->", oggetti1)
        if bivio["azione"] == "movimento":
            if bivio["comando"] == "e":
                print("Vai verso est.")
                Stanza2()
            elif bivio["comando"] == "s":
                print("Vai verso sud.")
                Stanza3()
            else:
                print("Non puoi andare qui.")
                st_input_1()
        elif bivio["azione"] == "guardare":
            print("Vedi un passaggio a est ed una nebbia fitta provenire da sud...")
            st_input_1()
        else:
            st_input_1()

    st_input_1()

    # richiamo motore di saving


# Utility.gioco["frase"] = 1
# Utility.saving()

# STANZA 2

oggetti2 = ["quadro"]


def Stanza2():
    print("Sei nella seconda stanza.")

    def st_input_2():
        bivio = Utility.my_input("\n 2  Che cosa faccio?\n-->", oggetti2)
        if bivio["azione"] == "movimento":
            if bivio["comando"] == "o":
                print("Vai verso ovest.")
                Stanza1()
            elif bivio["comando"] == "s":
                print("Vai verso sud.")
                Stanza4()
            else:
                print("Non puoi andare qui.")
                st_input_2()
        elif bivio["azione"] == "guardare":
            print("Vedi un passaggio a ovest ed una nebbia fitta provenire da sud...")
            st_input_2()
        else:
            st_input_2()

    st_input_2()


# STANZA 3

oggetti3 = []


def Stanza3():
    print("Sei nella terza stanza.")

    def st_input_3():
        bivio = Utility.my_input("\n 3  Che cosa faccio?\n-->", oggetti3)
        if bivio["azione"] == "movimento":
            if bivio["comando"] == "n":
                print("Vai verso nord.")
                Stanza1()
            elif bivio["comando"] == "e":
                print("Vai verso est.")
                Stanza4()
            else:
                print("Non puoi andare qui.")
                st_input_3()
        elif bivio["azione"] == "guardare":
            print("Vedi la navicella a nord e un buco ad est...")
            st_input_3()

    st_input_3()


# STANZA 4

oggetti4 = ["sasso"]


def Stanza4():
    print("Sei nella quarta stanza.")

    def st_input_4():
        bivio = Utility.my_input("\n 4  Che cosa faccio?\n-->", oggetti4)
        if bivio["azione"] == "movimento":
            if bivio["comando"] == "n":
                print("Vai verso nord.")
                Stanza2()
            elif bivio["comando"] == "o":
                print("Vai verso ovest.")
                Stanza3()
            else:
                print("Non puoi andare qui.")
                st_input_4()
        elif bivio["azione"] == "guardare":
            print("Vedi un grosso masso ad nord e un animale ad ovest...1")
            st_input_4()

    st_input_4()


