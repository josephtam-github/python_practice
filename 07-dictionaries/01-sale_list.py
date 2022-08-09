#!/usr/bin/python3
sale_list = []
while True:
    choice = str(input("Do you want to add more customers (y or n) ?"))
    if choice == "n":
        print(sale_list)
        break
    if choice == "y":
        fName, lName = str(input("What is the customers first and last name?")).split(" ")
        sale_list.append({'fName': fName, 'lName': lName})

