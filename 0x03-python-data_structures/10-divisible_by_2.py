#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            list[count] = True
        else:
            list[count] = False
    return list