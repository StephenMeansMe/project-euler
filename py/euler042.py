# ======================================================================
# PROJECT EULER PROBLEM NO. 42: CODED TRIANGLE NUMBERS
# ----------------------------------------------------------------------
# How many words in a given text file are 'triangle words'?
# ======================================================================

import math as m
import string

alphabet = string.ascii_uppercase

def isTri(n):
    return m.sqrt(8*n + 1) == int(m.sqrt(8*n + 1))

def wordScore(word):
    return sum(alphabet.index(letter) for letter in word)

with file.open("euler42.txt") as f:
    
