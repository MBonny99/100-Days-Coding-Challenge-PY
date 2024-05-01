import random

"""
random_integer = random.randint(1, 100)
print(random_integer)

random_float = random.random()  # 0 to 0.9999999
print(random_float)

random_number_decimal = random_integer + random_float
print(random_number_decimal)

max_number = int(input("Inserisci un numero per stabilire il range massimo per un float number randomico : \n"))
random_float_increased = random_float * max_number
print(random_float_increased)
"""

# Head or Tail coin flip

"""
value = random.randint(0, 1)
if value == 0:
    print("HEAD")
else:
    print("TAIL")
"""

# List
"""
# Zero Based List
states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]

print(states_of_america[0])
print(states_of_america[-1])  # parte dal fondo

states_of_america[1] = "Pencilvania"  # Modifico l'elemento della lista
states_of_america.append("Iowa")    # Aggiunge un'elemento alla fine della lsita
states_of_america.extend(["Carolina", "Vermont", "Kentucky"])   # Aggiunge elementi multipli alla lista

print(states_of_america)
"""

# WHO PAYS THE BILL
"""
nome_da_aggiungere = str(input("Inserisci il nome della persona se non ci sono altre persone da aggiungere premi il "
                               "tasto INVIO : \n"))
name_list = []
while nome_da_aggiungere != '':
    name_list.append(nome_da_aggiungere)
    nome_da_aggiungere = str(input("Inserisci il nome della persona : \n"))

print(name_list)

random_person = random.randint(0, len(name_list))

print(f"Oggi la cena verrà pagata da : {name_list[random_person]}")

"""

# IndexError : List index out of range
# Significa che sto cercando di chiamare una posizione della lista che non esiste
"""
fruits = ["fragole", "mele", "banane", "pere"]
vegetables = ["Carote", "Zucchine", "Patate"]

# Nested List

raccolto = [fruits, vegetables]
print(raccolto[1][2])
"""

# ROCK PAPER SCISSOR GAME DAY 4 PROJECT

scelta_personale = int(input("Inserisci 1 per giocare ROCK"
                             "Inserisci 2 per giocare PAPER"
                             "Inserisci 3 per giocare SCISSOR"
                             "Inserisci 0 per terminare il gioco : \n"))
RPS_list = ["ROCK", "PAPER", "SCISSOR"]

while scelta_personale != 0:
    scelta_personale -= 1
    random_value = random.randint(0, 2)

    scelta_random = RPS_list[random_value]

    scelta_input = RPS_list[scelta_personale]

    if scelta_input == scelta_random:
        print(f"Hai scelto {scelta_input} , il computer ha giocato {scelta_random}")
        print("Patta")
    elif (scelta_input == "ROCK" and scelta_random == "SCISSOR") or (scelta_input == "PAPER" and scelta_random == "ROCK") or (scelta_input == "SCISSOR" and scelta_random == "PAPER"):
        print(f"Hai scelto {scelta_input} , il computer ha giocato {scelta_random}")
        print("Hai Vinto!")
    else:
        print(f"Hai scelto {scelta_input} , il computer ha giocato {scelta_random}")
        print("Hai Perso!")

    scelta_personale = int(input("Inserisci 1 per giocare ROCK"
                                 "Inserisci 2 per giocare PAPER"
                                 "Inserisci 3 per giocare SCISSOR"
                                 "Inserisci 0 per terminare il gioco : \n"))






