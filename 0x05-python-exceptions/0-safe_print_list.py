#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if my_list is None:
        my_list = []
    
    j = 0
    printed = 0

    for i in range(min(x, len(my_list))):
        try:
            print("{}".format(my_list[i]), end="")
            printed += 1
        except IndexError:
            continue

    print()
    return printed