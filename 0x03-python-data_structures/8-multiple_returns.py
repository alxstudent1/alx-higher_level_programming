#!/usr/bin/python3
def multiple_returns(sentence):
    taille = len(sentence)
    if taille == 0:
        firs_char = None
        couple = (taille, first_char)
        return couple
    else:
        first_char = sentence[0]
        couple = (taille, first_char)
        return couple
