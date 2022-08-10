#!/usr/bin/python3
nth = int(input("How many values of fibonaci do you want? "))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(1,(nth + 1)):
    print(fib(i), end="\n")
print("All done")
