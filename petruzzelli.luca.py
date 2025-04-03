import random
import pandas as pd

# Definizione delle rarità e probabilità
RARITA = ['Comune', 'Non Comune', 'Rara', 'Ultra Rara']
PROBABILITA = [0.7, 0.2, 0.09, 0.01]

trovate = {}  # Dizionario per memorizzare le carte trovate
punti = 100  # Punti iniziali

# Punti da guadagnare in base alla rarità
GUADAGNO_PUNTI = {
    'Comune': 2,
    'Non Comune': 5,
    'Rara': 10,
    'Ultra Rara': 20
}

# Funzione per generare una carta casuale
def genera_carta():
    r = random.choices(RARITA, PROBABILITA)[0]
    return r

# Funzione per aprire un pacchetto
def apri_pacchetto():
    carte = [genera_carta() for _ in range(5)]  # Genera 5 carte
    return carte

# Funzione per stampare le carte
def stampa_carte(carte):
    print("Carte trovate nel pacchetto:")
    for carta in carte:
        print(f"- {carta}")

# Funzione per il gioco
def gioco(punti):
    if punti >= 10:
        punti -= 10  # Diminuisci 10 punti per aprire il pacchetto
        print("Ora hai", punti, "punti.")
        
        carte = apri_pacchetto()  # Apre il pacchetto e ottiene le carte
        stampa_carte(carte)  # Stampa le carte

        # Calcola il guadagno di punti
        guadagno = 0
        for carta in carte:
            guadagno += GUADAGNO_PUNTI[carta]
            # Aggiungi la carta alla collezione
            if carta not in trovate:
                trovate[carta] = {"rarità": carta, "guadagno": GUADAGNO_PUNTI[carta]}

        print(f"Hai guadagnato {guadagno} punti!")
        punti += guadagno
        return punti
    else:
        print("Punti insufficienti.")
        return punti

# Funzione per visualizzare le istruzioni
def istruzioni():
    print("\nPremi 0 per uscire")
    print("Premi 1 per aprire un pacchetto")
    print("Premi 2 per mostrare l'intera collezione")
    print("Premi 3 per mostrare i punti")

# Funzione per visualizzare l'intera collezione
def mostra_collezione():
    if trovate:
        print("\nCollezione di carte trovate:")
        for carta, info in trovate.items():
            print(f"{carta} - Rarità: {info['rarità']}, Punti guadagnati: {info['guadagno']}")
    else:
        print("Non hai ancora trovato alcuna carta.")

# Ciclo principale del gioco
while True:
    istruzioni()
    messaggio = int(input("Menu: "))
    if messaggio == 0:
        print("Grazie per aver giocato!")
        break
    elif messaggio == 1:
        punti = gioco(punti)  # Passa i punti correnti alla funzione gioco
    elif messaggio == 2:
        mostra_collezione()  # Mostra l'intera collezione di carte trovate
    elif messaggio == 3:
        print(f"Hai {punti} punti.")  # Mostra i punti correnti
    else:
        print("Scelta non valida.")
