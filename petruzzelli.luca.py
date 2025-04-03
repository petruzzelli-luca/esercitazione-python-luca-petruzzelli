import random
import pandas

# Definizione delle rarità e probabilità
RARITA = ['Comune', 'Non Comune', 'Rara', 'Ultra Rara']
PROBABILITA = [0.7, 0.2, 0.09, 0.01]

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
    print(r)

# Funzione per aprire un pacchetto
def apri_pacchetto():
    for i in range(5):
        carte = [genera_carta()]
        print(carte)

# Funzione per stampare le carte
def stampa_carte(carte):
    print("Carte trovate nel pacchetto:")
    for carta in carte:
        print(f"- {carta}")

# Funzione per salvare le carte trovate in un file CSV










def gioco():
    punti = 100
    if punti >= 10:
        print("Hai", punti, "punti.")
        carte = apri_pacchetto()
        stampa_carte(carte)

        # Calcola il guadagno di punti
        guadagno = sum(GUADAGNO_PUNTI[carta] for carta in carte)
        print(f"Guadagni {guadagno} punti!")
        punti += guadagno - 10  
        salva_carte(carte)
    else:
        print("punti insufficienti.")
    
    
def istruzioni():
    print("premi 0 per uscire")
    print("premi 1 per salvare il progresso")
    print("premi 2 per aprire un pacchetto")
    print("premi 3 per mostrare l'intera collezione")
    print("premi 4 per mostrare i punti")






while True:
    istruzioni()
    messaggio= int(input("menu: "))
    if messaggio==0:
        print("Grazie per aver giocato!")
        break
    elif messaggio==1:
        
        print("salvataggio avvenuto con successo")
    elif messaggio==2:
        gioco()
    elif messaggio==3:
        print("ecco l'intera collezione")