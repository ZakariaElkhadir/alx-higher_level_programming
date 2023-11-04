#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        reverse = len(my_list) -1

        while reverse >= 0:
            print("{:d}".format(my_list[reverse]))
            reverse -= 1
