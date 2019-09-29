import atextgamestory, sys, time, Capitolo_2
import os.path
import json
from os import path

gioco = {"livello": 0, "frase": 0, "stanza": 0}
file_salva = "saving.txt"

azioni = {"movimento": ["n", "e", "s", "o"],
          "guardare": ["guarda", "osserva", "controlla"],
          "prendere": ["prendi", "afferra"],
          "posare": ["posa", "lascia", "tira"],
          "usare": ["usa", "utilizza"],
          "esci": ["esci","exit","chiudi"],
          "insultare": ["vaffanculo", "scemo", "coglione", "bastardo", "stupido", "stronzo", "idiota"]}
zaino=["zaino","torcia"]

def morte():
    print("\n\n\nAHAHAHAHAH. Sei morto...\n...scemo!")
    time.sleep(3)
    sys.exit(0)

def saving_crea():

    if path.exists(file_salva):
        with open(file_salva, 'r') as f:
            gioco = json.load(f)
        f.close()

        #todo
        print(gioco)

    else:
        gioco = {"livello": 0, "frase": 0, "stanza": 0}
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

# ---------------------------------------------------------------------------------------

def my_input(cTxt="", aLuogo=[]):
    while True:
        cInp = input(cTxt).lower()
        aAzio = cInp.split()
        try:
            cCmd = aAzio[0]
        except IndexError:
            print("IndexError... Scrivi qualcosa pls...")
            cCmd = "errore"
        xAzio=""
        xOgg=""
        if cCmd in azioni["movimento"]:
           xAzio = "movimento"
        elif cCmd in azioni["guardare"]:
           xAzio = "guardare"
        elif cCmd in azioni["prendere"]:
           xAzio = "prendere"
        elif cCmd in azioni["posare"]:
           xAzio = "posare"
        elif cCmd in azioni["usare"]:
           xAzio = "usare"
        elif cCmd in azioni["esci"]:
            xAzio = "esci"
        elif cCmd in azioni["insultare"]:
            xAzio = "insultare"
            print(str((cCmd).upper()) + "!?\n")
            time.sleep(1)
            print(str((cCmd).upper()) + " A ME!?")
            time.sleep(1)
            print("Ti faccio vedere io adesso...")
            time.sleep(3)
            morte()
        else:
            print("Non ho capito.")

        for ogg in aAzio:
            if ogg in zaino:
                xOgg=ogg
                if xAzio=="posare":
                    aLuogo.append(ogg)
                    zaino.remove(ogg)
                    print("Hai lasciato: \"" + ogg +"\".")
                break
            elif ogg in aLuogo:
                xOgg=ogg
                if xAzio=="prendere":
                    zaino.append(ogg)
                    aLuogo.remove(ogg)
                    print("Hai preso: \"" + ogg +"\".")
                break


        if len(xAzio)!=0:
            return {"azione":xAzio, "comando":cCmd, "oggetto":xOgg}

#- FINE LIBRERIA ----------------------------------------------------------------------------