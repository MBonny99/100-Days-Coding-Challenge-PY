# Control Flow and conditional statement

# if/else

"""

if condition:
    do this
else:
    do this

"""
"""
water_level = 50

if water_level > 80:
    print("Drain Water")
else:
    print("Pour Water")


altezza = float(input("Inserisci la tua altezza : "))
if altezza > 120:
    print("Puoi acqistare il Ticket per il rollercoaster")
else:
    print("Non puoi acquistare il ticket")

# Nested If/elif/else Statement
age = int(input("Inserisci la tua età: "))
if( altezza > 120):
    if(age > 35):
        print("il tuo ticket costa 10€")
    elif(age > 18 and age < 35):
        print("il tuo ticket costa 8€")
    else:
        print("il tuo ticket costa 5€")
else:
    print("Non puoi Acquistare il ticket")

"""

"""
# BMI CALCULATOR

height = float(input("Inserisci la tua altezza : "))
weight = float(input("Inserisci il tuo peso : "))

if height > 10:
    height = height/100

bmi = weight / (height * height)

print(f"il tuo BMI è di : {bmi}")

if bmi < 18.5:
    print("you are underweight")
elif bmi < 25:
    print("You are normal weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("you are obese")
else :
    print("you are clinically obese")
    
"""

# Multiple IF Statement
"""
altezza = 100
peso = 20

if altezza == 100: 
    print("sei alto un metro ed un carciofo")

if altezza == 100 and peso == 20:
    print("sei alto un metro ed un carciofo e sei secco come uno stuzzicadente")
    
    
"""

# Logical Operator  AND , OR , NOT etc...
"""
if a > b and b > c:
    print("a")

if a > b or a < c:
    print("b")

if not a > b :    #se la condizione viene verificata, inverti il valore del bool
    print("b")
"""

# Day 3 PROJECT TREASURE ISLAND

print("Welcome to Treasure ISLAND , Your Mission is to find the treasure  \n")
print("You left the village and are now at the border of the mystic forest  \n"
      "you have decide to enter the forest but at some point  \n"
      "you are lost , now you have two choise , go right or go left. \n")
first_decision = str(input("make you decision by typing right or left : \n"))
second_decision = ''
third_decision = ''
if first_decision.lower() == "right":
    print("Sadly you encounter a monster, you are dead.")
else:
    print("You arrive at a lake , now you have to decide if you want to swim or wait for a boat to arrive: ")
    second_decision = str(input("make you decision by typing swim or boat : \n"))
    if second_decision.lower() == "swim":
        print("Sadly you don't know how to swim , so you are dead.")
    else:
        print("Good for you , a man with a boat decide to help you cross the lake \n"
              "Now that you crossed the lake, you found a mansion that have three door \n"
              "The first door is blue , the second door is red and the third is green, you can only chose 1 door.")
        third_decision = str(input("make your choise by typing blue , red or green : \n"))
        if third_decision.lower() == "blue":
            print("You Won the game")
        else:
            print("You enter a dimensional pocket and have to suffer for the rest of the eternity")


