#!/usr/bin/python3
import random
randList = []
for i in range(1,6):
    randList.append(random.randint(1,9))

print(randList)

#BUBBLE SORT
i = len(randList) - 1

while i > 1:
    j = 0
    while j < i:
        if randList[j] > randList[j + 1]:
            temp = randList[j]
            randList[j] = randList[j + 1]
            randList[j + 1] = temp
        j += 1
    i -= 1

print(randList)
