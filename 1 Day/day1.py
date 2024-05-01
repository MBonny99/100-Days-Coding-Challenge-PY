"""
print("Hello World!")
# aggiungere backslash per andare a capo direttamente senza fare un'altra print
# posso concatenare due stringhe tramite il simbolo +

name = str(input("What is your name? "))
# il metodo input permette all'utente di inserire un input
# tramite il metodo input possiamo inserire un valore in una variabile
# si possono "limitare" i tipi di dati che si vogliono ricevere
print("Hi " + name)

print(len(name))
# il metodo Len restituisce il numero di caratteri dentro le parentesi
# conviene usare nomi di variabili significativi in modo tale da rendere il codice di pi facile comprensione
"""
# PROJECT BAND NAME GENERATOR

print("Hello , this is a band generator software , "
      "it will use the information that you will "
      "provide to create a beautiful band name")

city = str(input("Where are you born? "))
pet = str(input("What is your pet name? "))

band_name = city + " " + pet

print("Your band Name is : " + band_name)




