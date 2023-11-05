#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    Sec_list = my_list[:]

    if 0 <= idx < len(my_list):
        Sec_list[idx] = element
    return Sec_list
