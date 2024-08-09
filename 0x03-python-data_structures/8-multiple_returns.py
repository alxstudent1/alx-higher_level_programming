#!/usr/bin/python3
def multiple_returns(sentence):
    taille = len(sentence)
    firs_char = sentence[0]
    if taille == 0:
        firs_char = None
        return taille, firs_char
    else:
        return taille, firs_char