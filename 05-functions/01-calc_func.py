#!/usr/bin/python3
def calc(string):
    try:
        array = string.split(" ")
        variable = array[0]
        operand = int(array[2])
        answer  = int(array[4])
        print(variable, "=", (answer - operand))
    except ValueError:
        print("Please use the 'format x + number = number'")
