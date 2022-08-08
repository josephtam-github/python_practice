#!/usr/bin/python3
amount = float(input("Enter investment amount: "))
interest = float(input("Enter expected intrest : "))
year = 0   
while (year < 10):
    amount = amount + amount * (interest / 100)
    year += 1
print(f"Total earnings after 10 years is {amount:.2f}")
