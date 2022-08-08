#!/usr/bin/python3
stack = int(input("How tall do you want your tree to be: "))
tree = 0
for i in range(stack):
    print(" " * (stack - i) , "#" * (1 + tree), " " * (stack - i))
    tree += 2
print(" " * (stack), "#", " " * (stack))
#The hint was that we'd need three four loops but I used only 1 
