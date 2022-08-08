#!/usr/bin/python3
age = int(input("Enter your age: "))
if (age == 5):
    print("Go to kindergarten.")
elif (age >= 6 ) and (age <= 17):
    print(f"Go to grade {age - 5}.")
elif (age > 17):
    print("Go to college.")
else:
    print("You just a cute baby!")
