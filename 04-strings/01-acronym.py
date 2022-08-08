#!/usr/bin/python3

acronym = ""
sentence = str(input("Enter a sentence: "))
str_array = sentence.split(" ")
for word in str_array:
    acronym = acronym + word[0].upper()
print(acronym)


