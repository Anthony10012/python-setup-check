"""
Name: Calculatrice.py
Author: <Anthony Simond>
Date : 07.11.2024
"""

def add(nb,nb2):
    print(nb+nb2)
    return nb+nb2
def sub(nb,nb2):
    print(nb-nb2)
    return nb-nb2
def mul(nb,nb2):
    print(nb*nb2)
    return nb*nb2
def div(nb,nb2):
    print(nb/nb2)
    return nb/nb2



nb= float(input("Donne moi un premier chiffre:"))
operator = input("Donner un opérateur:")
nb2=float(input("Donne moi un  deuxième chiffre:"))


if operator == "+":
    print(nb+nb2)
elif operator == "-":
    print(nb-nb2)
elif operator == "*":
    print(nb*nb2)
elif operator == "/":
    print(nb/nb2)




