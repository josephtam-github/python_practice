#!/usr/bin/python3
import math

def c_cipher(string, places):
    new_str = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if places > 25:
        places = places % 25
    for char in string:
        if char.isalpha():                
            if char.isupper():
                index = alphabet.find(char.lower())
                new_str = new_str + alphabet[(index + places) % 25].upper()
            if char.islower():
                index = alphabet.find(char)
                new_str = new_str + alphabet[(index + places) % 25]
        else:
            new_str = new_str + char
    return new_str
