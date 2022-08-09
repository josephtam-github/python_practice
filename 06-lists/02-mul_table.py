#!/usr/bin/python3
mulTable = []

for i in range(1,11):
    mulTable.append(list(j*i for j in range(1,11)))
#DID THE MULTIDIMENSIONA LIST WITH THREE LINES OF CODE :o

for i in range(0,10):
    for j in range(0,10):
        print(f"|{j + 1} x {i + 1} = {mulTable[i][j]}", end="\t")
    print()
