import random
import pandas 

dataframe_pokemon = pandas.read_csv('pokemon.csv')
punti = 100
punti_tot = punti
probabilità = {
    'Comune': 0.7,
    'Non Comune': 0.2,
    'Rara': 0.09,
    'Ultra Rara': 0.01
}





def apri_pacchetto():
    global punti_tot
    pacchetto = []
    punti_guadagnati = 0 
    if punti >=10:
        punti_tot -= 10
        for i in range(5):                 
            rarita_casuale = random.choices(list(probabilità.keys()),weights=probabilità.values(),k=1)[0]
                
            carta = dataframe_pokemon[dataframe_pokemon['Rarità'] == rarita_casuale].sample(n=1).iloc[0]
            pacchetto.append(carta)

            if rarita_casuale == 'Comune':
                punti_guadagnati += 2
            elif rarita_casuale == 'Non Comune':
                punti_guadagnati += 5
            elif rarita_casuale == 'Rara':
                punti_guadagnati += 10
            elif rarita_casuale == 'Ultra Rara':
                punti_guadagnati += 20
               
        punti_tot += punti_guadagnati        
        print(f"Hai guadagnato {punti_guadagnati} punti. Ora hai {punti_tot} punti.")
        stampa_carte(pacchetto)       
        salva_collezione(pacchetto)
    else:
        print("non hai abbastanza punti")
    return pacchetto, punti_tot

def salva_collezione(pacchetto):
    collezione = pandas.DataFrame(pacchetto)
    collezione.to_csv('carte_trovate.csv')
    print("Collezione salvata")



# stampare le carte
def stampa_carte(pacchetto):
    print("Carte trovate nel pacchetto:")
    for carta in pacchetto:
        print("-", carta)





def istruzioni():
    print("----------------------------------------------------------------------------")
    print("---------------------------Premi 0 per uscire-------------------------------")
    print("---Premi 1 per aprire un pacchetto (il costo del pacchetto è di 10 punti)---")
    print("-----------------Premi 2 per mostrare l'intera collezione-------------------")
    print("-----------------------Premi 3 per mostrare i punti-------------------------")
    print("----------------------------------------------------------------------------")

def mostra_intera_collezione():
    collezione_completa = pandas.read_csv('carte_trovate.csv')
    print(collezione_completa)


while True:
    istruzioni()
    try:
        messaggio = int(input("Menu: "))
        if messaggio == 0:
            print("Grazie per aver giocato!")
            break
        elif messaggio == 1:
            apri_pacchetto() 
        elif messaggio == 2:
            mostra_intera_collezione()  
        elif messaggio == 3:
            print(f"Hai {punti_tot} punti.")  
        else:
            print("Scelta non valida.")
    except ValueError:
        print("Inserisci un numero valido.")