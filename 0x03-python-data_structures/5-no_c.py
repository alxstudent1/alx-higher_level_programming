#!/usr/bin/python3
def no_c(my_string):
    resultat = "".join([char for char in my_string if char.lower() != "c"])
    return resultat