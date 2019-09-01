# motore di salvataggio
from typing import Any


def saving_crea():
    try:
        saving = open("saving.txt", "w")
    except:
        saving = open("saving.txt", "x")
    saving.close()

def saving():  # TODO load data to file
    salvataggio_progressi = []
    saving = open ("saving.txt", "w")
    saving.write(str(salvataggio_progressi))
    saving.close()
    print("SV-OK")
    return saving

