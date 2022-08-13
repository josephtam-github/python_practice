#!/usr/bin/python3
def return_odd(_list, func):
    odd_list = []
    for i in range(0, len(_list)):
        if func(_list[i]):
            odd_list.append(_list[i])
    return odd_list

def even_or_odd(list_value):
    if list_value % 2 == 0:
        return False
    else:
        return True

def main():
    ran_list = [1,2,3,45,21,1,43,345,2,4,3,123,5,4578,3,463,1]
    print(return_odd(ran_list, even_or_odd))

main()
