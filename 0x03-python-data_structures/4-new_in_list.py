#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = my_list[:]
    if (idx >= 0):
        list[3] = 9
        return list

    elif idx > len(my_list):
        list[idx] = element
        return list
