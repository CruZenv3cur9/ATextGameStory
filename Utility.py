# motore di salvataggio
def saving_crea():
    try:
        saving = open("saving.txt", "w")
    except:
        saving = open("saving.txt", "x")
    saving.close()

def saving():  # TODO load data to file
    global salvataggio_progressi
    try:
        saving = open("saving.txt", "w")
    except:
        saving = open("saving.txt", "x")
    saving.write(str(salvataggio_progressi))
    saving.close()
    return saving
    print("\n\n\nSV-OK")


#creazione saving
#creazione_file = open("saving.txt", "w")
#creazione_file.close()
saving_crea()
# LISTE  GLOBALI
progressi_scena1 = ["1"]
lettura  = open("saving.txt", "r")
lettura2 = str(lettura.read())
salvataggio_progressi = list(lettura2.split(","))
lettura.close()
saving()
