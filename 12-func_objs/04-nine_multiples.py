#!/usr/bin/python3
from random import choice, randint

rand_list = []
for i in range(100):
    rand_list.append(randint(1,1000))

def count_nine(_list):
    nines =  len(list(filter(lambda x: x % 9 == 0, _list)))
    break_count = -1
    for i in _list:
        break_count += 1
        if break_count % 10 == 0:
            print()
        print(f"{i}", end="\t")
    print(f"\nThere are {nines} nines in the above list")

count_nine(rand_list)
