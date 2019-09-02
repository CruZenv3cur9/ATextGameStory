# motore di salvataggio
def saving_crea():
    try:
        saving = open("saving.txt", "w")
    except:
        saving = open("saving.txt", "x")
    saving.close()
# METTERE A POSTO STA ROBA
def saving():
    salvataggio_progressi = []
    saving = open("saving.txt", "w")
    saving.write(str(salvataggio_progressi))
    saving.close()
    print("SV-OK")
    return saving

#SETUPPARE COLLEGAMENTO TRA LISTE DI FILE DIVERSI