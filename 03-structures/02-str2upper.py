#!/usr/bin/python3
secret_code = ""
cap_str = ""
try:
    lowcase_str = input("Enter a lower case word to hide in uppercase: ")
    if " " in lowcase_str or type(lowcase_str == int):
        print("Enter a word (no spaces)")
    else:
        for letter in lowcase_str:
            secret_code = secret_code + str(ord(letter))
            cap_str = cap_str + chr(ord(letter) - 32)
        print("SECRET CODE: ", secret_code)
        print("ORIGINAL TEXT: ", cap_str)
except ValueError:
    print("Please enter a string")
