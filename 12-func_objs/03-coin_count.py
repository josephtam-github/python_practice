#!/usr/bin/python3
from random import choice, randint

rand_list = []
for i in range(100):
    rand_list.append(choice(["H","T"]))

def count_side(_list):
    H =  len(list(filter(lambda x: x == "H", _list)))
    T = len(_list) - H
    print(f"Heads: {H}\nTails: {T}")

count_side(rand_list)
