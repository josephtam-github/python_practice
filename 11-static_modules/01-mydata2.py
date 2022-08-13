#!/usr/bin/python3
import os
file = open("mydata2.txt", mode="w", encoding="utf-8")
file.write("hello world")
def with_as(filename, _encoding="utf-8"):
    try:
        alias = open(filename, encoding=_encoding)
        print(alias.read())
        alias.closed
    except FileNotFoundError:
        print("The file was not found")
    finally:
        print("This runs no matter what!")

def main():
    with_as("mydata2.txt")
    print()
    with_as("mydata3.txt")

main()
