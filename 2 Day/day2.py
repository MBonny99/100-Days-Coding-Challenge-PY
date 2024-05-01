"""
# Data Type

# String

# Subscript si inizia a contare dallo 0
prima_lettera = "Hello"[0]

print(prima_lettera)

# Integer

somma = 123 + 345

print(somma)

# Si possono inserire _ in un numero per rendere più leggibile il numero

large_number = 123_456_789_123

# Float

pi = 3.14159

# Boolean

booleantrue = True
booleanfalse = False

# Error
# len(1234) = TypeError: object of type 'int' has no len()

# num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.")
# TypeError: can only concatenate str (not "int") to str

# type check

print(type(booleantrue))  # <class 'bool'>

# type conversion str() , int() , float() ,etc...

stringa_boolTrue = str(booleantrue)

print(stringa_boolTrue)

# Mathematical Operation

# a + b , a - b , a * b , a / b             BASIC Operation
# a ** b                                    Exponent
# PEMDAS logics = Parentheses , Exponents , Multiplication , Division , Addition , Subtraction
print(3 * 3 + 3 / 3 - 3)  # ---- (3*3)+(3/3)-3 = 7

# Number Manipulation And F string

# round(number , digits) round(2.677777 , 2) = 2.67
# // division to integer

print(8//3)

# Operazioni di calcolo/assegnazione diretta +=  -=  *=  /=

result = 4/2  # 2
result /= 2   # 1
print(result)

# f davanti ad una stringa permette di inserire un valore che non sia di tipo stringa dentro {}
print(f"The result is {result}")
"""

# PROJECT 2 TIPS CALCULATOR

print("Welcome to the tip calculator! ")
totale = float(input("Quant'è il totale da pagare? "))
num_persone = int(input("In quanti siete? "))
tip_percentage = int(input("Quanto volete lasciare di mancia? 5-10-15-20 % "))
totale_da_pagare = round((totale/num_persone) + ((totale * (tip_percentage / 100)) / num_persone), 2)
print(f"Il Totale che ogni Persona dovrà pagare è : {totale_da_pagare}")
