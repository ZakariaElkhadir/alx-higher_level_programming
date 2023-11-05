#!/usr/bin/python3
def max_integer(my_list) == 0:
    if len (my_list) == 0:
        return ("None")
    s = my_list[0]
    for i in my_list:
        if i > s:
            s = i
    return (s)
