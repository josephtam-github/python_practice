#!/usr/bin/python3
number = 8

while True:
    try:
        guess = int(input("Enter a number between 1 and 10: "))
        if number == guess:
            print("You guessed the correct number!")
            break
        else:
            print("Wrong nuumber :(")
    except ValueError:
        print("Please input a number")
